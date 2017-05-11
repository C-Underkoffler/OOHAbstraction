#!/usr/bin/env python
# encoding: utf-8

#Import a variety of things
import os
import sys
import logging
FORMAT = "%(filename)s:%(lineno)d %(funcName)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


import re
import imp
import itertools
import cPickle as pickle

# do this before we have a chance to import openbabel!
import rdkit, rdkit.Chem, rdkit.Chem.rdDistGeom, rdkit.DistanceGeometry

from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy.reaction import Reaction
from rmgpy.kinetics import PDepArrhenius, PDepKineticsModel

from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.kinetics import KineticsDepository, KineticsRules
from rmgpy.qm.main import QMCalculator


if len(sys.argv)>1:
    i = int(sys.argv[-1])
elif os.getenv('SLURM_ARRAY_TASK_ID'):
    i = int(os.getenv('SLURM_ARRAY_TASK_ID'))
elif os.getenv('LSB_JOBINDEX'):
    i = int(os.getenv('LSB_JOBINDEX'))
else:
    #raise Exception("Specify a TS number!")
    logging.warning("Number not specified as script argument or via environment variable, so using default")
    i = 1
logging.info("RUNNING WITH JOB NUMBER i = {}".format(i))

rxnFamilies = ['H_Abstraction']  # Only looking at H_abstraction via OOH

logging.info('Loading RMG Database ...')
rmgDatabase = RMGDatabase()
databasePath = os.path.abspath(os.path.join(os.getenv('RMGpy', '..'), '..', 'RMG-database', 'input'))
logging.info(databasePath)
rmgDatabase.load(databasePath,
                 kineticsFamilies=rxnFamilies,
                 transportLibraries=[],
                 reactionLibraries=[],
                 seedMechanisms=[],
                 thermoLibraries=['primaryThermoLibrary', 'KlippensteinH2O2', 'thermo_DFT_CCSDTF12_BAC', 'CBS_QB3_1dHR' ],
                 solvation=False,
                 )
logging.info('RMG Database Loaded')

loadSpecies = rmgDatabase.kinetics.families[rxnFamilies[0]]
species_dict_file = os.path.expanduser('~/Code/OOHabstraction/Biofuels/chemkin/species_dictionary.txt')
species_dict = loadSpecies.getSpecies(species_dict_file)
logging.info("Species Dictionary loaded")
print species_dict

file_object = open(os.path.expanduser('~/Code/OOHabstraction/Biofuels/chemkin/chem_annotated.inp'), 'r')
mechLines = file_object.readlines()
logging.info("Chemkin loaded")



rxnList = []
gotit = []
for rxnFamily in rxnFamilies:
	for k, line in enumerate(mechLines):
		if line.startswith('! Template reaction: {0}'.format(rxnFamily)):
			for m in range(10):
				reaction = mechLines[k+m].split()[0]
				if not reaction.startswith('!'):
					break
			if reaction not in gotit:
				gotit.append(reaction)
				rxnList.append((rxnFamily, mechLines[k+m]))
logging.info(rxnList)
logging.info(type(rxnList))
"""
def sorter_key(rxn):

    A key to generate the sort order for reactions.
    Needs to be consistent across runs, but we want small reactions
    first, so that it runs faster.

    weight = 0.
    for r in rxn.reactants:
        weight += r.molecule[0].getMolecularWeight()
    return (weight, repr(rxn))
"""



logging.info("Reaction list generated")
reactionTuple = rxnList[i-1]
rxnFamily, reactionLine = reactionTuple
chemkinRxn, A, n, Ea = reactionLine.split()
reactants, products = chemkinRxn.split('=')
logging.info("This reaction:")
logging.info(str(chemkinRxn))
logging.info(repr(chemkinRxn))
logging.info(reactants)
logging.info(products)
if rxnFamily in ['H_Abstraction']:
	rSpecies1, rSpecies2 = [species_dict[j] for j in reactants.split('+')]
	pSpecies1, pSpecies2 = [species_dict[j] for j in products.split('+')]

	rSpecies1.generateResonanceIsomers()
	rSpecies2.generateResonanceIsomers()
	pSpecies1.generateResonanceIsomers()
	pSpecies2.generateResonanceIsomers()

	testReaction = Reaction(reactants=[rSpecies1, rSpecies2], products=[pSpecies1, pSpecies2], reversible=True)
	reactionList = []
	for moleculeA in rSpecies1.molecule:
		for moleculeB in rSpecies2.molecule:
			tempList = rmgDatabase.kinetics.generateReactionsFromFamilies([moleculeA, moleculeB], [], only_families=[rxnFamily])
			for rxn0 in tempList:
				reactionList.append(rxn0)
logging.info("generateReactionsFromFamilies successfuly performed")
gotOne=False
for reaction in reactionList:
	# Check if any of the RMG proposed reactions matches the reaction in the mechanism
	if testReaction.isIsomorphic(reaction):
		# Now add the labeled atoms to the Molecule, and check all labels were added
		atLblsR = dict([(lbl[0], False) for lbl in reaction.labeledAtoms])
		atLblsP = dict([(lbl[0], False) for lbl in reaction.labeledAtoms])

		for reactant in reaction.reactants:

			reactant.clearLabeledAtoms()
			for atom in reactant.atoms:
				for atomLabel in reaction.labeledAtoms:
					if atom==atomLabel[1]:
						atom.label = atomLabel[0]
						atLblsR[atomLabel[0]] = True
		for product in reaction.products:

			product.clearLabeledAtoms()
			for atom in product.atoms:
				for atomLabel in reaction.labeledAtoms:
					if atom==atomLabel[1]:
						atom.label = atomLabel[0]
						atLblsP[atomLabel[0]] = True
		if all( atLblsR.values() ) and all( atLblsP.values() ):
			gotOne=True
			break

def sorter_key(rxn):
    """
    A key to generate the sort order for reactions.
    Needs to be consistent across runs, but we want small reactions
    first, so that it runs faster.
    """
    weight = 0.
    for r in rxn.reactants:
        weight += r.molecule[0].getMolecularWeight()
    return (weight, repr(rxn))



qmCalc = QMCalculator(
                        software='gaussian',
                        method='m062x',
                        fileStore=os.path.expandvars('/gss_gpfs_scratch/harms.n/QMfiles'),
                        scratchDirectory=os.path.expandvars('/gss_gpfs_scratch/harms.n/QMscratch'),
                        )

def calculate(reaction):
    logging.info("Calculating reaction rate for {!s}".format(reaction))
    rxnFamily = reaction.family
    logging.info("Selecting the appropriate TS distance database for family {!r}".format(rxnFamily))
    tsDatabase = rmgDatabase.kinetics.families[rxnFamily].transitionStates
    logging.info("Calculating kinetic data by calling qmCalc.getKineticData")
    reaction = qmCalc.getKineticData(reaction, tsDatabase)
    logging.info("Removing 'core*' files")
    for files in os.listdir('./'):  # This deletes any files with names starting 'core' which fill up your disk space on discovery.
        if files.startswith('core'):
            try:
                os.remove(files)
            except:
                logging.info("Error deleting files {}".format(files))
    if reaction.kinetics:
        logging.info("Yay, reaction kinetics calculated!!!")
        logging.info(repr(reaction))
    else:
        logging.info("Boo, reaction kinetics not calculated!!!")
    return reaction


def performCalcs(chemkinRxn):

    logging.info("chemkinRxn: {!r}".format(chemkinRxn))
    # Ensure all resonance isomers have been generated
    logging.info('Ensuring resonance isomers have been generated')
    for species in itertools.chain(chemkinRxn.reactants, chemkinRxn.products):
        print(type(species))
        species = species.generateResonanceIsomers()

    testReaction = Reaction(reactants=chemkinRxn.reactants, products=chemkinRxn.products, reversible=True)

    reactants = [species for species in chemkinRxn.reactants]
    # reactant_molecules is a list of lists of resonance isomers,
    # eg. a bimolecular reaction where the second reactant has 2 isomers is: [[r1],[r2i1,r2i2]]

    products = [species for species in chemkinRxn.products]
    # products is a list of molecule objects (only one resonance form of each product), eg [p1, p2]
    print reactants
    #print type(reactant_molecules[0])
    print products

    checkRxn = rmgDatabase.kinetics.generateReactionsFromFamilies(reactants, products, only_families=rxnFamilies)
    if len(checkRxn) == 1:
        logging.info("Generated one reaction:")
        logging.info(checkRxn)
        reaction = checkRxn[0]
    else:  # didn't break from for loop
        for reaction in checkRxn:
            logging.info("Generated these reactions:")
            logging.info(reaction)
            reaction = checkRxn[0]
        raise Exception("Couldn't generate exactly one reaction matching {} in family {}".format(chemkinRxn, rxnFamilies))

    logging.info("The reaction of interest is as follows: ")
    logging.info(reaction)

    logging.info("asserting that the testReaction is Isomorphic")
    assert testReaction.isIsomorphic(reaction)
    logging.info("reaction: {!r}".format(reaction))

    atLblsR = dict([(lbl[0], False) for lbl in reaction.labeledAtoms])
    atLblsP = dict([(lbl[0], False) for lbl in reaction.labeledAtoms])

    gotOne = False
    logging.info("Labeling reactant atoms")
    for reactant in reaction.reactants:
        reactant = reactant
        reactant.clearLabeledAtoms()
        for atom in reactant.atoms:
            for atomLabel in reaction.labeledAtoms:
                if atom == atomLabel[1]:
                    atom.label = atomLabel[0]
                    atLblsR[atomLabel[0]] = True

    logging.info("Labeling product atoms")
    for product in reaction.products:
        product = product
        product.clearLabeledAtoms()
        for atom in product.atoms:
            for atomLabel in reaction.labeledAtoms:
                if atom == atomLabel[1]:
                    atom.label = atomLabel[0]
                    atLblsP[atomLabel[0]] = True

    if all(atLblsR.values()) and all(atLblsP.values()):
        gotOne = True

    rxnFamily = reaction.family
    assert gotOne, "Couldn't label all the atoms using the reaction family template"

    logging.info("We have generated a {!s} reaction that matches, and used it to label the atoms.".format(rxnFamily))

    logging.info("Calculating reaction kinetics")
    reaction = calculate(reaction)

    logging.info("For reaction {0!r}".format(reaction))
    if reaction.kinetics:
        logging.info("We have calculated kinetics {0!r}".format(reaction.kinetics))

    else:
        logging.warning("Couldn't calculate kinetics.")


    if reaction.kinetics and False:
        """
        Return the rate coefficient in the appropriate combination of cm^3,
        mol, and s at temperature `T` in K and pressure `P` in Pa.
        """
        importKin = chemkinRxn['rmgPyKinetics']
        Temp = 1000  # Kelvin
        idx = str(i)
        row = [idx, rxnFamily]
        row.extend([mol.label for mol in reaction.reactants])
        row.extend([mol.label for mol in reaction.products])

        rateCal = reaction.calculateTSTRateCoefficient(Temp)
        row.extend(['AutoTST_fwd', str(rateCal)])

        if isinstance(importKin, PDepArrhenius) or isinstance(importKin, PDepKineticsModel):
            row.extend([smiles_dict[entry], str(importKin.getRateCoefficient(Temp, 1000000))])  #1000000 Pa = 10 bar
        else:
            row.extend([smiles_dict[entry], str(importKin.getRateCoefficient(Temp))])

        famDatabase = rmgDatabase.kinetics.families[rxnFamily]
        famDatabase.addKineticsRulesFromTrainingSet(thermoDatabase=rmgDatabase.thermo)
        famDatabase.fillKineticsRulesByAveragingUp()

        # Using the `testReaction` will keep the reaction direction the same as the model
        rxnTemplate = famDatabase.getReactionTemplate(testReaction)
        kList = famDatabase.getKinetics(testReaction, rxnTemplate)

        allRates = []
        kComments = []
        for rate in kList:
            k = rate[0]
            if k:
                label = rate[1]
                if isinstance(label, KineticsDepository):
                    label = label.label
                elif isinstance(label, KineticsRules):
                    label = label.label
                if label.lower() == 'rate rules':
                    kComments = k.comment.split('\n')
                allRates.append((label, k.getRateCoefficient(Temp)))

        kDict = {'Rate Rules': []}
        for kTuple in allRates:
            if kTuple[0] == 'AutoTST':
                kDict['AutoTST'] = kDict['AutoTST'] + [kTuple[1]]
            elif kTuple[0] == 'rate rules':
                kDict['Rate Rules'] = kDict['Rate Rules'] + [kTuple[1]]
            elif kTuple[0].endswith('/NIST'):
                kDict['NIST'] = kDict['NIST'] + [kTuple[1]]
            elif kTuple[0].endswith('/rules'):
                kDict['KineitcsRules'] = kDict['KineitcsRules'] + [kTuple[1]]

        # Print the values in order
        kineticsTypes = ['Rate Rules']  #['AutoTST', 'Rate Rules', 'NIST', 'KineitcsRules']
        for kinType in kineticsTypes:
            row.append(kinType)
            if kDict[kinType] == []:
                row.append('no Val')
            else:
                for val in kDict[kinType]:
                    row.append(str(val))

        # Store line containing reaction from corresponding chemkin file
        row.append(smiles_dict[entry])
        row.append(chemkinRxn['chemkinKinetics'].strip())

        # Store rmgpy kinetics group comments
        row = row + kComments

        folderPath = os.path.join('KinTxtFiles', idx)

        if not os.path.exists(folderPath):
            os.makedirs(folderPath)

        input_string = ','.join(row)
        with open(os.path.join(folderPath, smiles_dict[entry] + '_kinetics.txt'), 'w') as kinTxt:
                kinTxt.write(input_string)
rxn = reactionList[0]
performCalcs(rxn)

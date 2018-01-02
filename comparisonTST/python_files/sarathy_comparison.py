import os
if os.path.exists("/gss_gpfs_scratch/"):
    RMG_PY_PATH = os.path.expanduser('/gss_gpfs_scratch/westgroup/Importer/RMG-Py/')
    RMG_MODELS_PATH = os.path.expanduser('/gss_gpfs_scratch/westgroup/Importer/RMG-models')
else:
    RMG_PY_PATH = os.path.expanduser('~/Code/RMG-Py/')
    RMG_MODELS_PATH = os.path.expanduser('~/Code/RMG-models')
import sys
import re

sys.path.insert(1,RMG_PY_PATH)
from rmgpy.molecule import Molecule
import rmgpy.kinetics
import rmgpy.rmg
import rmgpy.data
import rmgpy.data.kinetics
import numpy
import cPickle as pickle
from collections import Counter, defaultdict
from rmgpy.reaction import Reaction
import pandas as pd
import ck2cti
import cantera as ct
import itertools
import random
import numpy as np
import itertools


# Getting the OOH reactions
f = open("../../autotst_kinetics.pkl","r")
autotst_kinetics = pickle.load(f)
ooh_reactions = []
for rxn in autotst_kinetics:
    reactants, products = rxn.label.split("_")
    r1, r2 = reactants.split('+')
    p1, p2 = products.split('+')
    if "OO" in [r1, r2, p1, p2] and "[O]O" in [r1, r2, p1, p2]:
        ooh_reactions.append(rxn)

### Looking at the sarathy butanol model
master = 'CombFlame2012/2028-Sarathy'

# Find and read the chemkin file
with open(os.path.join(RMG_MODELS_PATH, master,'import.sh')) as infile:
    shellscript = infile.read()
reactions_filename = re.search('--reactions\s+(\S+)',shellscript).group(1)
reactions_filepath = os.path.join(RMG_MODELS_PATH,master,reactions_filename)
thermo_filename = re.search('--thermo\s+(\S+)',shellscript).group(1)
thermo_filepath = os.path.join(RMG_MODELS_PATH,master,thermo_filename)
print(reactions_filepath)
print(thermo_filepath)
with open(reactions_filepath) as infile:
    chemkin = infile.readlines()
print "".join(chemkin[:4]) # print first 4 lines only

parser = ck2cti.Parser()
surfaces = parser.convertMech(inputFile=reactions_filepath,
                              thermoFile=thermo_filepath,
                              transportFile=None,
                              surfaceFile=None,
                              phaseName=None,
                              outName='~/Code/OOHAbstraction/comparisonTST/reference_files/master_sarathy.cti',
                              permissive=True)

dict_path = os.path.join(RMG_MODELS_PATH, master, 'RMG-Py-kinetics-library', 'dictionary.txt')
print "Loading species_dict from",dict_path
species_dict = rmgpy.data.kinetics.KineticsLibrary().getSpecies(dict_path)

smiles_to_nickname_dict = {}
for species in species_dict.itervalues():
    for mol in species.molecule:
        smiles_to_nickname_dict[mol.toSMILES()] = species.label

sarathy_rxns = []
for r in parser.reactions:
    split_string = str(r).split()
    if not (smiles_to_nickname_dict["OO"] in split_string and smiles_to_nickname_dict["[O]O"] in split_string):
        continue

    # Creating a list of possible reaction labels
    reactants = [species_dict[n].molecule[0].toSMILES() for n in r.reactantString.split(' + ')]
    products = [species_dict[n].molecule[0].toSMILES() for n in r.productString.split(' + ')]
    joined_reactant_orders = ['+'.join(order) for order in itertools.permutations(reactants)]
    joined_product_orders = ['+'.join(order) for order in itertools.permutations(products)]
    possible_labels = ['_'.join((joined_r, joined_p)) for joined_r in joined_reactant_orders for joined_p in joined_product_orders]

    for reaction in ooh_reactions:
        ooh_reactants, ooh_products = reaction.label.split("_")
        r1, r2 = ooh_reactants.split("+")
        p1, p2 = ooh_products.split("+")
        ooh_smiles = [r1, r2, p1, p2]

        # Creating a dictionary to decode inchikeys into smiles
        inchikey_to_smiles_dict = {}
        for smiles in ooh_smiles:
            inchikey_to_smiles_dict[Molecule(SMILES=smiles).toInChIKey()] = smiles

        # Setting the reactant and product labels as the nickname given in the model
        if reaction.label in possible_labels:
            for reactant in reaction.reactants:
                inchi_key = reactant.label.split("-u")[0]
                if not reactant.label in smiles_to_nickname_dict.itervalues():
                    reactant.molecule = [Molecule(SMILES=inchikey_to_smiles_dict[inchi_key])]
                    reactant.label = smiles_to_nickname_dict[inchikey_to_smiles_dict[inchi_key]]

            for product in reaction.products:
                inchi_key = product.label.split("-u")[0]
                if not product.label in smiles_to_nickname_dict.itervalues():
                    product.molecule = [Molecule(SMILES=inchikey_to_smiles_dict[inchi_key])]
                    product.label = smiles_to_nickname_dict[inchikey_to_smiles_dict[inchi_key]]

            # Then append the reaction to our reaction list
            sarathy_rxns.append([r, reaction, reaction.toChemkin(), reaction.toCantera()])

sarathy_df = pd.DataFrame(sarathy_rxns)
sarathy_df.columns = ["Sarathy Reaction", "AutoTST Reaction", "AutoTST Reaction - Chemkin" , "AutoTST - Cantera"]

parser.energy_units = 'kcal/mol'
reactions_by_cti_string = {}
for entry in zip(sarathy_df.iloc[:,1], sarathy_df.iloc[:,2]):
    reaction, chemkin_string = entry
    kinetics = reaction.kinetics
    chemkin_string = '\n'.join([l for l in chemkin_string.splitlines() if not l.startswith('!')])
    chemkin_string
    cantera_reaction, reverse_reaction = parser.readKineticsEntry(chemkin_string, False)
    cti_string = str(cantera_reaction)
    reactions_by_cti_string[cti_string] = (reaction, chemkin_string, cantera_reaction)

print len(reactions_by_cti_string)
print '\n'.join(sorted(reactions_by_cti_string.keys()))

import textwrap
original_reactions = list()
alternatives_rates = defaultdict(list)
for i, r in enumerate(parser.reactions):
    original_reactions.append(r)
    assert original_reactions[i] == parser.reactions[i]

    if r in list(sarathy_df.iloc[:,0]):
        _, rmg_reaction, kinetics_options, ct_version_of_rmg_kinetics = sarathy_df[r == sarathy_df.iloc[:,0]].values[0]
        # we just want the rmg_reaction

        chemkin_string = rmg_reaction.toChemkin()
        chemkin_string = '\n'.join([l for l in chemkin_string.splitlines() if not l.startswith('!')])
        r2, reverse_reaction = parser.readKineticsEntry(chemkin_string, False)
        # r2 is the new replacement reaction

        r2.comment = r.comment
        r2.comment += '\n \nSUBSTITUTION: The following reaction was originally\n{}\n'.format(r.to_cti())
        r2.comment += 'But has been replaced with the following as seen in AutoTST'

        alternatives_rates[i].append(r2)

        print
        print '\n'.join(['# '+c for c in r2.comment.split('\n') if c])
        print r2.to_cti()

print "original reactions", len(parser.reactions)
print "reactions to change", len(alternatives_rates)
c = Counter(map(len,alternatives_rates.values()))
print "substitutions", sorted(c.items())
print "total variations", sum(map(len,alternatives_rates.values()))

outdir = '~/Code/OOHAbstraction/comparisonTST/reference_files/cantera_sub_models/sarathy/'
os.path.exists(outdir) or os.mkdir(outdir)
for f in os.listdir(outdir):
    os.unlink(os.path.join(outdir, f))

parser.writeCTI(outName=os.path.join(outdir,'master.0.0.cti'))
for i, options in alternatives_rates.iteritems():
    for j, replacement in enumerate(options):
        output_filename = 'master.{}.{}.cti'.format(i+1,j+1)
        parser.reactions[i] = replacement
        ## save the file!
        header = ["####################################################",
                  "##  Reaction {:2d} has been replaced with option {:2d}  ##".format(i+1,j+1),
                  "####################################################"]
        print "saving", output_filename
        parser.writeCTI(header=header, outName=os.path.join(outdir,output_filename))
        # restore original
        parser.reactions[i] = original_reactions[i]

def get_ignition_delay(cantera_file_path, temperature , pressure, stoichiometry=1.0, isomer='n'):
    """
    Get the ignition delay at temperature (K) and pressure (bar) and stochiometry (phi),
    for the butanol isomer (n,s,t,i)
    """
    try:
        ct.suppress_thermo_warnings(True)
    except AttributeError:
        print("Sorry about the warnings...")
    gas = ct.Solution(cantera_file_path)
    assert isomer in ['n','s','t','i'], "Expecting isomer n, s, t, or i not {}".format(isomer)
    oxygen_mole = 1.0
    argon_mole = 96./4.*oxygen_mole
    butanol_mole = stoichiometry * oxygen_mole/6.
    X_string = isomer + 'c4h9oh:{0}, o2:{1}, ar:{2}'.format(butanol_mole, oxygen_mole, argon_mole)
    gas.TPX = temperature, pressure*1e5, X_string
    reactor=ct.IdealGasReactor(gas)
    reactor_network=ct.ReactorNet([reactor])
    time=0.0
    end_time=1000e-3
    times=[]
    concentrations=[]

    pressures=[]
    temperatures=[]
    print_data = True
    while time < end_time:
        time=reactor_network.time
        times.append(time)
        temperatures.append(reactor.T)
        pressures.append(reactor.thermo.P)
        concentrations.append(reactor.thermo.concentrations)
        reactor_network.step(end_time)
    print("reached end time {0:.4f} ms in {1} steps ". format(times[-1]*1e3, len(times)))
    concentrations = np.array(concentrations)
    times = np.array(times)
    pressures = np.array(pressures)
    temperatures = np.array(temperatures)

    dTdt = (temperatures[1:] - temperatures[:-1]) / (times[1:] - times[:-1])

    step_with_fastest_T_rise = dTdt.argmax()
    if step_with_fastest_T_rise > 1 and step_with_fastest_T_rise < len(times)-2:
        ignition_time_ms = 1e3 * times[step_with_fastest_T_rise]
        print("At {0} K {1} bar, ignition delay time is {2} ms for {3}-butanol".format(temperature,pressure,ignition_time_ms,isomer))
        return ignition_time_ms
    else:
        print("At {0} K {1} bar, no ignition is detected for {2}-butanol" .format(temperature, pressure, isomer))
        return np.infty

ignition_delays = []
ignition_temps = np.arange(500, 2050, 100)
dff = pd.DataFrame(index=ignition_temps)
dff.index = ignition_temps

if not os.path.exists("~/Code/OOHAbstraction/comparisonTST/reference_files/ignition_delay_sarathy.pkl"):
    for cantera_file in os.listdir("~/Code/OOHAbstraction/comparisonTST/reference_files/cantera_sub_models/sarathy/"):
        identifier = cantera_file.split(".")[1]
        print cantera_file
        delays = []
        for ignition_temp in ignition_temps:
            delay = get_ignition_delay(os.path.join("~/Code/OOHAbstraction/comparisonTST/reference_files/cantera_sub_models/sarathy/", cantera_file),
                       temperature=ignition_temp,
                       pressure=1,
                       stoichiometry=1.0)

            delays.append(delay)
        test = pd.DataFrame(delays)
        test.columns = [identifier]
        test.index = ignition_temps
        dff = pd.concat([dff, test], axis=1)
    f=open("~/Code/OOHAbstraction/comparisonTST/reference_files/ignition_delay_sarathy.pkl", "w")
    pickle.dump(dff, f)
else:
    print"Pickle file for Heptane already created, passing for now."

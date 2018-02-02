import os
import sys
import logging
FORMAT = "%(filename)s:%(lineno)d %(funcName)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


import re
import imp
import itertools
import cPickle as pickle
import pandas as pd

# do this before we have a chance to import openbabel!
import rdkit, rdkit.Chem, rdkit.Chem.rdDistGeom, rdkit.DistanceGeometry

from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy.reaction import Reaction
from rmgpy import reaction
from rmgpy.kinetics import PDepArrhenius, PDepKineticsModel, Arrhenius, Eckart
from rmgpy.statmech.translation import *
from rmgpy.statmech.rotation import *
from rmgpy.statmech.vibration import *
from rmgpy.statmech.torsion import *

from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.kinetics import KineticsDepository, KineticsRules
from rmgpy.qm.main import QMCalculator
from rmgpy.statmech import Conformer, IdealGasTranslation, NonlinearRotor, HarmonicOscillator, LinearRotor
from rmgpy.species import Species, TransitionState

root_dir = "/gss_gpfs_scratch/harms.n/QMfiles/"
kinetics_files = []
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".kinetics"):
            kinetics_files.append(os.path.join(root_dir, file))
print kinetics_files
autotst_list = []
for kinetics_file in kinetics_files:
    print kinetics_file

    f = open(kinetics_file)


    reaction_string =  f.readlines()[-1].split("reaction = ")[-1].split("\n")[0]
    print reaction_string
    rxn = eval(reaction_string)
    if len(rxn.reactants) == 2 and len(rxn.products) == 2:
        # only looking at bimolecular reactions
        reactants, products = kinetics_file.split(root_dir)[-1].split(".kinetics")[0].split("_")
        r1, r2 = reactants.split("+")
        p1, p2 = products.split("+")
        if Molecule(SMILES=r1).toInChIKey() in rxn.reactants[0].label:
            rxn.reactants[0].molecule = [Molecule(SMILES=r1)]
            rxn.reactants[1].molecule = [Molecule(SMILES=r2)]
        else:
            rxn.reactants[1].molecule = [Molecule(SMILES=r1)]
            rxn.reactants[0].molecule = [Molecule(SMILES=r2)]

        if Molecule(SMILES=p1).toInChIKey() in rxn.products[0].label:
            rxn.products[0].molecule = [Molecule(SMILES=p1)]
            rxn.products[1].molecule = [Molecule(SMILES=p2)]
        else:
            rxn.products[1].molecule = [Molecule(SMILES=p1)]
            rxn.products[0].molecule = [Molecule(SMILES=p2)]

        autotst_list.append(rxn)

results = open("../reference_files/autotst_kinetics.pkl", "w")

pickle.dump(autotst_list, results)
results.close()

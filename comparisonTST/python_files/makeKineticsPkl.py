
"""
Reads in a pickle file from the importer project contating
a dictionaly of dictionaries of RMG kinetics (eg Arrhenius)
objects, one for each reaction for each model.

Makes a Pandas DataFrame containing log10(k) evaluated
at 1000 K and 1 bar.
Saves that Pandas DataFrame to a pickle
"""

import os, sys
rmg_path = os.getenv('RMGpy')
if rmg_path and rmg_path not in sys.path:
    sys.path.insert(1,rmg_path)
import pandas as pd
import cPickle as pickle
import re

import numpy as np



import rmgpy.kinetics
from rmgpy.molecule import Molecule
from rmgpy.reaction import Reaction
from collections import defaultdict, OrderedDict

with open("~Code/OOHabstraction/comparisonTST/reference_files/kinetics.pkl", "r") as f:
    importerKinetics = pickle.load(f)

def evalArrhenius(autoTSTExpression):
    """
    Converts a string to an Arrhenius object
    """
    if autoTSTExpression is np.nan:
        return autoTSTExpression
    try:
        my_string = str(autoTSTExpression).strip("'")
        print my_string
        result = eval(my_string, {}, {'Arrhenius': rmgpy.kinetics.Arrhenius,
                                     'MultiArrhenius': rmgpy.kinetics.MultiArrhenius,
                                     'PDepArrhenius': rmgpy.kinetics.PDepArrhenius,})
    except:
        result = autoTSTExpression
        raise
    return result

def RateCoefficients(arrhenius):
    """
    Takes an Arrhenius object, evaluates k at 1000K 1bar, and returns log10(k)
    """
    rate = np.nan
    try:
        rate = np.log10(arrhenius.getRateCoefficient(T=1000, P=1e5))
        print "Rate Calculated"
    except:
        print "No rate to calculate"
        pass
    return rate

for key in importerKinetics:
    try:
        #print importerKinetics[key]['AutoTST-OOHabstraction']
        del importerKinetics[key]['AutoTST-OOHabstraction']
    except:
        pass

df = pd.DataFrame(importerKinetics)

rateCoefficients = df.applymap(RateCoefficients)

rateCoefficients.to_pickle("~/Code/OOHabstraction/comparisonTST/reference_files/rateCoefficients.plk")

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

with open("./ComparerTST/kinetics.pkl", "r") as f:
    importerKinetics = pickle.load(f)

def evalArrhenius(autoTSTExpression):
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
    rate = np.nan
    try:
        rate = np.log(arrhenius.getRateCoefficient(T=1000, P=1e5))
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

arrhenius = pd.DataFrame(importerKinetics)
df = arrhenius
rateCoefficients = df.applymap(RateCoefficients)

rateCoefficients.to_pickle("rateCoefficients.plk")

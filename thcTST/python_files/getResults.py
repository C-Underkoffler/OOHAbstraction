"""
This is a file designed to read through the biofuelsTST
log files and determine if kinetics were calculated.

If so, it creates a dictionary of the successful reactions.
"""


import os
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


rmg_path = os.getenv('RMGpy')
if rmg_path and rmg_path not in sys.path:
    sys.path.insert(1,rmg_path)

import rmgpy.kinetics

def evalArrhenius(autoTSTExpression):
    if autoTSTExpression is np.nan:
        return autoTSTExpression
    try:
        my_string = str(autoTSTExpression).strip("'")
        #print my_string
        result = eval(my_string, {}, {'Arrhenius': rmgpy.kinetics.Arrhenius,
                                     'MultiArrhenius': rmgpy.kinetics.MultiArrhenius,
                                     'PDepArrhenius': rmgpy.kinetics.PDepArrhenius,})
    except:
        result = autoTSTExpression
        raise
    return result


directory = "./results"

filelist = []
for filename in os.listdir(directory):
    if filename.startswith("AutoTST-biofuels") and filename.endswith("combined.log"):
        filelist.append(str(directory) + '/' + str(filename))
#print filelist

kinDict = {}
for filename in filelist:
    f = open(filename, 'r')
    lineList = f.readlines()
    for fileline in lineList:
        if fileline.startswith("biofuelsTST.py:105"):
            splt = fileline.split(' ')
            reaction = splt[-1]
            reaction = reaction[:-1]
            #print reaction
            #print

        if fileline.startswith('Yay,'):
            lastline = lineList[len(lineList)-1]
            splt = lastline.split('kinetics ')
            kinetics = splt[-1]
            kinetics = evalArrhenius(kinetics[:-1])
            #print type(kinetics)
            #print

            #print kinetics
            kinDict[reaction] = kinetics

df = pd.DataFrame(kinDict.items(), columns=['Reaction', 'Kinetics'])

ln_A = []
E_a = []
kin = {}
inverseTemps = np.linspace(1000./800., 1000/2500., 15)
Temps = 1000./inverseTemps
comparisonPressure = 1e5

for i in range(len(df['Kinetics'])):
    kinetics = df['Kinetics'].iloc[i]
    reaction = df['Reaction'].iloc[i]

    kinList = []
    for Temp in Temps:
        kinList.append(kinetics.getRateCoefficient(T=Temp, P=comparisonPressure))
    kin[reaction] = kinList
    A = float(str(kinetics.A).split(' ')[0])
    #print A
    ln_A.append(np.log10(A))

    Ea = float(str(kinetics.Ea).split(' ')[0])
    #print Ea
    E_a.append(Ea)

ln_A = np.array(ln_A)
E_a = np.array(E_a)

print ln_A, E_a
print kin

for i in range(len(kin.keys())):
    rates = kin.values()[i]
    reaction = kin.keys()[i]
    plt.plot(inverseTemps, reaction)




#df.to_csv("biofuelKinetics.csv")

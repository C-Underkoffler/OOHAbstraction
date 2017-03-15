
# coding: utf-8

# This reads in the `output.xls` file from the modelComparer script, and creates various plots comparing H abstraction by OOH radical rates from the AutoTST library with all the other libraries.

# In[1]:

import matplotlib
matplotlib.use('Agg')
get_ipython().magic(u'matplotlib inline')
from matplotlib import pyplot as plt
import pandas as pd

import numpy as np
import os, sys
rmg_path = os.getenv('RMGpy')
if rmg_path and rmg_path not in sys.path:
    sys.path.insert(1,rmg_path)

import rmgpy.kinetics


# In[2]:

# workbookPath = '/gss_gpfs_scratch/westgroup/Importer/RMG-models/modelComparer/output.xls'
kineticsSheet = pd.read_excel('output.xls', sheetname='k-1000K-100bar', header=4).iloc[:,1:-5]
expressionSheet = pd.read_excel('output.xls', sheetname='k-expressions', header=4).iloc[:,1:]


# ## Making the box plot

# In[3]:

rxnList = kineticsSheet['AutoTST-OOHabstraction'].dropna().index.values
kinSheet = kineticsSheet.ix[rxnList].sort_values(by='AutoTST-OOHabstraction').set_index('Reaction')
kSheet = kinSheet.iloc[:,:-2] # remove the last column, which is AutoTST-OOHabstraction
kSheet


# In[4]:

get_ipython().magic(u'cd plotOutputResults')


# In[5]:

boxPlot = kSheet.transpose().plot.box(figsize=(12,8), grid=True, rot=90)
boxPlot.plot(range(1,kinSheet.transpose().shape[1]+1),kinSheet.transpose().loc['AutoTST-OOHabstraction'].values, marker='o', color='k', linestyle='')
boxPlot.set_ylabel('$log_{10}(k)$', fontsize=20)
boxPlot.set_xlabel('Reaction', fontsize=20)
fig = boxPlot.get_figure()
fig.tight_layout()
#fig.savefig("boxPlot.pdf")


# ## Making the parity plot

# In[6]:

for j in kinSheet.index:
    mean = kSheet.loc[j].mean(axis=0) + 6 # ksheet excludes AutoTST
    autoTST = kinSheet['AutoTST-OOHabstraction'].loc[j] + 6
    x_list = []
    y_list = []
    for i in list(kinSheet):
        if i != "AutoTST-OOHabstraction" and not pd.isnull(kinSheet[i].loc[j]):
            x_list.append(kinSheet[i].loc[j] + 6)
            y_list.append(autoTST)

    plt.plot(range(-2, 20), range(-2, 20), '-g', zorder=-1) # Parity Line
    plt.plot(range(-3, 19), range(-2, 20), ':g', zorder=-1) # 1 order of magnitude
    plt.plot(range(-1, 21), range(-2, 20), ':g', zorder=-1) # 1 order of magnitude
    
    plt.plot(x_list, y_list, '.-b', alpha=0.2) # Line and dots for the range of literature values
    #plt.plot(x_list, y_list, '|b') # Tick marks for each point
    plt.plot(mean, autoTST, '|r') # Red bars for the average

    plt.axis('equal')
    plt.ylim([6,11])
    plt.xlim([6,11])
    plt.title("$k(T=1000 K, P=100 bar) \ [cm^3 / (mole \cdot s)]$")
    plt.xlabel('$log_{10}k$ from literature', fontsize=10)
    plt.ylabel('$log_{10}k$ by AutoTST', fontsize=10)
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

plt.savefig('parityPlot.pdf')


# ## Making the Arrhenius plots for each reaction

# In[ ]:

rxnList = expressionSheet['AutoTST-OOHabstraction'].dropna(axis=0).index.values
expSheet = expressionSheet.ix[rxnList].sort(columns='AutoTST-OOHabstraction').set_index('Reaction')
expSheet


# In[ ]:

get_ipython().magic(u'cd arrheniusPlots')


# In[ ]:

def evalArrhenius(autoTSTExpression):
    try:
        my_string = str(autoTSTExpression)[1:]
        result = eval(my_string, {}, {'Arrhenius': rmgpy.kinetics.Arrhenius})
    except:
        result = autoTSTExpression
    return result

Temps = np.array(range(200,2600,100))
inverseTemps = 1000./Temps

for j in expSheet.index:
    for i in list(expSheet):
        logk = []
        logkAutoTST = []
        expSheet[i].loc[j] = evalArrhenius(expSheet[i].loc[j])
        #print type(expSheet[i].loc[j])
        
        if i == 'AutoTST-OOHabstraction':
            for Temp in Temps:
                k = expSheet[i].loc[j].getRateCoefficient(Temp,1000)
                logkAutoTST.append(np.log10(k) + 6)
                
            plt.plot(inverseTemps, logkAutoTST, '-r', linewidth=2)
        elif type(expSheet[i].loc[j]) == rmgpy.kinetics.arrhenius.Arrhenius:
            #expSheet[i].loc[j]
            for Temp in Temps:
                k = expSheet[i].loc[j].getRateCoefficient(Temp,1000)
                logk.append(np.log10(k) + 6)
            plt.plot(inverseTemps, logk, ':k', linewidth=2)
    plt.xlabel("$1000/T [K^{-1}]$", fontsize=16)
    plt.ylabel("$log_{10}(k) [cm^3 / (mole \cdot s)]$", fontsize=16)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    #plt.title(j)
    plt.xlim([0.25,1.5])
    saveString = str(j) + '.pdf'
    plt.savefig(saveString)
    plt.show()  


# # My attempt to generate parity plots for $A$ and $E_a$

# In[ ]:

get_ipython().magic(u'cd ..')


# In[ ]:

for j in expSheet.index:
    #mean = kinSheet.loc[j].mean(axis=0) + 6
    
    autoTST = np.log10(float(str(expSheet['AutoTST-OOHabstraction'].loc[j].A).split(' ')[0])) + 6
    #print expSheet['AutoTST-OOHabstraction'].loc[j].A
    #print 
    x_list = []
    y_list = []
    for i in list(expSheet):
        if i != "AutoTST-OOHabstraction" and pd.isnull(kinSheet[i].loc[j]) == False:
            try:
                #print float(str(expSheet[i].loc[j].A).split(' ')[0])
                x_list.append(np.log10(float(str(expSheet[i].loc[j].A).split(' ')[0])) + 6)
                y_list.append(autoTST)
            except:
                print expSheet[i].loc[j]
            
    mean = np.mean(x_list)
    plt.plot(x_list, y_list, '-b') # Line for the range for each AutoTST point
    plt.plot(x_list, y_list, '|b') # Tick marks for each point
    plt.plot(mean, autoTST, '.k') # Dots for each average data point
    plt.plot(range(-5, 22), range(-5, 22), '-g')# Parity Line
    plt.plot(range(-6, 21), range(-5, 22), ':g') # 1 order of magnitude
    plt.plot(range(-4, 23), range(-5, 22), ':g')# 1 order of magnitude
    plt.ylim([-5,20])
    plt.xlim([-5,20])
    plt.xlabel('$log_{10}A [cm^3 / (mole \cdot s)]$ by Imported Kinetics', fontsize=10)
    plt.ylabel('$log_{10}A [cm^3 / (mole \cdot s)]$ by AutoTST', fontsize=10)
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

plt.savefig('parityPlotA.pdf')


# In[ ]:

for j in expSheet.index:
    #mean = kinSheet.loc[j].mean(axis=0) + 6
    
    autoTST = np.log10(float(str(expSheet['AutoTST-OOHabstraction'].loc[j].Ea).split(' ')[0]) / 0.004184)
    #print expSheet['AutoTST-OOHabstraction'].loc[j].Ea
    #print 
    x_list = []
    y_list = []
    for i in list(expSheet):
        if i != "AutoTST-OOHabstraction" and pd.isnull(kinSheet[i].loc[j]) == False:
            try:
                #print expSheet[i].loc[j].Ea
                x_list.append(np.log10(float(str(expSheet[i].loc[j].Ea).split(' ')[0])))
                y_list.append(autoTST)
            except:
                print expSheet[i].loc[j]
            
    mean = np.mean(x_list)
    plt.plot(x_list, y_list, '-b') # Line for the range for each AutoTST point
    plt.plot(x_list, y_list, '|b') # Tick marks for each point
    plt.plot(mean, autoTST, '.k') # Dots for each average data point
    plt.plot(range(-5, 22), range(-5, 22), '-g')# Parity Line
    plt.plot(range(-6, 21), range(-5, 22), ':g') # 1 order of magnitude
    plt.plot(range(-4, 23), range(-5, 22), ':g')# 1 order of magnitude
    plt.ylim([2.5,5])
    plt.xlim([2.5,5])
    plt.xlabel('$E_a [cal / mol]$ by Imported Kinetics', fontsize=10)
    plt.ylabel('$E_a [cal / mol]$ by AutoTST', fontsize=10)
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

plt.savefig('parityPlotEa.pdf')


# In[ ]:

kinSheet.



# coding: utf-8

# This reads in the `output.xls` file from the modelComparer script, and creates various plots comparing H abstraction by OOH radical rates from the AutoTST library with all the other libraries.

# In[1]:

import matplotlib
#matplotlib.use('Agg')
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


# In[10]:

kineticsSheet.columns = [n.split('gss_gpfs_scratch/westgroup/Importer/RMG-models/')[-1] for n in kineticsSheet.columns]
expressionSheet.columns = [n.split('gss_gpfs_scratch/westgroup/Importer/RMG-models/')[-1] for n in expressionSheet.columns]


# ## Making the box plot

# In[11]:

rxnList = kineticsSheet['AutoTST-OOHabstraction'].dropna().index.values
kinSheet = kineticsSheet.ix[rxnList].sort_values(by='AutoTST-OOHabstraction').set_index('Reaction')
kSheet = kinSheet.iloc[:,:-2] # remove the last column, which is AutoTST-OOHabstraction
kSheet


# In[12]:

get_ipython().magic(u'cd plotOutputResults')


# In[15]:

boxPlot = kSheet.transpose().plot.box(figsize=(24,8), grid=True, rot=90)
boxPlot.plot(range(1,kinSheet.transpose().shape[1]+1),kinSheet.transpose().loc['AutoTST-OOHabstraction'].values, marker='o', color='k', linestyle='')
boxPlot.set_ylabel('$log_{10}(k)$', fontsize=20)
boxPlot.set_xlabel('Reaction', fontsize=20)
fig = boxPlot.get_figure()
fig.tight_layout()
#fig.savefig("boxPlot.pdf")


# ## Making the parity plot

# In[16]:

plt.plot(range(-2, 20), range(-2, 20), '-g', zorder=-1) # Parity Line
plt.plot(range(-3, 19), range(-2, 20), ':g', zorder=-1) # 1 order of magnitude
plt.plot(range(-1, 21), range(-2, 20), ':g', zorder=-1) # 1 order of magnitude

for j in kinSheet.index:
    mean = kSheet.loc[j].mean(axis=0) + 6 # ksheet excludes AutoTST
    autoTST = kinSheet['AutoTST-OOHabstraction'].loc[j] + 6
    x_list = []
    y_list = []
    for i in list(kinSheet):
        if i != "AutoTST-OOHabstraction" and not pd.isnull(kinSheet[i].loc[j]):
            x_list.append(kinSheet[i].loc[j] + 6)
            y_list.append(autoTST)

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

# In[7]:

rxnList = expressionSheet['AutoTST-OOHabstraction'].dropna(axis=0).index.values
expSheet = expressionSheet.ix[rxnList].sort_values(by='AutoTST-OOHabstraction').set_index('Reaction')
expSheet


# In[8]:

get_ipython().magic(u'cd arrheniusPlots')


# In[9]:

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

# Temps = np.array(range(800,2500,100))
# inverseTemps = 1000./Temps

inverseTemps = np.linspace(1000./800., 1000./2500., 15)
Temps = 1000./inverseTemps

comparisonPressure = 1e5 # Pa

# make a copy and leave the original so we can try this cell several times
kineticsSheet = expSheet.copy() 
for j in expSheet.index:
    fig, ax = plt.subplots()
    for i in list(expSheet):
        logk = []
        logkAutoTST = []
        kineticsSheet[i].loc[j] = evalArrhenius(expSheet[i].loc[j])
        #print type(kineticsSheet[i].loc[j])
        
        if i == 'AutoTST-OOHabstraction':
            for Temp in Temps:
                k = kineticsSheet[i].loc[j].getRateCoefficient(T=Temp,P=comparisonPressure)
                logkAutoTST.append(np.log10(k) + 6)

            plt.plot(inverseTemps, logkAutoTST, '-r', linewidth=2)
        elif type(kineticsSheet[i].loc[j]) == rmgpy.kinetics.arrhenius.Arrhenius:
            #kineticsSheet[i].loc[j]
            for Temp in Temps:
                k = kineticsSheet[i].loc[j].getRateCoefficient(T=Temp,P=comparisonPressure)
                logk.append(np.log10(k) + 6)
            plt.plot(inverseTemps, logk, ':k', linewidth=2, alpha=0.4)
    plt.xlabel("$1/T [K^{-1}]$", fontsize=16)
    plt.ylabel("$log_{10}(k) [cm^3 / (mole \cdot s)]$", fontsize=16)
    
    Tticks = [800, 1000, 1500, 2500]
    ax.set_xticks([1000./T for T in Tticks])
    ax.set_xticklabels(['1/{:.0f}'.format(T) for T in Tticks])
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    #plt.title(j)
    plt.xlim([0.39,1.26])
    
    #plt.ylim([6,13])
    # the following will EXPAND the limits to at least (6,13) but not shrink them
    plt.ylim(min(ax.get_ylim()[0], 6), max(ax.get_ylim()[1], 13))
    saveString = str(j) + '.pdf'
    plt.savefig(saveString)
    print str(j)
    plt.show() 
    print


# In[ ]:




# # My attempt to generate parity plots for $A$ and $E_a$

# In[10]:

get_ipython().magic(u'cd ..')


# In[11]:

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



# coding: utf-8

# # Progress Metering for OOH abstraction

# This is a notebook designed to go through each output file in rwest-autotst-1 and determine the progress of each run.

# In[1]:

import os, sys
rmg_path = os.getenv('RMGpy')
if rmg_path and rmg_path not in sys.path:
    sys.path.insert(1,rmg_path)
import os
import re
from collections import defaultdict, OrderedDict
import pandas as pd
from rmgpy.molecule import Molecule
from rmgpy.reaction import Reaction
import IPython
from IPython.display import display, Markdown
def mprint(s): display(Markdown(s))


# In[2]:

directory = '/gss_gpfs_scratch/harms.n/comparerTST'
results = defaultdict(OrderedDict)
comparerFiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
k = 0
for fil in comparerFiles:
    if ".log" in fil:
        k += 1
results = defaultdict(OrderedDict)
not_ooh_abstraction = []
for i in range(1,k+1):
    r = results[i]
    filename = 'AutoTST-comparer.{0:d}.combined.log'.format(i)
    filepath = os.path.join(directory,filename)
    if os.path.exists(filepath):
        r['1 log file exists'] = 1
    else:
        continue
    with open(filepath) as f:
        lines = f.readlines()
    for j,l in enumerate(lines):
        m = re.match('comparerTST.py:141 performCalcs INFO chemkinRxn: (.*)', l)
        if m:
            rxn = m.group(1)
            if not ('SMILES="[O]O"'  in rxn and 'SMILES="OO"'  in rxn):
                not_ooh_abstraction.append(i)
                break
            r['0 reaction'] = eval(rxn)
            
        
        if 'We have generated a H_Abstraction reaction that matches, and used it to label the atoms' in l:
            r['2 matched H-abstraction'] = 1
          
        
        if 'Reading existing kinetics file' in l:
            r['XX using existing kinetics data file'] = 1 # Reading in existing .kinetics file
            
        
           
        
        if 'Generating a TS geometry via the direct guess method' in l:
            r['3A started making TS geometry'] = 1
        if "Reading existing ts file" in l:
            r['3B using existing ts data file'] = 1 # If reading in existing .ts file, this bypasses 4, 5 and 6
        if 'optimizeTS INFO Output file' and 'exists and looks complete. Trying that.' in l:
            r['3C Previous TS optimization complete'] = 1 #If reading in existing .log, this then checks if there is an existing IRC clac
            
            
            
        if 'Running loose optimization of TS with frozen center' in l:
            r['4A TS opt w frozen center'] = 1    
        if 'Optimization of TS reaction center distances' in l:
            r['4B TS opt of rxn center'] = 1  
        if 'Optimizing TS attempt' in l:
            r['4C TS optimization started'] = 1
        
        
        if 'verifyOutputFile INFO Verifying output file' in l:
            r['5A New TS optimization complete'] = 1
        
        
            
        if 'Creating IRC file' in l:
            r['6A IRC file created'] = 1
        if "Verifying the IRC output file" in l:
            r['6B New IRC calc complete'] = 1
        if "saveTSData INFO Saving TS result file" in l:
            r['6C New IRC calc successful'] = 1
            
            
            
        if 'Symmetry input file written to' in l:
            r['7A starting Symmetry calculation'] = 1
        if 'Point group:' in l:
            r['7B Symmetry calc successful'] = 1
         
        
        if 'CanTherm execution initiated' in l:
            r['8 CanTherm started'] = 1
        if 'One or both of the barrier heights of' in l:
            r['8A CanTherm barrier height problem'] = -1
         
        
        if 'Yay, reaction kinetics calculated!!!' in l:
            r['ZZ overall success'] = 1
            
        if "gaussian.py:880 verifyIRCOutputFile ERROR Not all of the required keywords for success were found in the IRC output file!" in l:
            r['ZZZ IRC success keywords not found'] = 1

    
    if 'XX using existing TS data file' and 'ZZ overall success' in r.keys():
        r['YY successful prior calculation'] = 1
        
    if '5A New TS optimization complete' and '6A IRC file created' in r.keys():
        r['5B TS successfully optimized'] = 1
    
    if '6B New IRC calc complete' in r.keys() and "6A IRC file created" not in r.keys():
        r['6D IRC calc from previous calculation'] = 1
        #print "deleting 6B"
        del(r['6B New IRC calc complete'])
        
    if '5A New TS optimization complete' and '5C Previous TS optimization complete' in r.keys():
        del(r['5A New TS optimization complete'])
        
        
        
          
        

for i in not_ooh_abstraction:
    del(results[i])
df = pd.DataFrame(results)
df


# In[3]:

df.count(axis=1)


# finished_but_failed_irc = (df.T["6B New IRC calc complete"]==1) & (df.T["6C New IRC calc successful"]!=1)
# df.T[finished_but_failed_irc]['0 reaction']
# mprint("# Finished IRC but failed it ({})".format(sum(finished_but_failed_irc)))
# for r in df.T[finished_but_failed_irc]['0 reaction']:
#     display(r)
#     print df.T[finished_but_failed_irc]

# analysis = defaultdict(OrderedDict)
# 
# for i in range(df.shape[1]):
#     i= i+1
#     r = {}
#     testRxn = str(df.loc['0 reaction'][i])
#     success = df.loc['B overall success'][i]
#     spec = testRxn.split('<=>')
#     for d in spec:
#         if """<Molecule "[O]O">""" in d:
#             r1, r2 = d.split('+')
#             if """<Molecule "[O]O">""" in r1:
#                 important = str(r2)
#             else:
#                 important = str(r1)
#     smiles = important.split("\"")[1]
#     
#     mol = Molecule(SMILES=smiles)
#     r['Molar Mass'] = mol.getMolecularWeight()
#     r['Radical Count'] = mol.getRadicalCount()
#     r['Is Linear'] = mol.isLinear()
#     r['Is Aromatic'] = mol.isAromatic()
#     r['Is Rotor'] = mol.countInternalRotors()
#     
#     mol.getBonds
#     if success == 1:
#         r['Has Kinetics'] = True
#     else:
#         r['Has Kinetics'] = False
#     analysis[smiles] = r
# 
# 
# 
#     

# ana = pd.DataFrame(analysis).transpose()
# ana.sort('Has Kinetics')
# 
# ana[ana['Has Kinetics']]

# In[4]:




# directory = "/Users/nathan/Code/scratch_test/bioTST/"
# bioFiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
# k = 0
# for fil in bioFiles:
#     if ".log" in fil:
#         k += 1
# results = defaultdict(OrderedDict)
# for i in range(k):
#     i = i + 1
#     r = results[i]
#     filename = 'AutoTST-biofuels.{0:d}.combined.log'.format(i)
#     filepath = os.path.join(directory,filename)
#     if os.path.exists(filepath):
#         r['1 log file exists'] = 1
#     else:
#         continue
#     with open(filepath) as f:
#         lines = f.readlines()
#     for j,l in enumerate(lines):
#         m = re.match('autoTST-OOH.py:62 <module> INFO (.*)', l)
#         if m:
#             r['0 reaction'] = m.group(1)
#         if 'We have generated a H_Abstraction reaction that matches, and used it to label the atoms' in l:
#             r['2 matched H-abstraction'] = 1
#         if 'Generating a TS geometry via the direct guess method' in l:
#             r['3 started making TS geometry'] = 1
#         if 'Reading existing ts file' in l:
#             r['4 using existing TS data file'] = 1
#         if 'Symmetry input file written to' in l:
#             r['5 starting Symmetry calculation'] = 1
#         if 'Point group:' in l:
#             r['6 Symmetry calc successful'] = 1
#         if 'line 295, in saveCoordinatesFromRDMol' in l:
#             r['7 saveCoordinatesFromRDMol bug'] = -1
#             print ''.join(lines[j-30:])
#         if 'CanTherm execution initiated' in l:
#             r['9 CanTherm started'] = 1
#         if 'One or both of the barrier heights of' in l:
#             r['9a CanTherm barrier height problem'] = -1
#         if "Reading existing kinetics file" in l:
#             r['A using prior calculation result'] = 1
#         if 'Yay, reaction kinetics calculated!!!' in l:
#             r['B overall success'] = 1
# 

# df = pd.DataFrame(results)
# df

# df.sum(axis=1)

# df.count(axis=1)

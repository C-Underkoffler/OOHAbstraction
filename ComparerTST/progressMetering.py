
# coding: utf-8

# # Progress Metering for OOH abstraction

# This is a notebook designed to go through each output file in comparerTST and determine the progress of each run.

# In[1]:

import os
import re
from collections import defaultdict, OrderedDict
import pandas as pd


# In[2]:

directory = '/gss_gpfs_scratch/harms.n/comparerTST'
results = defaultdict(OrderedDict)
for i in range(1,408):
    r = results[i]
    filename = 'AutoTST.{0:d}.combined.log'.format(i)
    filepath = os.path.join(directory,filename)
    if os.path.exists(filepath):
        r['1 log file exists'] = 1
    else:
        continue
    with open(filepath) as f:
        lines = f.readlines()
    for j,l in enumerate(lines):
        m = re.match('autoTST-OOH.py:62 <module> INFO (.*)', l)
        if m:
            r['0 reaction'] = m.group(1)
        if 'We have generated a H_Abstraction reaction that matches, and used it to label the atoms' in l:
            r['2 matched H-abstraction'] = 1
        if 'Generating a TS geometry via the direct guess method' in l:
            r['3 started making TS geometry'] = 1
        if 'Reading existing ts file' in l:
            r['4 using existing TS data file'] = 1
        if 'Symmetry input file written to' in l:
            r['5 starting Symmetry calculation'] = 1
        if 'Point group:' in l:
            r['6 Symmetry calc successful'] = 1
        if 'line 295, in saveCoordinatesFromRDMol' in l:
            r['7 saveCoordinatesFromRDMol bug'] = -1
            print ''.join(lines[j-30:])
        if 'CanTherm execution initiated' in l:
            r['9 CanTherm started'] = 1
        if 'One or both of the barrier heights of' in l:
            r['9a CanTherm barrier height problem'] = -1
        if "Reading existing kinetics file" in l:
            r['A using prior calculation result'] = 1
        if 'Yay, reaction kinetics calculated!!!' in l:
            r['B overall success'] = 1


# In[3]:

df = pd.DataFrame(results)
df


# In[4]:

df.sum(axis=1)


# In[5]:

df.count(axis=1)


# In[6]:




# In[6]:




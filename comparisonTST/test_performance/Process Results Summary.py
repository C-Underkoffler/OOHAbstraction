
# coding: utf-8

# The `results-summary.txt` contains, for each alternative model, the name and the overal badness from PyTEK

# In[1]:

import pandas as pd
get_ipython().magic(u'matplotlib inline')
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:

data = pd.read_csv('results-summary.txt', delimiter='\s+',names=['model','error'])
data


# In[3]:

sns.set_style('ticks')


# In[4]:


data.error.hist(bins=50, log=True, figsize=(4,4), normed=True)
plt.xlabel("Error metric $E$")
plt.ylabel("Number of models")


# In[5]:

e = data['error']
plt.figure(figsize=(4,4))
plt.hist(e, bins=range(int(min(e)),int(max(e))+1), log=True, normed=False ) 
plt.xlabel("Error metric $E$")
plt.ylabel("Number of models")


# In[6]:

e = data['error']
plt.figure(figsize=(3,3))
plt.hist(e, bins=100, log=True, normed=False) 
plt.xlabel("Error metric $E$")
plt.ylabel("Number of models")
plt.vlines(e[0],0,100, color='red', linewidth=1)
min(e), max(e)
plt.tight_layout()
plt.savefig('histogram-log.pdf')


# In[7]:

e = data['error']
plt.figure(figsize=(3,3))
plt.hist(e, bins=2000, log=False, normed=False) 
plt.xlim(107.5,108)
plt.xlabel("Error metric $E$")
plt.ylabel("Number of models")
plt.vlines(e[0],0,100, color='red', linewidth=1)
plt.tight_layout()
plt.savefig('histogram-linear.pdf')


# In[8]:

data['deltaE'] = data['error'] - e[0]
data


# In[28]:

data['absDeltaE'] = data['deltaE'].map(abs)
sorted_abs  = data.sort_values(by='absDeltaE', ascending=False)
sorted_abs.head(20)


# In[50]:

line = u"""
% {subs:30s} 
{kind:17s} & {number:5s} & {alternate} & {error:.3f} & {deltaE:+.3f} \\\\"""
for i,row in sorted_abs.iloc[:20].iterrows():
    subs = row.model
    deltaE = row.deltaE
    error = row.error
    n = row.model.split('.')[1]
    sub = subs.replace('master.thermo','Thermochemistry').replace('master','Kinetics')
    kind, number, alternate  = sub.split('.')
    print line.format(**locals())
    


# In[9]:

sorted = data.sort_values(by='error')
sorted


# In[10]:

data



# In[11]:

kinetics = sorted[sorted.model.str.contains('thermo')==False]


# In[12]:

kinetics.head(13), kinetics.tail(10)


# In[13]:

line = u"""
{n} & Orig. & \\num{{ 1e1 }} & 0.0 &  &
{{\\small  }}
\\\\ %% Substitution: {subs}
  & Repl. & \\num{{ 1e1 }} &  0.0 &  & 
{{\\small  }}&
{deltaE:.3f}
  \\\\
\\midrule
"""
for i,row in kinetics.iloc[:12:+1].iterrows():
    subs = row.model
    deltaE = row.deltaE
    n = row.model.split('.')[1]
    print line.format(**locals())
    
    
for i,row in kinetics.iloc[:-8:-1].iterrows():
    subs = row.model
    deltaE = row.deltaE
    n = row.model.split('.')[1]
    print line.format(**locals())
    
    


# In[14]:

thermo = sorted[sorted.model.str.contains('thermo')==True]
thermo


# In[15]:

line = u"""
%% Substitution: {subs}
{n} & 
\ce{{  }}
&
ASSEENIN
& 
{deltaE:+.3f}
\\\\
"""
for i,row in thermo.iloc[:2:+1].iterrows():
    subs = row.model
    deltaE = row.deltaE
    n = row.model.split('.')[2]
    print line.format(**locals())
    
    
for i,row in thermo.iloc[:-5:-1].iterrows():
    subs = row.model
    deltaE = row.deltaE
    n = row.model.split('.')[2]
    print line.format(**locals())


# In[ ]:




# In[16]:

list(kinetics.iloc[:12:+1].model)


# In[17]:

list(kinetics.iloc[:-8:-1].model)


# In[18]:

kinetics.iloc[:-8:-1]


# In[19]:


thermo = sorted[sorted.model.str.contains('thermo')==True]
thermo


# In[20]:

e = data['error']
plt.figure(figsize=(6,5))
# range(int(min(e)),int(max(e))+1)
n, bins, patches = plt.hist(e, bins=1000, log=False, normed=False ) 
plt.xlabel("Error metric $E$")
plt.ylabel("Number of models")
plt.ylim(-5,)

# this is an inset axes over the main axes
a = plt.axes([.6, .6, .25, .25], facecolor='w')
n, bins, patches = plt.hist(e, bins=1000, log=False, normed=False ) 
plt.vlines(e[0],0,50, color='red', linewidth=1)
plt.ylim(-2,50)
plt.xlim(107,109)
#plt.xticks([])
#plt.yticks([])


plt.tight_layout()
plt.savefig("big-histogram.pdf")
#plt.vlines(e[0],0,25, color='red', linewidth=1)


# In[21]:

plt.figure(figsize=(2,2))
# range(int(min(e)),int(max(e))+1)
plt.bar(a[1][1:],a[0])
plt.ylim(-5,50)
plt.xlim(107,109)
a[0]


# In[ ]:

e = data['error']
plt.figure(figsize=(10,10))
# range(int(min(e)),int(max(e))+1)
a = plt.hist(e, bins=2000, log=False, normed=False) 

plt.xlim(107.7,107.8)


# In[ ]:

i = np.argmax(a[0])
a[1][i], a[1][i+1]
e.mi
np.arange()


# In[ ]:

min(e), max(e)


# In[ ]:

bins = np.arange(98.35,122.52, 0.01)


# In[ ]:

e = data['error']
plt.figure(figsize=(20,10))
# range(int(min(e)),int(max(e))+1)
a = plt.hist(e, bins=bins, log=True, normed=False ) 
plt.xlabel("Error metric $E$")
plt.ylabel("Probability density")


# In[ ]:

delta = (e-e[0])
delta[delta!=0].abs().min()


# In[ ]:

delta[delta==0] = 1e-7


# In[ ]:

delta[delta>0].map(np.log10).hist(bins=range(-7,2))


# In[ ]:

plt.figure(figsize=(4,4))
plt.hist(delta[delta>0].map(np.log10), bins=range(-7,2))
plt.xlabel('$\log_{10}(\Delta E)$ for $\Delta E > 0$')
plt.ylabel('Number of models')
plt.tight_layout()
plt.savefig("histogram-logx.pdf")


# In[ ]:

plt.figure(figsize=(4,4))
plt.hist(delta.abs().map(np.log10), bins=range(-7,2))
plt.xlabel('$\log_{10}( \| \Delta E \|)$')
plt.ylabel('Number of models')
plt.tight_layout()
plt.savefig("histogram-logAbsDeltaE.pdf")


# In[ ]:

(delta[delta<0]*-1).map(np.log10).hist(bins=range(-7,2))


# In[ ]:

delta.hist(bins=100, log=True)


# In[ ]:

e = data['error']
plt.figure(figsize=(7,6))
# range(int(min(e)),int(max(e))+1)
n, bins, patches = plt.hist(e, bins=1000, log=False, normed=False ) 
plt.xlabel("Error metric $E$")
plt.ylabel("Number of models")
plt.ylim(-5,)

# this is an inset axes over the main axes
a = plt.axes([.6, .6, .3, .3], facecolor='w')
plt.hist(e, bins=1000, log=True, normed=False ) 
plt.vlines(e[0],0,50, color='red', linewidth=1)
plt.xlim(107,109)
plt.xlabel('$E$')
plt.ylabel('Number of models')

a = plt.axes([.6, .2, .3, .3], facecolor='w')
plt.hist(delta.abs().map(np.log10), bins=range(-7,2))
plt.xlabel('$\log_{10}( \| \Delta E \|)$')
plt.ylabel('Number of models')
#
#plt.ylim(-2,50)
#plt.xlim(107,109)
#plt.xticks([])
#plt.yticks([])

plt.tight_layout()
plt.savefig("big-histogram.pdf")
#plt.vlines(e[0],0,25, color='red', linewidth=1)


# In[ ]:

# this is an inset axes over the main axes
plt.figure(figsize=(3,3))
plt.hist(e, bins=1000, log=True, normed=False )
plt.xlim(107,109)
plt.xlabel('$E$')
plt.ylabel('Number of models')


# In[ ]:

x=0.01
print "percentage of substitutions changing the error by less than",x
100.* sum(delta<x) / (len(delta)-1)


# In[ ]:

e[0]


# In[ ]:




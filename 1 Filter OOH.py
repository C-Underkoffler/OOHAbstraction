
# coding: utf-8

# In[2]:

import os


# In[3]:

root_dir = '/scratch/bhoorasingh.p/QMfiles/Reactions/H_Abstraction/'
all_reactions = os.listdir(root_dir)
len(all_reactions)


# In[4]:

ooh_forward = []
ooh_reverse = []
for reaction in all_reactions:
    reactants, products = reaction.split('_')
    reactants = reactants.split('+')
    products = products.split('+')
    if '[O]O' in reactants and 'OO' in products:
        ooh_forward.append(reaction)
    if 'OO' in reactants and '[O]O' in products:
        ooh_reverse.append(reaction)
print("Forward", len(ooh_forward))
print("Reverse", len(ooh_reverse))
ooh_forward


# In[22]:

to_try = []
for reaction in ooh_forward:
    try:
        path = os.path.join(root_dir, reaction)
        assert 'm062x' in os.listdir(path), "Doesn't have m062x files"
        path = os.path.join(root_dir, reaction, 'm062x')
        files = os.listdir(path)
        assert 'output.py' in files, "Doesn't have output.py file"
        to_try.append(reaction)
        
    except Exception as err:
        print "# ⚠️", reaction, "Gave error", str(err)
len(to_try)


# In[21]:

for reaction in to_try:
    try:
        path = os.path.join(root_dir, reaction, 'm062x','output.py')
        with open(path) as f:
            lines = f.readlines()
        start = lines.index('kinetics(\n')
        print
        print "#  ",reaction
        print ''.join(lines[start:])
    except Exception as err:
        print "⚠️", reaction, "Gave error", str(err)


# In[ ]:




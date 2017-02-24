
# coding: utf-8

# In[1]:

import os


# In[2]:

root_dir = '/scratch/bhoorasingh.p/QMfiles/Reactions/H_Abstraction/'
all_reactions = os.listdir(root_dir)
len(all_reactions)


# In[3]:

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


# In[4]:

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


# In[5]:

get_ipython().run_cell_magic(u'capture', u'cap --no-stderr', u'for reaction in to_try:\n    try:\n        path = os.path.join(root_dir, reaction, \'m062x\',\'output.py\')\n        with open(path) as f:\n            lines = f.readlines()\n        start = lines.index(\'kinetics(\\n\')\n        print\n        print "#  ",reaction\n        print \'\'.join(lines[start:])\n    except Exception as err:\n        print "# \u26a0\ufe0f", reaction, "Gave error", str(err)')


# In[6]:

with open('filtered_kinetics.py', 'w') as f:
    f.write('# - *- coding: utf- 8 - *-/n')
    f.write(cap.stdout)
print cap.stdout


# In[7]:

root_dir = '/gss_gpfs_scratch/westgroup/QMscratch/'
new_reactions = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir,f)) ]
print new_reactions
len(new_reactions)


# In[8]:

to_try = []
for reaction in new_reactions:
    try:
        path = os.path.join(root_dir, reaction)
        files = os.listdir(path)
        assert 'output.py' in files, "Doesn't have output.py file"
        to_try.append(reaction)
    except Exception as err:
        print "# ⚠️", reaction, "Gave error", str(err)
len(to_try)


# In[9]:

get_ipython().run_cell_magic(u'capture', u'cap --no-stderr', u'success = fail = 0\nfor reaction in to_try:\n    try:\n        path = os.path.join(root_dir, reaction,\'output.py\')\n        with open(path) as f:\n            lines = f.readlines()\n        start = lines.index(\'kinetics(\\n\')\n        print\n        print "#  ",reaction\n        print \'\'.join(lines[start:])\n        success += 1\n    except Exception as err:\n        print "# \u26a0\ufe0f", reaction, "Gave error", str(err)\n        fail += 1')


# In[10]:

print cap.stdout
with open('filtered_kinetics.py', 'a') as f:
    f.write(cap.stdout)


# In[11]:

success, fail


# In[1]:

for r in new_reactions:
    print r,  r in ooh_forward


# In[ ]:




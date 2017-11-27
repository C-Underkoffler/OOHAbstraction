
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

get_ipython().run_cell_magic(u'capture', u'cap --no-stderr', u'success = fail = 0\nfor reaction in to_try:\n    try:\n        path = os.path.join(root_dir, reaction, \'m062x\',\'output.py\')\n        with open(path) as f:\n            lines = f.readlines()\n        start = lines.index(\'kinetics(\\n\')\n        print\n        print "# {} from {}".format(reaction, root_dir)\n        print \'\'.join(lines[start:])\n        success += 1\n    except Exception as err:\n        print "# \u26a0\ufe0f", reaction, "Gave error", str(err)\n        fail += 1')


# In[6]:

with open('filtered_kinetics.py', 'w') as f:
    f.write('# - *- coding: utf- 8 - *-/n')
    f.write(cap.stdout)
print cap.stdout


# In[7]:

success, fail


# # Now try the new ones
# These are in `/gss_gpfs_scratch/westgroup/QMscratch/`

# In[8]:

root_dir = '/gss_gpfs_scratch/westgroup/QMscratch/'
new_reactions = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir,f)) ]
print new_reactions
len(new_reactions)


# In[9]:

new_forward = []
new_reverse = []
for r in new_reactions:
    reactants, products = r.split('_')
    reactants = reactants.split('+')
    products = products.split('+')
    if '[O]O' in reactants and 'OO' in products:
        new_forward.append(r)
    elif '[O]O' in products and 'OO' in reactants:
        new_reverse.append(r)
len(new_forward), len(new_reverse)


# In[10]:

to_try = []
for reaction in new_forward:
    try:
        path = os.path.join(root_dir, reaction)
        files = os.listdir(path)
        assert 'output.py' in files, "Doesn't have output.py file"
        to_try.append(reaction)
    except Exception as err:
        print "# ⚠️", reaction, "Gave error", str(err)
len(to_try)


# In[11]:

get_ipython().run_cell_magic(u'capture', u'cap --no-stderr', u'success = []\nduplicate = []\nfail = []\nfor reaction in to_try:\n    try:\n        path = os.path.join(root_dir, reaction, \'output.py\')\n        with open(path) as f:\n            lines = f.readlines()\n        start = lines.index(\'kinetics(\\n\')\n        print\n        print "# {} from {}".format(reaction, root_dir)\n        if reaction in ooh_forward:\n            print \'# This is a duplicate of one above so commenting it out:\\n"""\'\n            duplicate.append(reaction)\n        print \'\'.join(lines[start:])\n        success.append(reaction)\n        if reaction in ooh_forward:\n            print \'"""\\n\'\n    except Exception as err:\n        print "# \u26a0\ufe0f", reaction, "Gave error", str(err)\n        fail.append(reaction)')


# In[12]:

print cap.stdout
with open('filtered_kinetics.py', 'a') as f:
    f.write("###### NOW DOING THINGS IN "+root_dir)
    f.write(cap.stdout)


# In[13]:

len(success), len(duplicate), len(fail)


# In[14]:

for r in success:
    print r,  
    if r in duplicate: print "is a DUPLICATE and",
    if r in fail: print "FAILED"
    if r in success: print "worked"


# In[15]:




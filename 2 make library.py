
# coding: utf-8

# In[1]:

import os, sys
rmg_path = os.getenv('RMGpy')
if rmg_path and rmg_path not in sys.path:
    sys.path.insert(1,rmg_path)
sys.path


# In[2]:

# Not actually sure which of all these we need...
# it's mostly copied from the importChemkin.py script.
# actually, from some old version that was lying around somewhere :-/
import os
import logging # doesn't work well in a notebook, without some fu
import rmgpy
import rmgpy.rmg
import rmgpy.rmg.input
#from rmgpy.display import display
from IPython.display import display
from rmgpy.chemkin import loadChemkinFile, readSpeciesBlock, readThermoBlock, readReactionsBlock, removeCommentFromLine
from rmgpy.data.thermo import Entry, saveEntry
from rmgpy.data.base import Entry as kinEntry
from rmgpy.data.kinetics.common import saveEntry as kinSaveEntry
from rmgpy.molecule import Molecule
from rmgpy.rmg.model import Species
from rmgpy.reaction import Reaction
from rmgpy.kinetics import Arrhenius
from rmgpy.cantherm.output import prettify
from rmgpy.rmg.main import RMG, initializeLog
from rmgpy.molecule.draw import MoleculeDrawer

#import time
import sys
## Put the RMG-database project at the start of the python path, so we use that importOldDatabase script?
## (is this still needed?)
databaseDirectory = rmgpy.settings['database.directory']
databaseProjectDirectory = os.path.abspath(os.path.join(databaseDirectory, '..'))
sys.path.insert(0, databaseProjectDirectory)


# In[3]:

logging.info("Loading RMG database...")
rmg = RMG()
rmg.outputDirectory = '.'
rmg.scratchDirectory = '.'
rmg.databaseDirectory = databaseDirectory
rmg.thermoLibraries = ['primaryThermoLibrary']
rmg.kineticsFamilies = ['H_Abstraction',]
rmg.reactionLibraries = [('KlippensteinH2O2', False),]
rmgpy.rmg.input.rmg = rmg  # put it in this scope so these functions can modify it
#rmg.loadDatabase()  # this seems to hang (forever??) but turns out it's not needed!
logging.info("Loaded database.")


# In[4]:

rmg.reactionModel = rmgpy.rmg.model.CoreEdgeReactionModel()
rmg.reactionModel.kineticsEstimator = 'rate rules'
rmg.reactionModel.verboseComments = True
rmg.initialSpecies = []
rmg.reactionSystems = []

def makeOrEmptyDirectory(path):
    """Either create a directory at `path` or delete everything in it if it exists"""
    if os.path.exists(path):
        assert os.path.isdir(path), "Path {0} exists but is not a directory".format(path)
        # empty it out
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    else:
        os.makedirs(path)
        


# In[5]:

kineticsLibrary = rmgpy.data.kinetics.KineticsLibrary(
        label="AutoTST-M062X",
        name="AutoTST-M062X",
        solvent=None,
        shortDesc="AutoTST using M062X",
        longDesc="AutoTST calculations using M062X",
        )
def addReactionToKineticsLibrary(reaction):
    """
    Add the reaction (once species are identified) to the reactionLibrary
    """
    entry = kinEntry()
    entry.index = len(kineticsLibrary.entries) + 1
    entry.item = reaction
    entry.label = str(reaction)
    entry.data = reaction.kinetics
    comment = getattr(reaction, 'comment', '')
    if comment:
        entry.longDesc = comment + '.\n'
    else:
        entry.longDesc = ''
    entry.shortDesc = 'AutoTST M062X for {0}'.format(str(reaction))
    kineticsLibrary.entries[entry.index] = entry

def savePyKineticsLibrary(kineticsLibrary):
    "Save an RMG-Py style kinetics library"
    library_path = 'RMG-Py-kinetics-library'
    makeOrEmptyDirectory(library_path)
    kineticsLibrary.checkForDuplicates(markDuplicates=True)
    #kineticsLibrary.convertDuplicatesToMulti()
    kineticsLibrary.save(os.path.join(library_path, 'reactions.py'))
    kineticsLibrary.saveDictionary(os.path.join(library_path, 'dictionary.txt'))

    savedReactions = [kineticsLibrary.entries[key].item 
                      for key in sorted(kineticsLibrary.entries.keys())
                      ]


# In[6]:

species_dict = {}

def kinetics(label, kinetics):
    reactants, products = label.split('_')
    reactants = reactants.split('+')
    products = products.split('+')

    reaction = Reaction(reactants=[], products=[], reversible=True)
    
    for in_list, out_list in [(reactants, reaction.reactants), (products, reaction.products)]:
        for i, smiles in enumerate(in_list):
            if smiles not in species_dict:
                species = Species().fromSMILES(smiles)
                species_dict[smiles] = species
                species.label = '{0}({1})'.format(species.toChemkin(), len(species_dict))
            out_list.append(species_dict[smiles])
    
    reaction.kinetics = kinetics
    print repr(reaction)
    display(reaction)
    
    addReactionToKineticsLibrary(reaction)
    


# In[7]:

kinetics(
    label = 'C=CCC=C+[O]O_C=C[CH]C=C+OO',
    kinetics = Arrhenius(
        A = (1.46901e-07, 'cm^3/(mol*s)'),
        n = 5.46227,
        Ea = (16.0409, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.40766, dn = +|- 0.115316, dEa = +|- 0.634353 kJ/mol',
    ),
)


# In[8]:

kineticsLibrary.entries


# In[9]:

savePyKineticsLibrary(kineticsLibrary)


# In[10]:

kineticsLibrary.entries.clear()


# Next we paste in the results from the previous notebook. Uncomment the first line
# ```
# %run filtered_kinetics.py
# ```

# In[11]:

get_ipython().magic(u'run -i filtered_kinetics.py')


# In[12]:

savePyKineticsLibrary(kineticsLibrary)


# In[ ]:




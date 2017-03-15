#!/bin/bash

NOTEBOOK="1 Filter OOH.ipynb"
jupyter nbconvert --to=notebook --inplace --execute "$NOTEBOOK"
jupyter nbconvert --to=html "$NOTEBOOK"
jupyter nbconvert --to=python "$NOTEBOOK"

NOTEBOOK="2 make library.ipynb"
jupyter nbconvert --to=notebook --inplace --execute "$NOTEBOOK"
jupyter nbconvert --to=html "$NOTEBOOK"
jupyter nbconvert --to=python "$NOTEBOOK"


# Copy the reaction libary into the Importer folder
cp -r RMG-Py-kinetics-library /gss_gpfs_scratch/westgroup/Importer/RMG-models/AutoTST-OOHabstraction/

# Run the model comparer tool to regenerate the xls spreadsheets
export PYTHONPATH=/gss_gpfs_scratch/westgroup/Importer/RMG-Py:$PYTHONPATH
python /gss_gpfs_scratch/westgroup/Importer/RMG-models/modelComparer/modelComparer.py /gss_gpfs_scratch/westgroup/Importer/RMG-models/ --names=/gss_gpfs_scratch/westgroup/Importer/RMG-models/PCI2013/353-Malewicki

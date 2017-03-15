#!/bin/bash

NOTEBOOK="1 Filter OOH.ipynb"
jupyter nbconvert --to=notebook --inplace --execute "$NOTEBOOK"
jupyter nbconvert --to=html "$NOTEBOOK"
jupyter nbconvert --to=python "$NOTEBOOK"

NOTEBOOK="2 make library.ipynb"
jupyter nbconvert --to=notebook --inplace --execute "$NOTEBOOK"
jupyter nbconvert --to=html "$NOTEBOOK"
jupyter nbconvert --to=python "$NOTEBOOK"

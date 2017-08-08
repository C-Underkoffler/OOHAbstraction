#!/bin/bash

NOTEBOOK="progressMetering.ipynb"
jupyter nbconvert --to=notebook --inplace --execute "$NOTEBOOK"
jupyter nbconvert --to=html "$NOTEBOOK"
jupyter nbconvert --to=python "$NOTEBOOK"
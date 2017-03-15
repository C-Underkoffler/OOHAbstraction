#!/bin/bash

jupyter nbconvert --to=notebook --inplace --execute "1 Filter OOH.ipynb"
jupyter nbconvert --to=html "1 Filter OOH.ipynb"
jupyter nbconvert --to=python "1 Filter OOH.ipynb"

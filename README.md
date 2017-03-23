# Instructions for OOHabstraction

## To start new calculations:

On discovery, with $RMGpy pointing to an RMG-Py installation on the OOHAbstraction branch, and having called `export PYTHONPATH=$RMGpy:$PYTHONPATH` to ensure it's at the front of your path,
1. `$ python $RMGpy/scripts/filterReactions.py /scratch/westgroup/Importer/RMG-models/`
    This will create updated `kineticsDict.pkl` that we later use.
2. `$ cp $RMGpy/scripts/autoTST-slurm.sh ./`
3.  Update it to have the array values you wish to run.
2. `$ sbatch autTST-slurm.sh`


## To postprocess the calculations

**See the run_all.sh script**. You can probably just sbatch that and it'll do all this.

Do this on Discovery:

1. Run `1 Filter OOH.ipynb`. This reads all the files in `'/scratch/bhoorasingh.p/QMfiles/Reactions/H_Abstraction/'` looking for things with OOH reactant and HOOH product, and then those in `'/gss_gpfs_scratch/westgroup/QMscratch/'` looking for the same but removing duplicates. It writes all these to `filtered_kinetics.py`.
2. Run `2 make library.ipynb`. This reads everything in `filtered_kinetics.py` and turns it into an RMG-compatible reaction library, saved in `RMG-Py-kinetics-library`.
3. Copy that folder to `/gss_gpfs_scratch/westgroup/Importer/RMG-models/AutoTST-OOHabstraction/`
4. Probably worth adding and the updated folder to git, committing, and pushing. It's the [RMG-models](https://github.com/comocheng/RMG-models) repo.
5. Run the model comparer tool in `/gss_gpfs_scratch/westgroup/Importer/RMG-models/modelComparer`, eg.  `sbatch -p west comparer.sh`. This creates the `output.xls` and all the `.txt` files that compare thermo and kinetics across models. There are options to specify whose names are used preferentially, etc, and to limit things to only species in one model, but for this project I think we want to include everything.
6. Run (Nate's script called ?) which reads in the `output.xls` file into Pandas and does some analysis... (fill in here)

Also, to get statistics on how far jobs are getting:
(this should be moved into the OOHabstraction repository along with everything else)
```
cd /gss_gpfs_scratch/westgroup
srun -p westlargemem jupyter nbconvert --to html --execute progressMetering.2.ipynb
```
then download `progressMetering.2.html` and have a look.

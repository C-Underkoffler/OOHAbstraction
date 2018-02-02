#!/bin/sh
#set a job name
#SBATCH --job-name=symmetry_rerun

#a file for job output, you can check job progress
#SBATCH --output=symmetry_rerun.%a.slurm.log

# a file for errors from the job
#SBATCH --error=symmetry_rerun.%a.slurm.log

#time you think you need; default is one day
# d-hh:mm:ss
#SBATCH --time=0

#number of tasks you are requesting
#SBATCH -N 1
#SBATCH -n 10
##SBATCH --ntasks-per-node=2
##SBATCH --exclusive

#partition to use
#SBATCH --partition=west

#number of nodes to distribute n tasks across
#SBATCH -N 1

#an array job
#SBATCH --array=1-150


#####################################################

export RMGpy=~/Code/RMG-Py
export PYTHONPATH=$RMGpy:$PYTHONPATH


#python $RMGpy/scripts/filterReactions.py /scratch/westgroup/Importer/RMG-models/
## that creates the kineticsDict files, and doesn't need repeating until the imported models change significantly
echo $SLURM_ARRAY_TASK_ID
cd /home/harms.n/Code/OOHabstraction/comparisonTST
# the "stdbuf -o0 -e0"  and the "-u" are to disable buffering,
# so that you see output from the script in the log files immediately.
stdbuf -o0 -e0 python -u ~/Code/OOHabstraction/comparisonTST/python_files/comparisonTST_symmetry_rerun.py > /gss_gpfs_scratch/harms.n/comparerTST/AutoTST-comparer.symmetry_rerun.1.$SLURM_ARRAY_TASK_ID.combined.log 2>&1

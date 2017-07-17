#!/bin/sh
#set a job name
#SBATCH --job-name=natesSideProject

#a file for job output, you can check job progress
#SBATCH --output=thcTST.%a.slurm.log

# a file for errors from the job
#SBATCH --error=thcTST.%a.slurm.log

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
#SBATCH --array=1-112%2


#####################################################

export RMGpy=~/Code/RMG-Py
export PYTHONPATH=$RMGpy:$PYTHONPATH


#python $RMGpy/scripts/filterReactions.py /scratch/westgroup/Importer/RMG-models/
## that creates the kineticsDict files, and doesn't need repeating until the imported models change significantly
echo $SLURM_ARRAY_TASK_ID
cd /gss_gpfs_scratch/harms.n/thcTST/
# the "stdbuf -o0 -e0"  and the "-u" are to disable buffering,
# so that you see output from the script in the log files immediately.
stdbuf -o0 -e0 python -u ~/Code/OOHabstraction/THC/thcTST.py > /gss_gpfs_scratch/harms.n/thcTST/AutoTST-THC.$SLURM_ARRAY_TASK_ID.combined.log 2>&1

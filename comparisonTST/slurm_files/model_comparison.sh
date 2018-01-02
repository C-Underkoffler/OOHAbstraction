#!/bin/sh
#set a job name
#SBATCH --job-name=model_comparison

#a file for job output, you can check job progress
#SBATCH --output=model_comparison_heptane.%a.slurm.log

# a file for errors from the job
#SBATCH --error=model_comparison_heptane.%a.slurm.log

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
#SBATCH --array=1


#####################################################



#python $RMGpy/scripts/filterReactions.py /scratch/westgroup/Importer/RMG-models/
## that creates the kineticsDict files, and doesn't need repeating until the imported models change significantly
echo $SLURM_ARRAY_TASK_ID
# the "stdbuf -o0 -e0"  and the "-u" are to disable buffering,
# so that you see output from the script in the log files immediately.

cd ~/Code/OOHabstraction/comparisonTST/python_files

python ~/Code/OOHabstraction/comparisonTST/python_files/sarathy_comparison.py
python ~/Code/OOHabstraction/comparisonTST/python_files/heptane_comparison.py

#!/bin/sh
#set a job name
#SBATCH --job-name=progressMeteringDF

#a file for job output, you can check job progress
#SBATCH --output=progressMeteringDF.%a.slurm.log

# a file for errors from the job
#SBATCH --error=progressMeteringDF.%a.slurm.log

#time you think you need; default is one day
# d-hh:mm:ss

#number of tasks you are requesting
#SBATCH -N 1
#SBATCH -n 10
##SBATCH --ntasks-per-node=2
##SBATCH --exclusive

#partition to use
#SBATCH --partition=par-gpu-2

#number of nodes to distribute n tasks across
#SBATCH -N 1

#an array job
#SBATCH --array=1


#####################################################

export RMGpy=~/Code/RMG-Py
export PYTHONPATH=$RMGpy:$PYTHONPATH

python progressMeteringDF.py

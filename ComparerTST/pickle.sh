#!/bin/bash
#!/bin/sh
#set a job name
#SBATCH --job-name=pckl

#a file for job output, you can check job progress
#SBATCH --output=pckl.%a.slurm.log

# a file for errors from the job
#SBATCH --error=pckl.%a.slurm.log

#time you think you need; default is one day
# d-hh:mm:ss
#SBATCH -p par-gpu 

python makeKineticsPkl.py

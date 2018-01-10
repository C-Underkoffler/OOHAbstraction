#!/bin/sh
#SBATCH -n 1
#SBATCH --job-name=ooh_comparison
#SBATCH -e error.log
#SBATCH -o output.log
#SBATCH -p ser-par-10g

stdbuf -o0 -e0 python3 -u test_performance.py

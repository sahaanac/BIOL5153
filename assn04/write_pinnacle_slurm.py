#! /usr/bin/env python3

# This script generates a SLURM script for the AHPCC Pinnacle cluster
jobname = "chandran_pinnacle_python_test"
queue = "comp01"
node = 1
processor = 32
wall = 5 # this is in hours

# This section prints the header/required info for the SLURM script
print('#SBATCH - J' + " " + jobname) # jobname 
print('#SBATCH -- partition' + " " + queue) #which queue to use 
print('#SBATCH - o' + " " + jobname + '_%j.txt') # standard output file
print('#SBATCH - e' + " " + jobname + '_%j.err') # standard error file
print('#SBATCH --mail-type=ALL') 
print('#SBATCH --mail-user=sc112@uark.edu') 
print('#SBATCH --nodes=' + str(node)) # Number of nodes to ask for
print('#SBATCH --ntasks-per-node=' + str(processor)) # Tasks in each node
print('#SBATCH --time=' + str(wall) + ':00:00') # Set the walltime
print()

print('export OMP_NUM_THREADS=32')
print()

#load the necessary modules
print('# load modules')
print('module purge')
print('module load samtools')
print('moduleload jellyfish')
print('moduleload bowtie2')
print('moduleload salmon/0.8.2')
print('moduleload java')
print()

# cd into the directory where you are submitting this script from
print('cd $SLURM_SUBMIT_DIR')
print()

# copy files from storage to scratch 
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')
print()

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')
print()

# copy output files back to storage
print('rsync -av trinity_Run2 $SLURM_SUBMIT_DIR')

#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster.
jobname = "chandran_razor_python_test"
queue = "onenode16core"
oe = "chandran_razor_python_test_STDOUT_STDERR"
sc112 = "chandran_razor_python_test.out"
node = 1
processor = 1
wall = 3 # this is in hours


# This section prints the header/required info for the PBS script
print('#PBS -N' + " " + jobname) # job name 
print('#PBS -q' + " " + queue) # which queue to use
print('#PBS -j' + " " + oe) # join STDOUT and STDERR into single file
print('#PBS -o' + " " + sc112 + '$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(node) + ':ppn=' + str(processor)) # how many resource to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

#cd into working directory
print('cd $PBS_O_WORKDIR')
print()

#load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print('module load python/3.7.3-anaconda')
print()

#commands for this job
print('# insert commands here')

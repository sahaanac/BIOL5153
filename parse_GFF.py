#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# This script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments (absolutely required and order matters)
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(genome.seq)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:

    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    #loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
      
        # For Python Index
        genomestart = int(line[3]) - 1 
        genomeend = int(line[4])
       
        # Strand Information
        strandinfo = line[6]

        # Header Information
        headerinfo = line[8]

        # printing fasta header
        print('>' + genome.id, headerinfo)

         # printing sequence based on strand info
        if strandinfo == '-': 
            print(genome.seq[genomestart:genomeend].reverse_complement()) 
        else: 
            print(genome.seq[genomestart:genomeend]) 

#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

import re
from collections import OrderedDict



def rev_comp(genome,genomestart,genomeend):
  return genome.seq[genomestart:genomeend].reverse_complement()

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

CDS_FEATURE = 'CDS'
data = OrderedDict()
finaldict = OrderedDict()
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

        #Feature
        feature = line[2]

        # Iterating only if it is CDS Feature
        if feature == CDS_FEATURE:

            # Regex to identify if exon is present or not
            exonregex = re.search("exon \d", headerinfo)

            #Regex to identify the type of gene
            generegex = re.search("(?<=Gene\s)\S*", headerinfo)

            # if No exon available, then continue with reading next line
            if(exonregex == None):
                continue;
            exon_number = exonregex[0]
            gene = generegex[0]
            
            #Adding to dictionary only if exon available
            if exon_number:

                # Creating unique dictionary key to store elements
                dict_key = gene + "_" + exon_number

                if strandinfo == '-':
                    extracted_sequence = rev_comp(genome,genomestart,genomeend)
                else: 
                    extracted_sequence = genome.seq[genomestart:genomeend]

                data[dict_key]= extracted_sequence

# Sorting the dictionary keys
sorted_dictionary = OrderedDict(sorted(data.items()))

# Appending the values of the same key in fianl dictioanry for output purposes
for key, value in sorted_dictionary.items():
    gene_key = key.split()

    if (finaldict.get(gene_key[0]) == None):
        finaldict[gene_key[0]] = value
    else:
        finaldict[gene_key[0]] = finaldict[gene_key[0]] + value

# Printing the Output in the expected format
for key, value in finaldict.items():
    print(">Citrullus_lanatus_"+key)
    print(value)
    print()
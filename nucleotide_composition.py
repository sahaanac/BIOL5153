#! /usr/bin/env python3
# set the name of the input DNA sequence file
#dna_sequence = "ACGGATCCTATCAAATATTTCACATTTTCTATGATCATCTCTATTTTAGGTATTCGGGGAATCCTCCTTAATAGACGAAATATTCCTATTATGTCAATGCCAATTGAATCAATGTTATTAGCTGTGAATTCGAACTTTTTGGTATTTTCCGTTTCTTCGGATGATATGATGGGTCAATCATTTGCTTCATTGGTTCCAACGGTGGCAGCTGCGGAATCCGCTATTGGGTTAGCCATTTTCGTTATTACTTTCCGAGTCCGAGGGACTATTGCTGTAGAATTTATTAATAGCATTCAAGGTTAA"
filename = "nad4L_DNA.txt"

# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

# read the file
dna_sequence = infile.read().rstrip()

# close the file
infile.close()

# find the sequence length
seqlen = len(dna_sequence)
print("Sequence Length:", seqlen)

# calculate the frequency of A in the sequence
numA = dna_sequence.count ('A')
freqA = numA/seqlen
print ("Freq of A: %.3f" % (freqA))

# calculate the frequency of C in the sequence
numC = dna_sequence.count ('C')
freqC = numC/seqlen
print ("Freq of C: %.3f" %(freqC))

# calculate the frequency of G in the sequence
numG = dna_sequence.count ('G')
freqG = numG/seqlen
print ("Freq of G: %.3f" % (freqG))

# calculate the frequency of T in the sequence
numT = dna_sequence.count ('T')
freqT = numT/seqlen
print("Freq of T: %.3f" % (freqT))

# calculate G+C content
freqGC = freqG + freqC
print ("G + C content: %.3f" % (freqGC))

# check to see of frequencies sum to 1
freqsum = freqA + freqT + freqG + freqC
print (freqsum)

#!/usr/bin/env python3

# Description: Count number of each DNA base

f = open("rosalind_dna.txt", 'r')
bases = f.readline().rstrip()

for i in 'ACGT':
    print(bases.count(i)),
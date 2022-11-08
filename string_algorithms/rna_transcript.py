#!/usr/bin/env python3

# Description: DNA -> mRNA

f = open("rosalind_rna.txt", 'r')
bases = f.readline().rstrip()

def changeTU(dna):
    return ''.join("U" if l == "T" else l for l in dna)

print(changeTU(bases))
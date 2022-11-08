#!/usr/bin/env python3

# Description: Given a DNA sequence, find its reverse compliment

f = open("rosalind_revc.txt", 'r')
bases = f.readline().rstrip()

def revTrans(dna):
    compliments = {"A":"T", "C":"G", "G":"C", "T":"A"}

    dna = ''.join(compliments[l] for l in dna)
    
    return dna[::-1]

print(revTrans(bases))
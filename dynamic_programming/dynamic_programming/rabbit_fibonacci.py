#!/usr/bin/env python3

# Description: Starting with 1 pair, rabbits mature in 1 month and produce 'b' pairs of offspring.
# Total population at the end of 'a' months is to be calculated.

f = open("rosalind_fib.txt", 'r')
a,b = [int(x) for x in f.readline().rstrip().split()]


def fib(n,k):
    if n > 0:
        if n == 1 or n == 2:
            sum = 1
            return sum
        else:
            sum = fib(n-1,k) + k*fib(n-2,k)
            return sum


print(fib(a,b))
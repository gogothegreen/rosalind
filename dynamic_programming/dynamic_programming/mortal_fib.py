#!/usr/bin/env python3

# Description: rabbit fibonacci with rabbits having a life span of 'b' months
# Total population at the end of 'a' months is to be calculated.

f = open("rosalind_fibd.txt", 'r')
a,b = [int(x) for x in f.readline().rstrip().split()]
#a = 6
#b = 3
print(a)
print(b)

def mortal_fib_rec(n,k):
    # recursive implimentation
    # NOT WORKING as expected
    if n > 0:
        if n == 1 or n == 2:
            sum = 1
            #print(f"-> mortal_fib({n}) returns {sum}")
            return sum
        elif n < k:
            sum  =  mortal_fib_rec(n-2,k) + mortal_fib_rec(n-1,k)
            #print(f"-> mortal_fib_rec({n}) returns {sum}")
            return sum
        elif n-k == 0 or n-k == 1:
            sum = mortal_fib_rec(n-2,k) + mortal_fib_rec(n-1,k) - 1
            return sum
        else:
            sum = mortal_fib_rec(n-2,k) + mortal_fib_rec(n-1,k) - mortal_fib_rec(n-k-1,k)
            return sum

def mortal_fib(n,m):
    bunnies = [1, 1]                                                           
    months = 2
    count = []                                                                     
    while months < n:                                                              
        if months < m:                                                             
            bunnies.append(bunnies[-2] + bunnies[-1])                              
        elif months == m or count == m + 1:                                        
            bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
        else:                                                                      
            bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(                  
                m + 1)])                                                           
        months += 1
    return bunnies[-1]

print(mortal_fib(a,b))
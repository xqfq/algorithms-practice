
from random import randint
import numpy as np

class UniversalHashing:
    def __init__(self,num_b,k):
        '''
        num_b = number of buckets
        k = vector key
        Doing universal hashing
        '''
        self.num_b = num_b
        self.k = k
        self.p = MinPrime(num_b)
    def key(self):
        '''
        Returns the index of the key in the hash table
        '''
        a = [0] * len(self.k)
        for i in range(len(self.k)):
            a[i] = randint(0, (self.p - 1))
        return (sum(np.array(self.k) * np.array(a))) % self.p

def MinPrime(x):
    '''
    Returns the smallest prime number larger than a positive integer
    '''
    if x == 1:
        return 2
    elif x == 2:
        return 3
    elif x == 3:
        return 5
    else:
        # Check primality of odd numbers
        # By Bertrand's postulate, guaranteed to find a prime number
        # between x and 2*x-1
        if x % 2 ==0:
            x += 1
            if miller(x,40):
                return x
            else:
                return MinPrime(x+2)
        else:
            if miller(x,18):
                return x
            else:
                return MinPrime(x+2)

def miller(n,iteration):
    '''
    Check whether a positive integer x is a prime number
    '''
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d = d // 2
    for i in range(iteration):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x ==1 or x == n-1:
            continue
        for i in range(s-1):
            x = pow(x,2,n)
            if x == n - 1:
                break
        else:
            return False
    return True

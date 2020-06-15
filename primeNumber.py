import math
import sys
import os

def primeNumber(n):

    ''' this function return  if the number is a prime number
    or not ex :
    primeNumber(12) return False
    primeNumber(13) return True'''
    
    if n > 1 :
        for i in range (2, n/2) :
            if n%i == 0 :
                return False
                break
        return True
    else :
        return False
    

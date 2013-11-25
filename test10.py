from math import *
def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for i in range(3,int(ceil(sqrt(n)))+1,2):
        if n%i == 0:
            return False
    return True
print isPrime(157)
print isPrime(571)
print isPrime(715)
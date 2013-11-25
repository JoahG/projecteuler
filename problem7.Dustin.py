from math import *
 
def isPrime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(ceil(sqrt(n)))+1,2):
        if n%i == 0:
            return False
    return True
 
count = 1 #counting 2 as first prime
i = 3
while count <= 10001:
    if isPrime(i):
        count += 1
    if count == 10001 and isPrime(i):
        print i
    i += 2
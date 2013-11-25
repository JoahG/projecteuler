from math import *
def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for i in range(3,int(ceil(sqrt(n)))+1,2):
        if n%i == 0:
            return False
    return True
a = 0
for i in range(7650000, 8000000):
	if isPrime(i):
		s = []
		y = True
		for j in range(0,len(str(i))):
			s.append(str(i)[j])
		for k in range(1,len(str(i))+1):
			try:
				s.index(str(k))
			except:
				y = False
				break
		if y:
			a = i
			break
print a

# ==> 7652413
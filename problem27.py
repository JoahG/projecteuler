# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

def isPrime(number):
	try:
	    if number%2 == 0:
	        return False
	    for p in range(3,int(number**0.5)+1,2):
	        if number%p==0:
	            return False
	    return True
	except:
		return False


def checkNumPrimes(a,b):
	c = 0
	while isPrime(c**2+a*c+b):
		c += 1
	return c

maximum = 1000
minimum = -1000
t = False
a = minimum
while a < maximum:
	b = minimum
	while b < maximum:
		if checkNumPrimes(a,b) > 70:
			print checkNumPrimes(a,b), a, b, a*b
			t = True
		if t:
			break
		b += 1
	if t:
		break
	a += 1
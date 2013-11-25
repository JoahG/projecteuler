# Project Euler Problem #23
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def isAbundant(n):
	return (sum([i for i in range(1,n) if n % i == 0]) > n)

def abundantLimit(n):
	return [i for i in range(1,n) if isAbundant(i)]

def abundantList(n):
	a = abundantLimit(n)
	l = range(n)
	for i in a:
		if i % 1000 == 0:
			print i
		for j in a:
			if i + j >= n:
				break
			l[i+j] = 0
	return l

print sum(abundantList(28123))
# ==> 4179871
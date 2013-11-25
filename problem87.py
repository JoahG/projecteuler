
import math

def genPrimes(n):
	l = range(2,n)
	primes = []
	while len(l) > 0:
		p = l[0]
		primes.append(p)
		t = p
		while t < n:
			if t in l:
				l.remove(t)
			t += p
	return primes

def problem(n):
	t = genPrimes(int(math.floor(n/3)))
	p = 0
	for a in t:
		for b in t:
			for c in t:
				d = (a**2) + (b**3) + (c**4)
				if d < n:
					p += 1
	return p

print problem(50000000)
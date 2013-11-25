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
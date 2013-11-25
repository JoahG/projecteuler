def isPrime(number):
  if number%2 == 0 and number != 2 or number==1:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True

primes = []

for i in range(1,10000000):
	if isPrime(i):
		primes.append(i)

y = {}
while len(primes) > 1:
	t = 0
	i = 0
	while t <= 1000000:
		t += primes[i]
		if isPrime(t):
			try:
				y.index(t)
			except:
				y[i] = t
		i += 1

	primes.remove(primes[0])



print y
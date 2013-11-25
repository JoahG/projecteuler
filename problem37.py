# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def isPrime(number):
  if number%2 == 0 and number != 2 or number==1:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True

def isTruncatablePrime(n):
	s = str(n)
	f = s
	if not isPrime(n):
		return False
	for i in range(0,len(s)-1):
		f = list(f)
		del(f[0])
		f = "".join(f)
		if not isPrime(int(f)):
			return False
	f = s
	for i in range(0,len(s)-1):
		f = list(f)
		del(f[-1])
		f = "".join(f)
		if not isPrime(int(f)):
			return False
	return True

t = 0
i = 0
j = 0
while i < 15:
	if isTruncatablePrime(j):
		i += 1
		t += j
		print i,j
	j += 1

print t
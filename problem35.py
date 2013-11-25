# How many circular primes are there below one million?

def isPrime(number):
  if number%2 == 0:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True
def rot(s, n):
	i = n
	h = 0
	m = ""
	while True:
		try:
			m += s[i]
			i += 1
		except:
			while h < n:
				m += s[h]
				h += 1
			break
	return m
a = 0
i = 1
while i <= 1000000:
	if isPrime(i):
		o = 1
		while isPrime(int(rot(str(i),o))):
			if o == len(str(i)):
				a += 1
				break
			o += 1
	i += 1
print a

# ==> 56
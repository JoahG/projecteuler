# Find the value of n  1,000,000 for which n/phi(n) is a maximum.

def isPrime(number):
  if number%2 == 0:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True

def phi(n):
	t = []
	if not isPrime(n):
		for i in range(1,n):
			b = True
			for j in range(2, i+1):
				if n % j == 0 and i % j == 0:
					b = False
			if b:
				t.append(i)
		return len(t)
	else:
		return 1

def r(n):
	return float(float(n)/float(phi(n)))

ans = []

i = 999000
while i <= 1000000:
	print r(i)
	i += 1

ans.sort()
ans.reverse()

print ans[0][1]
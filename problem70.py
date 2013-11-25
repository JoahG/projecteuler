

def isPrime(number):
  if number%2 == 0 or number==1:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True


def phi(n):
	t = 0
	if not isPrime(n):
		for i in range(1,n):
			b = True
			for j in range(2, i+1):
				if n % j == 0 and i % j == 0:
					b = False
			if b:
				t += 1
		return t
	else:
		return 1

print phi(87109)
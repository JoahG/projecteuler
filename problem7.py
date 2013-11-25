# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def isPrime(number):
  if number%2 == 0:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True
  
i = 0
p = 2
while i <= 10001:
	p+=1
	if isPrime(p):
		i+=1
a = p
print a

# ==> 104743
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million

def isPrime(number):
        if number%2 == 0:
            return False
        for p in range(3,int(number**0.5)+1,2):
                if number%p==0:
                        return False
        return True
total = 0
for i in range(2, 2000000):
	if isPrime(i) and i%2!=0:
		total+=i
print total

# ==> 142913828922
#Find the sum of the digits in the number 100!

def factorial(n):
	if (n == 0):
		return 1
	return n*factorial(n-1)
t = 0
for i in str(factorial(100)):
	t += int(i)
print t

# ==> 648
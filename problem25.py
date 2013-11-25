# What is the first term in the Fibonacci sequence to contain 1000 digits?

a = 1
b = 1
c = 2
n = 3
while True:
	a = b
	b = c
	c = a + b
	n += 1
	if len(str(c)) == 1000:
		n = int(n)
		break
print n
# ==> 4782
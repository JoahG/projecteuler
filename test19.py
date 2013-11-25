def fib(n):
	a = 1
	b = 1
	c = 2
	t = 3
	if n > t:	
		while True:
			a = b
			b = c
			c = a + b
			t += 1
			if t == n:
				return c
	else:
		y = [0,a,b,c]
		return y[n]

for i in range(1,14):
	print fib(i)
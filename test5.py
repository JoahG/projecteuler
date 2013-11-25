def f(n):
	if (n == 0):
		return 1
	return n*f(n-1)

print f(4)+f(0)+f(5)+f(8)+f(5)
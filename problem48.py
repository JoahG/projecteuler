# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

t = 0
for i in range(1,1001):
	t += i ** i
a = str(t)[-10:]
print a

# ==> 9110846700
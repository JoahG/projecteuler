# How many n-digit positive integers exist which are also an nth power?

a = 0
i = 1
while a < 50:
	if (i ** (float(1)/float(len(str(i))))) % 1 == 0:
		print i
		a += 1
	i += 1
print a
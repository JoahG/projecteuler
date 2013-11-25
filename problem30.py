# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

a = 0
i = 2
while i <= 1000000:
	t = 0
	for m in [int(str(i)[j])**5 for j in range(0,len(str(i)))]:
		t += m
	if i == t:
		a += i
	i += 1

print a

# ==> 443839
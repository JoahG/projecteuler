# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def f(n):
	if n == 0:
		return 1
	return n*f(n-1)
a = 0
i = 0
while True:
	t = 0
	for j in str(i):
		t += f(int(j))
	if t == i:
		a += i
	i += 1
	if i == 1000000:
		break
print a

# ==> 40730
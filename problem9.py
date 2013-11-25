# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
s = 1
f = 1001
for a in range(s, f):
	for b in range(s,f):
		if a+b+(((a**2)+(b**2))**0.5)==1000:
			print int(a*b*(((a**2)+(b**2))**0.5))
# ==> 31875000

# a = 200
# b = 375
# c = 425
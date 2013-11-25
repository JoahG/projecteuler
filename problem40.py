# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

i = "01"
j = 2
while len(i) < 1000003:
	i += str(j)
	j += 1

print i[:10]
print int(i[1]) * int(i[10]) * int(i[100]) * int(i[1000]) * int(i[10000]) * int(i[100000]) * int(i[1000000])
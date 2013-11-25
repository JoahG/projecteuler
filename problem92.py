# How many starting numbers below ten million will arrive at 89?
a = 0
i = 1
u = [89]
while i < 10000000:
	g = i
	while True:
		k = 0
		for j in str(g):
			k += int(j)**2
		g = k
		if g == 1:
			break
		if g in u:
			a += 1
			u.append(i)
			break
	i +=1
print a

# ==> 8581146
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
f = [1,2]
j = 0
total = 0
while j <= 4000000:
	i = len(f)
	j = f[i-1]+f[i-2]
	f.append(j);

for i in f:
	if i%2==0:
		total+=i
print total
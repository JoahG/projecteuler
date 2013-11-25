i = "hello"
p = []
for t in range(0, len(i)):
	p.append(i[t])
q = []
for j in range(0,len(p)):
	q.append(p[(len(p)-1)-j])
print p
print q
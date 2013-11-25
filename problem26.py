
y = ""
t = {}
for j in range(1,1001):
	e = str(float(1)/float(j)).split(".")[1]
	for i in range(0,len(e)):
		if len([j for j in e.split(e[0:i+1]) if j != '']) == 0:
			t[int(e[0:i+1])] = j
			break
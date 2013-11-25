#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

p = open('matrix.txt', 'r')
p = p.readlines()
a = []
for i in p:
	j = i.replace("\n","")
	n = []
	for u in j.split(","):
		n.append(int(u))
	a.append(n)


col = 0
row = 0
answer = a[row][col]
q = a[row][col]
while col < len(a)-1 or row < len(a)-1:
	p = False
	try:
		colc = a[row+1][col]
	except:
		q = a[row][col+1]
		col += 1
		p = True
	try:
		rowc = a[row][col+1]
	except:
		q = a[row+1][col]
		row += 1
		p = True

	if not p:
		if rowc > colc:
			q = a[row+1][col]
			row += 1
		elif colc > rowc:
			q = a[row][col+1]
			col += 1
		else:
			print "weird error"
			break
	answer += q
	print col, row, colc, rowc, q

print answer

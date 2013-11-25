def isAbundant(number):
  a = []
  for p in range(1,number):
    if number%p==0:
       a.append(p)
  if sum(a) > number:
    return True
  return False


arr = []
for i in range(24, 28124):
	if isAbundant(i):
		arr.append(i)
		print i
print
print "****BREAK****"
print
arrt = []
for i in arr:
	print "*** ",i
	for j in arr:
		if i+j > 28123:
			break
		try:
			arrt.index(i+j)
		except:
			arrt.append(i+j)
			print i+j
print
print "****BREAK****"
print
f = []
for i in range(1,28124):
	try:
		arrt.index(i)
	except:
		f.append(i)
		print i
print f
print sum(f)

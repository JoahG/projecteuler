
def toRoman(n):
	numb = n
	thou = 0
	fhun = 0
	hund = 0
	fift = 0
	ten  = 0
	five = 0
	one  = 0
	if numb >= 1000:
		while numb >= 1000:
			numb -= 1000
			thou += 1
	if numb >= 500:
		while numb >= 500:
			numb -= 500
			fhun += 1
	if numb >= 100:
		while numb >= 100:
			numb -= 100
			hund += 1
	if numb >= 50:
		while numb >= 50:
			numb -= 50
			fift += 1
	if numb >= 10:
		while numb >= 10:
			numb -= 10
			ten += 1
	if numb >= 5:
		while numb >= 5:
			numb -= 5
			five += 1
	if numb >= 1:
		while numb >= 1:
			numb -= 1
			one += 1
	arr = {"M":thou,"D":fhun,"C":hund,"L":fift,"X":ten,"V":five,"I":one}
	t = ""
	for i in arr:
		k = arr[i]
		if k >= 1:
			if k == 1:
				t += i
			else:
				if k >= 1000:
					while k >= 1000:
						k -= 1000
						t += "M"
				if k >= 500:
					while k >= 500:
						k -= 500
						t += "D"
				if k >= 100:
					while k >= 100:
						k -= 100
						t += "C"
				if k >= 50:
					while k >= 50:
						k -= 50
						t += "L"
				if k >= 10:
					while k >= 10:
						k -= 10
						t += "X"
				if k >= 5:
					while k >= 5:
						k -= 5
						t += "V"
				if k >= 1:
					while k >= 1:
						k -= 1
						t += "I"
	return t




print toRoman(16)
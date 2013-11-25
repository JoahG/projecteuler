def div(number):
        i=2
        d = []
        while i<number:
        	if number % i == 0:
        		d.append(i)
        	i+=1
        return d
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
n = 600851475143
i = 2
d = []
while i<n:
        if n % i == 0:
        	j = 2
        	while j<i:
        		if i % j == 0:
        			d.append(i)
        			j+=1
        		else:
        			j+=1
        	 i+=1
        else:
        	i+=1
print d

# ==> 6857
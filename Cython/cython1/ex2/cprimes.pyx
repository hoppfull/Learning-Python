def primes_cy(upto): #Pure python code
	i = 2
	primes = []
	while i <= upto:
		isprime = True
		j = 2
		while j < i:
			if i % j == 0:
				isprime = False
			j = j +1
		if isprime:
			primes.append(i)
		i = i +1
	return primes

def primes(int upto): #Contains three variable type declarations, one on this line
	cdef int i, j #...and two on this line
	i = 2
	primes = []
	while i <= upto:
		isprime = True
		j = 2
		while j < i:
			if i % j == 0:
				isprime = False
			j = j +1
		if isprime:
			primes.append(i)
		i = i +1
	return primes
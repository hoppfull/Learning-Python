def primes_py(upto):
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
import pprimes #Here we import a pure python version of my prime-function
import cprimes #Here we import a file with two cython compiled versions of my prime function
#The first cython compiled function is identical in code to the python, the second contains three int declerations

# print(pprimes.primes_py(12000)) #The pure python version takes 13s to execute with 12000 as value
# print(cprimes.primes_cy(12000)) #The cython compiled pure python version takes 9s to execute with 12000 as value
# print(cprimes.primes(12000)) #The cython compiled version with declerations takes less than a second to execute
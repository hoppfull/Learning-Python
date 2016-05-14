# Implementation of a cheap modulus operator as a C-function: SHIT
#cdef int fstmodulo(int x, int y):
#    cdef int i = 0
#    while i <= x:
#        i += y
#    return ((x - i) + y)

# Implementation of a cheap sqrt operator as a C-function:

cimport libc.math as math  # Using this instead speeded up cython a lot!

#cdef int fstsqrt(int x):
#    cdef int a = 1
#    while (a * a) <= x:
#        a += 1
#    return a

def isPrime(int n):
    cdef int i = 2
    cdef int n_sqrt = <int>math.sqrt(n)
    while i < n_sqrt:
        if n % i == 0:
            return False
        i += 1
    return True

"""What have I learned? (Made in Python 3.4.3 + Cython 0.22)
The for loop is slow in cython. Use while loops instead!
My implementation of the modulus operator sucks! (It's really slow!)
The math C-library is faster than anything I can implement, it seems!
List comprehension in python is much faster than anything I can
implement in Cython in any reasonable amount of time!
"""

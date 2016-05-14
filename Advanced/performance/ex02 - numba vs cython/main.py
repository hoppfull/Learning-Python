import time
import numba as nb
import math
import primes


@nb.jit(nb.boolean(nb.int32),
        nopython=True,
        locals={'i': nb.int32, 'upper': nb.int32})
def isPrime(n):
    i = 2
    upper = int(math.sqrt(n)) + 1
    while i < upper:
        if n % i == 0:
            return False
        i += 1
    return True

n0 = 30000
n1 = 500000

t0 = time.perf_counter()

# Numba function:
a = [p for p in range(1, n1) if isPrime(p)]

t1 = time.perf_counter()

# Cython function:
b = [p for p in range(1, n1) if primes.isPrime(p)]

t2 = time.perf_counter()

print("Numba time:", round((t1-t0)*1000, 1), "ms")
print("Cython time:", round((t2-t1)*1000, 1), "ms")

"""Numba vs Cython
Made with:
Python 3.4.3
Numba 0.18.2
Cython 0.22

Pretty consistent results (30000 loops each):
    Python time: ~115ms
    Numba time: ~9ms
    Cython time: ~6ms
    Scala time: ~8ms
    Clojure+Java: ~10ms
    Java pure: ~5ms

Pretty consistent results (500000 loops each):
    Python time: ~5150ms
    Numba time: ~210ms
    Cython time: ~150ms
    Scala time: ~100ms
    Clojure+Java: ~110ms
    Java pure: ~85ms

Concurrency?
Python: Sure
Numba: Sure
Cython: Sure
Scala: Sure
Clojure+Java: Sure
Java: No

Cython is messy to work with and takes long to get right. However it is
useful for that extra 'edge'. Numba is very fast to work with and easy
to get right!

Compiled Cython will work for anyone. But code with Numba requires user
to have Numba installed (Unless there is some workaround I don't know
about).

This was an experiment in linear computation. I have not yet tried
parallellism and dealing with native data structures. Cython
datastructures do seem to be a bloody mess to work with though.

The primes experiment is interesting becouse it can be made parallell.
It can deal with the case of when you don't know the dimensions of your
data output. But can also be adapted to the case when you do know the
dimensions of your output. There's also not a pure way of calculating
primes today (if there ever will be in mathematics).

What have I learned?
math.sqrt is faster than numpy.sqrt (for a single number atleast)
Supplying type data to the Numba JIT speeds it up quite a bit.
The for-loop is a lot slower than the while-loop in Cython, and only
slightly slower in Numba.
"""

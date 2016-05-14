"""Weak Reference

This is very useful in certain situations!
Basically a weak reference is a reference to an object that will not
prevent the garbage collector from removing it from memory. How does
this work?

If an object has only one strong reference and that reference is
deleted, then it will be removed from memory by the garbage collector.
"""
import weakref

class MyClass:
	def __init__(self, n):
		self.n = n
	def __call__(self):
		return self.n

if __name__ == "__main__":
	a = MyClass(10)
	b = MyClass(5)

	d0 = dict()
	d1 = weakref.WeakValueDictionary()
	
	d0[0] = a
	d1[0] = b
	
	print("Before removal:")
	print("a:\t", d0[0]())
	print("b:\t", d1[0]())
	
	# Delete references:
	del a, b
	
	print("After removal:")
	print("a:\t", d0[0]())
	# print("b:\t", d1[0]()) ## This produces an error!
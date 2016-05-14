"""Bridge Design Pattern (Made in Python 3.4.3)

This reminds me a hell of a lot of the Adapter Pattern!

The point is that the bridge creates a common interface between two
methods, classes, APIs or whatever.
"""

def mul1(x, y):
	# The point isn't how this function is implemented. Only that it's
	# different than mul2.
	result = 0
	for i in range(x):
		result += y
	return result

def mul2(x, y):
	return x * y

class Bridge:
	def __init__(self, algorithm):
		self.algorithm = algorithm
	
	def __call__(self, x, y):
		return self.algorithm(x, y)

if __name__ == "__main__": # Client code:
	mul = Bridge(mul1)
	print(mul(3, 3))
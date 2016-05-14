"""
	This is how we implement getters and setters in Python.
	
	Standard practice in Python is to not worry about client
	code assigning illegal values to fields.
	
	These two classes are supposed to be two examples of
	classes that do the same thing. A demonstration of how
	we can add getters and setters when we need them even
	if client code is already using them. Client code doesn't
	need to change!
"""

class ClassOne:
	# Constructor:
	def __init__(self, x):
		# Public fields accessible by client code:
		self.x = x

class ClassTwo:
	def __init__(self, x):
		# This calls the setX-method:
		self.x = x
	
	def getX(self):
		return self._x
	
	def setX(self, _x):
		if _x < 0: raise ValueError("x cannot be negative!")
		
		self._x = _x
	
	# If client code assigns value to x, setX is called:
	# If client code retrieves value of x, getX is called:
	x = property(getX, setX)
	
# Client code example:
if __name__ == "__main__":
	a = ClassOne(0)
	b = ClassTwo(0)
	# c = ClassTwo(-1) # This raises error
	
	a.x = 5
	b.x = 3
	# b.x = -2 # This raises error
	
	print(a.x)
	print(b.x)
	
	"""
		Notice how client code has not changed with the
		addition of getters and setters! In Java we ass
		getters and setters right away in case we need
		to redefine what client code may and may not do.
		In Python however, we don't have to bother! We
		can change classes and set restrictions later on!
	"""
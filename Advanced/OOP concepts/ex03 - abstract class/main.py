"""
	We don't have the formal abstract classes and interface classes
	from Java in Python. But if we require client code to implement
	a particular function, this is how we do it.
"""

class MyAbstract:	
	def foo(self):
		raise NotImplementedError("Subclasses must implement foo()!")

class MyClass(MyAbstract):
	def __init__(self):
		pass
	
	def foo(self): # Without this implementation of foo(), we get error!
		print("Yay foo is implemented!")

if __name__ == "__main__":
	o = MyClass()
	o.foo()
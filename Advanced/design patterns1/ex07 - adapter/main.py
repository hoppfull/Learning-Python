"""Adapter Design Pattern (Made in Python 3.4.3)

This is pretty cool. The adapter takes an object and creates a new
object with references to the old object except with new names so that
an algorithm that can't distinguish between objects of different
classes may still be able to 'interface' with them.
"""

class MyClass1:
	def foo(self):
		print("Running!")
	
	def bar(self):
		print("Performing!")

class MyClass2:
	def baz(self):
		print("Executing!")

class Adapter:
	def __init__(self, obj, **kwargs):
		self.obj = obj
		self.__dict__.update(kwargs)
	
	def __getattr__(self, method):
		"""This allows us to call methods in the original object. Not
		absolutely important but why not? It's a little pattern in
		itself!"""
		return getattr(self.obj, method)
	
if __name__ == "__main__": # Client code:
	ob0 = MyClass1()
	ob1 = MyClass2()
	
	ob0_adapted = Adapter(ob0, run=ob0.foo, execute=ob0.bar)
	ob1_adapted = Adapter(ob1, run=ob1.baz)
	
	ob0_adapted.run()
	ob0_adapted.foo()
	ob0_adapted.execute()
	
	ob1_adapted.run()
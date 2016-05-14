"""Factory Design Pattern (Made in Python 3.4.3)
http://en.wikipedia.org/wiki/Factory_method_pattern

This is a bit forced in Python. Basically all I'm doing here is
replacing the need to write "object = Class(*args, **kwargs)".
Pretty pointless I think. But here's what I got anyway:

This is my take on the factory design pattern for Python.
This shows that this factory pattern can be extended to create objects
of great complexity and variation.
"""

class MyClass1:
	def run(self):
		print("MyClass1")

class MyClass2:
	def run(self):
		print("MyClass2")

class MyClass3:
	def __init__(self, *args):
		self.args = args
		
	def run(self):
		print("MyClass3", self.args)

if __name__ == "__main__": # Client code:
	 f0 = {'a': MyClass1, "tjosan": MyClass2}
	 f1 = {1: MyClass1, 22: MyClass3}
	 
	 ob0 = f0['a']()
	 
	 ob1 = f0["tjosan"]()
	 
	 ob2 = f1[22]("knatte", "fnatte", "tjatte")
	 
	 ob3 = f1[22](
		f0['a'](),
		f0["tjosan"]()
	 )
	 
	 
	 ob0.run()
	 ob1.run()
	 ob2.run()
	 ob3.run()
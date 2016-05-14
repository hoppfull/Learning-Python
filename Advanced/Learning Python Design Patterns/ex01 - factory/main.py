"""Factory Design Pattern

This is my take on the factory design pattern for Python.
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

if __name__ == "__main__":
	 f0 = {'a': MyClass1, "tjosan": MyClass2}
	 f1 = {1: MyClass1, 22: MyClass3}
	 
	 ob0 = f0['a']()
	 ob1 = f0["tjosan"]()
	 ob2 = f1[22]("knatte", "fnatte", "tjatte")
	 
	 ob0.run()
	 ob1.run()
	 ob2.run()
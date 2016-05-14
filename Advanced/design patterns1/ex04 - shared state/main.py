"""Shared State Pattern (Made in Python 3.4.3)

Not really anything special. Except that we keep the shared state
variable with the MyClass-namespace, we're sure that any python file
containing these objects will also contain this variable.
"""

class MyClass:
	shared_name = None
	def __init__(self, name):
		self.name = name
		MyClass.shared_name = name
		
	def run(self):
		print(self.name, MyClass.shared_name)

if __name__ == "__main__": # Client code:
	ob0 = MyClass("Knatte")
	ob1 = MyClass("Fnatte")
	ob2 = MyClass("Tjatte")
	
	ob0.run()
	ob1.run()
	ob2.run()
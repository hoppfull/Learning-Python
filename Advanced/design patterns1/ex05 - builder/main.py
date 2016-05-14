"""Builder Design Pattern (Made in Python 3.4.3)
http://en.wikipedia.org/wiki/Builder_pattern

This is my interpretation of the builder pattern for Python 3.
Very simple. But also kinda cool! I use the lambda expression. This way
you can design a builder to only be able to change certain properties
later on. One could even create builders of builders this way. Neat!
Combine with factories as well I suppose!
"""

class Composition:
	def __init__(self, c1, c2, name="default"):
		self.name = name
		self.c1 = c1
		self.c2 = c2
	
	def run(self):
		print(self.name, "is running:")
		for i in range(self.c2.n):
			print(self.c1.names)

class Component1:
	def __init__(self, *args):
		self.names = args

class Component2:
	def __init__(self, n):
		self.n = n

if __name__ == "__main__": # Client code:
	builder0 = lambda name: Composition(
		Component1("Knatte", "Fnatte", "Tjatte"),
		Component2(2),
		name=name
	)
	
	builder1 = lambda: Composition(
		Component1("Tripp", "Trapp", "Trull"),
		Component2(3)
	)
	
	builder2 = lambda i: Composition(
		Component1("Snipp", "Snapp", "Slut"),
		Component2(i)
	)
	
	ob0 = builder0("Kalle")
	ob1 = builder0("Kajsa")
	ob2 = builder0("Pluto")
	ob3 = builder1()
	ob4 = builder1()
	ob5 = builder2(7)
	
	ob0.run()
	ob1.run()
	ob2.run()
	ob3.run()
	ob4.run()
	ob5.run()
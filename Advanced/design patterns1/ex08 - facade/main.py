"""Facade Design Pattern (Made in Python 3.4.3)
http://en.wikipedia.org/wiki/Facade_pattern

Very simple pattern. Already used it many times before. Didn't know it
was a common design pattern.

"""
class Part1:
	def foo(self):
		print("foo!")

class Part2:
	def bar(self):
		print("bar!")

class Part3:
	def baz(self):
		print("baz!")

class Facade:
	def __init__(self):
		self.p1 = Part1()
		self.p2 = Part2()
		self.p3 = Part3()
	
	def start(self):
		self.p1.foo()
		self.p2.bar()
		self.p3.baz()
		
if __name__ == "__main__": # Client code:
	facade = Facade()
	facade.start()
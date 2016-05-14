"""Proxy Design Pattern (Made in Python 3.4.3)

This looks a bit like the state pattern. I don't think the proxy
is necessary in Python!
"""

class MyClass:
	def f(self):
		print("F!")
	
	def g(self):
		print("G!")
	
	def h(self):
		print("H!")

class Proxy:
	def __init__(self, obj, access):
		self.obj = obj
		self.access = access
	
	def __getattr__(self, attr):
		if attr in self.access:
			return getattr(self.obj, attr)

if __name__ == "__main__": # Client code:
	proxy = Proxy(MyClass(), ['f', 'g'])
	
	proxy.f()
	proxy.g()
	# proxy.h() ## Error!
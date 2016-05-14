import functools as fp

def debug(func):
	@fp.wraps(func)
	def wrapper(*args, **kwargs):
		print(wrapper.__name__)
		func(*args, **kwargs)
	return wrapper

def debugMethods(cls):
	for key, val in vars(cls).items():
		if callable(val):
			## https://docs.python.org/3.3/library/functions.html#setattr
			setattr(cls, key, debug(val))
	return cls

@debugMethods
class MyClass:
	def method1(self):
		print("Knatte")
	
	def method2(self):
		print("Fnatte")
		
	def method3(self):
		print("Tjatte")
		
ob = MyClass()
ob.method1()
ob.method2()
ob.method3()
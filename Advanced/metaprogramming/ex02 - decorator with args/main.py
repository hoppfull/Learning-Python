import functools as fp

def debug(arg0):
	def decorate(func):
		@fp.wraps(func)
		def wrapper(*args, **kwargs):
			print(arg0)
			func()
		return wrapper
	return decorate

@debug("lolzc")
def myFunction():
	print("Morsning korsning!")

myFunction()
myFunction()
myFunction()
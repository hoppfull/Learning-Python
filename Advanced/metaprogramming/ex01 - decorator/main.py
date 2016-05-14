import functools as fp

def debug(func):
	 # This decorator adds meta data to our new wrapper function
	 # such as name and other kind of information:
	@fp.wraps(func)
	def wrapper(*args, **kwargs):
		print(wrapper.__name__)
		return func(*args, **kwargs)
	return wrapper

@debug
def add(x, y):
	return x + y

@debug
def sub(x, y):
	return x - y

@debug
def mul(x, y):
	return x * y

@debug
def div(x, y):
	return x / y
	
print(add(4, 5))
print(sub(4, 5))
print(mul(4, 5))
print(div(4, 5))
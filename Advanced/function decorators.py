"""
	http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
	"A decorator is just a callable that takes a function as an argument and returns
	a replacement function."
"""

def oldFunction():
	return 1

def myDecorator(func):
	def inner():
		return func() + 1
	
	return inner

newFunction = myDecorator(oldFunction)
# print(newFunction()) # Prints: 2
newFunction = myDecorator(newFunction)
# print(newFunction()) # Prints: 3

"""
	Here we do pretty much the same thing. We decorate our function at definition. So
	it's not the exact same thing as above. But all this should clear up what
	decorators are and how we use them.
"""

@myDecorator
def anotherFunction():
	return 5

# print(anotherFunction()) # Prints: 6

"""
	To create a more general decorator.
"""

def myGeneralDecorator(func):
	def newFunc(*args, **kwargs):
		print(func(*args, **kwargs))
		print(func(*args, **kwargs))
		print(func(*args, **kwargs))
		print("args: ", args)
		print("kwargs: ", kwargs)
	
	return newFunc

@myGeneralDecorator
def myFunc1(x, y, z = "!"):
	return x + y + z
	
myFunc1("bi", "ra", z = "!!")

@myGeneralDecorator
def myFunc2(x, y):
	return x + y

myFunc2("be", "rs")

"""
	Decorators are apparently best equated to LISP macros (awesome!).
"""
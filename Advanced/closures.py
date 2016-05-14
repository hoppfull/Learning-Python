def printer(arg1):
	"""
		Even though 'times' is destroyed when printer() has been called,
		the 'inner' function created remembers what times is. Same goes
		for the argument arg1.
	"""
	times = 3
	def inner():
		for i in range(times): print(arg1)
	
	return inner

greeter = printer("hello")
screamer = printer("AAAAH!")
shouter = printer("HEY!")

greeter()

shouter()

screamer()
class myDecorator:
	def __init__(self, f):
		print("Constructing!")
		self.f = f
	
	def __call__(self):
		print("Calling:", self.f.__name__)
		print(self.f())

@myDecorator
def func():
	return "lolzc"

func()
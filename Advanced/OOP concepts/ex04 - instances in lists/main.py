class MyClassOne:
	def __init__(self):
		self.x = 0

class MyClassTwo:
	def __init__(self):
		self.x = 1

if __name__ == "__main__":
	os = [
		MyClassOne(),
		MyClassOne(),
		MyClassOne(),
		MyClassTwo(),
		MyClassTwo(),
		MyClassTwo()
	]
	
	print(os[3].x)
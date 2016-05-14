class MyClass:
	def __init__(self):
		pass
	
	def getX(self):
		print("getting x!")
		return self._x
	
	def setX(self, _x):
		print("setting x!")
		self._x = _x
	
	x = property(getX, setX)

if __name__ == "__main__":
	o = MyClass()
	o.x = 10
	print(o.x)
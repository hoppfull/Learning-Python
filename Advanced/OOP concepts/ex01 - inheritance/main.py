class MySuper:
	def __init__(self, haha):
		print("This is super code!", haha)

class MySub(MySuper):
	def __init__(self, skratt):
		MySuper.__init__(self, skratt)
		print("This is sub code!")
		
if __name__ == "__main__":
	o = MySub("lolzc")
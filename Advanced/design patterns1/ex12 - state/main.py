"""State Design Pattern (Made in Python 3.4.3)

This pattern allows us to change the behaviour of our object as if it's
changed class. This reminds me a lot of the strategy pattern TBH.
It's quite flexible, as long as client code is constistent with use of
either dictionaries or lists to store states in object.
"""

class StateOne:
	def run(self, value):
		print(value)
	
	def execute(self):
		print("Another function in state1!!")

class StateTwo:
	def run(self):
		print("state2!")

class MyClass:
	def __init__(self, state, states):
		self.state = state
		self.states = states
	
	def __getattr__(self, attr):
		# Called only if MyClass doesn't contain requested attribute
		return getattr(self.states[self.state], attr)
		
		
		
if __name__ == "__main__": # Client code:
	ob0 = MyClass('s1', {'s1':StateOne(), 's2':StateTwo()})
	ob1 = MyClass(0, [StateOne(), StateTwo()])
	
	ob0.run("state1 allows arguments to be passed!")
	ob1.run("yay!")
	
	ob0.execute()
	ob1.execute()
	
	ob0.state = 's2'
	ob1.state = 1
	
	ob0.run()
	ob1.run()
	
	# These will produce errors:
	# ob0.execute() ## Error!
	# ob1.execute() ## Error!
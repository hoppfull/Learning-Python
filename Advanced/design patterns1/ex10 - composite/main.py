"""Composite Design Pattern (Made in Python 3.4.3)

This pattern is a way of organizing hierarchies. The pattern is simple.
But how I implement it is a different story. This might need to be
reworked!
"""

class Leaf: # Contains no children
	def __init__(self, name):
		self.name = name
		self.description = "No description."
	
	def run(self):
		print(self.name + ":\n\t", self.description)

class Group:
	def __init__(self, name):
		self.name = name
		self.description = "No description."
		self.members = {}
	
if __name__ == "__main__": # Client code:
	group0 = Group("Duck Tales")
	group0.description = "Favorite disney characters!"
	group0.members.update({
		'a': Leaf("Knatte"),
		'b': Leaf("Fnatte")
	})
	
	leaf0 = Leaf("Tjatte")
	leaf0.description = "My favorite of the tre little knattarna!"
	
	group0.members.update({
		'c': leaf0
	})
	
	for key in group0.members:
		group0.members[key].run()
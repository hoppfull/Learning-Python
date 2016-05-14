"""Observer Design Pattern (Made in Python 3.4.3)
http://en.wikipedia.org/wiki/Observer_pattern

This is a design pattern in which an object, called "the subject",
maintains a list of its dependents, called "observers", and notifies
them automatically of any state changes. Usually by calling one of
their methods.
"""

class Subject:
	def __init__(self):
		self.os = []
		
	def register(self, o):
		if not o in self.os:
			self.os.append(o)
			return True
		return False
	
	def unregister(self, o):
		if o in self.os:
			del self.os[self.os.index(o)]
			return True
		return False
	
	def notify(self):
		[o.update() for o in self.os]

class Observer:
	def __init__(self, name):
		self.name = name
	
	def update(self):
		print(self.name, "updated!")


if __name__ == "__main__": # Client code:
	
	observer0 = Observer("Knatte")
	observer1 = Observer("Fnatte")
	observer2 = Observer("Tjatte")
	observer3 = Observer("Kalle")
	
	subject = Subject()
	
	print("Registered:", subject.register(observer0))
	print("Registered:", subject.register(observer1))
	print("Registered:", subject.register(observer2))
	print("Unregistered:", subject.unregister(observer3))
	
	print([o.name for o in subject.os])
	
	subject.notify()
"""Command Design Pattern (Made in Python 3.4.3)
http://en.wikipedia.org/wiki/Command_pattern

The command pattern might be unnecessary in Python. We could just
assign a bunch of functions to a list and then execute them in order.

I have not implemented an undo functionality.
"""

class Command:
	# 'Static' method:
	stack = []	
	def __init__(self, command):
		# command must be callable and will be treated as a reference
		self.command = command
	
	def __call__(self):
		# Overrides won't work unless they implement __call__
		raise NotImplementedError

class OverrideCommand1(Command):
	def __call__(self):
		print("OverrideCommand1: ", end="")
		self.command()

class OverrideCommand2(Command):
	def __call__(self):
		print("OverrideCommand2")
		print("\t- ", end="")
		self.command()
		print("\t- ", end="")
		self.command()

if __name__ == "__main__": # Client code:
	# Put some callables in stack:
	Command.stack.append(OverrideCommand1(lambda:print("Knatte")))
	Command.stack.append(OverrideCommand1(lambda:print("Fnatte")))
	Command.stack.append(OverrideCommand1(lambda:print("Tjatte")))
	Command.stack.append(OverrideCommand2(lambda:print("Karl alfred")))
	
	# Run all callables in stack:
	[c() for c in Command.stack]
	
	# Clean stack:
	Command.stack = []
	
	# Put some more callables in stack:
	Command.stack.append(OverrideCommand2(lambda:print("Kalle")))
	Command.stack.append(OverrideCommand2(lambda:print("Joakim")))
	# Run all callables in stack:
	[c() for c in Command.stack]
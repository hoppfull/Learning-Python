"""Strategy Design Pattern

Here we take advantage of closures and the fact
that functions are first class objects in Python.

I personally think this code looks better and is
less uggly. And I believe it allows for more
customization of strategies.
"""

class StratEx:
	def __init__(self, s=None):		
		self.name = "stratex"
		if s:
			self.strategy = s(self)
		
	def strategy(self):
		print(self.name, "uses no strategy.")

	def run(self):
		self.strategy()

def strategyA(self):
	def f():
		print(self.name, "uses StrategyA!")
	
	return f

def strategyB(self):
	def f():
		print(self.name, "uses StrategyB!")
	
	return f

if __name__ == "__main__":
	strat0 = StratEx()
	strat1 = StratEx(strategyA)
	strat2 = StratEx(strategyB)
	
	strat0.run()
	strat1.run()
	strat2.run()
	
	# If we want to change strategy after creation:
	strat0.strategy = strategyA(strat0)
	strat0.run()
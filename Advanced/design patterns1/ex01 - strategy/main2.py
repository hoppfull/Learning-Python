"""Strategy Design Pattern

Here we design strategies as functions but in
this case it's a little confusing why the
default strategy would take two arguments.
While this code is smaller and more suscinct
than the other examples, it looks uglier to me.
"""

class MyClass:
	def __init__(self, strategy=None):
		self.name = "stratex"
		
		if strategy:
			self.strategy = strategy
	
	def run(self):
		self.strategy(self)

	def strategy(self, this):
		print(self.name, "uses no strategy...")

def strategyA(self):
	print(self.name, "uses StrategyA!")

def strategyB(self):
	print(self.name, "uses StrategyB!")

if __name__ == "__main__":
	strat0 = MyClass()
	strat1 = MyClass(strategyA)
	strat2 = MyClass(strategyB)
	
	strat0.run()
	strat1.run()
	strat2.run()
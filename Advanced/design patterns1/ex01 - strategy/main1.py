"""Strategy Design Pattern

Here we design strategies as classes.
"""

class MyClass:
	def __init__(self, strategy=None):
		class BasicStrategy:
			def method1(self, name):
				print("Dummy1", name)
			
			def method2(self, name):
				print("Dummy2", name)
		
		if strategy:
			self.strategy = strategy
		else:
			self.strategy = BasicStrategy()
		
		self.name = "Strategy Example!"
		
	def run(self):
		self.strategy.method1(self.name)
		self.strategy.method2(self.name)

class StrategyA:
	def method1(self, name):
		print("StrategyA, method1:", name)
	
	def method2(self, name):
		print("StrategyA, method2:", name)

class StrategyB:
	def method1(self, name):
		print("StrategyB, method1:", name)
	
	def method2(self, name):
		print("StrategyB, method2:", name)

if __name__ == "__main__":
	strat0 = MyClass()
	strat1 = MyClass(StrategyA())
	strat2 = MyClass(StrategyB())
	
	print("strat0:")
	strat0.run()
	print("strat1:")
	strat1.run()
	print("strat2:")
	strat2.run()
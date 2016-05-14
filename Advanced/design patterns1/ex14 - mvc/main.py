"""MVC Pattern (Made in Python 3.4.3)

"""

DATABASE = {
	'Knatte' : {'a': "tripp", 'b': 1},
	'Fnatte' : {'a': "trapp", 'b': 4},
	'Tjatte' : {'a': "trull", 'b': 3}
}

class Model:
	"""Handles data:
	The model layer communicates with the controller and data storage
	such as a database. The model layer also keeps track of all objects
	created within our application.
	"""
	def __init__(self, data):	
		self.data = data

class View:
	"""Handles presentation:
	The view layer has one-way relationships with the user and the
	controller layer. Recieving information and instructions from the
	controller and renders a presentation to display for the user.
	"""
	def __init__(self):
		self.presentation = "{name}:\n\t{a} was his " \
		+ "friend!\n\tAnd he was {b} years old!"
	
	def displayEntry(self, name, data):
		# The console acts as our graphics layer:
		print(self.presentation.format(
			name=name, a=data['a'], b=data['b'])
		)

class Controller:
	"""Handles decisions:
	The controller layer communicates with the user, the model layer
	and the view layer. It has an exclusive relation ship with the
	model layer, sending and requesting data.
	
	The controller has one-way communication with the view layer,
	sending information to it to tell it what to present.
	"""
	def __init__(self, model, view):
		self.model = model
		self.view = view
	
	def getEntry(self, name):
		entry = self.model.data[name]
		self.view.displayEntry(name, entry)

if __name__ == "__main__": # Client code:
	m = Model(DATABASE)
	v = View()
	c = Controller(m, v)
	
	c.getEntry('Knatte')
	c.getEntry('Fnatte')
	# c.getEntry('Knatte')
import sys #Imported for argv and loading settings.txt
import pygame as pg
import myGameEngine as myGE
import myObjects as myObj


with open(sys.argv[1], 'r') as txt: ##LOADING SETTINGS FROM EXTERNAL FILE!
	exec(txt.read()) #Settings from external file are initialized in variable 'settings'
del txt #Cleanup

class main(myGE.GameEngine):
	def __init__(self):
		self.s = settings
		myGE.GameEngine.__init__(self, self.s['$res'], self.s['$fps'])
		self.force = myObj.Empty()
		self.agent = myObj.Agent()
		self.free = True
		self.screen.fill(self.s["$bg_col"])
		
	def mouseUp(self, button, pos):
		if(button == 1):
			self.force.pos = pos
		if(button == 2):
			self.screen.fill(self.s["$bg_col"])
			
	def mouseMotion(self, buttons, pos, rel):
		if(buttons[0] == 1):
			self.force.pos = pos
		if(buttons[2] == 1):
			self.free = False
			self.agent.pos = pos
			self.agent.velocity = (rel[0]/4, rel[1]/4)
		else:
			self.free = True
		
	def update(self):
		
		i = myGE.get_unitvector((self.force.pos[0] - self.agent.pos[0], self.force.pos[1] - self.agent.pos[1]))
		r = (myGE.get_magnitude((self.force.pos[0] - self.agent.pos[0], self.force.pos[1] - self.agent.pos[1]))/20)**2
		a = myGE.get_force(10, i, r)
		if(self.free):
			self.agent.motion(a)

	def draw(self):
		self.agent.draw(self.screen)
		self.force.draw(self.screen)

myGameObject = main()
myGameObject.mainLoop()
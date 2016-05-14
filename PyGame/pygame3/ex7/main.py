import sys #Imported for argv and loading settings.txt
import pygame as pg
import numpy as np
import myGameEngine as myGE
import myObjects as myObj


with open(sys.argv[1], 'r') as txt: ##LOADING SETTINGS FROM EXTERNAL FILE!
	exec(txt.read()) #Settings from external file are initialized in variable 'settings'
del txt #Cleanup

class main(myGE.GameEngine):
	def __init__(self):
		self.s = settings
		myGE.GameEngine.__init__(self, self.s['$res'], self.s['$fps'])
		
		self.agents = []
		for i in range(30):
			a = myObj.Agent()
			a.pos = np.random.uniform([0,0], self.s['$res'])
			a.target = np.array([self.s['$res'][0]*0.5, self.s['$res'][1]*0.5])
			self.agents.append(a)

	def mouseUp(self, button, pos):
		for agent in self.agents:
			agent.mouse_selection(button, pos)
		
	def update(self):
		for agent in self.agents:
			agent.move_to_target(velocity = 10)
		
		for iterations in range(3):
			myGE.collision(self.agents, 20)
	
	def draw(self):
		self.screen.fill(self.s["$bg_col"])
		for agent in self.agents:
			agent.paint(self.screen)

myGameObject = main()
myGameObject.mainLoop()
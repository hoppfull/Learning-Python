#http://karpathy.ca/phyces/tutorial4.php

import pygame as pg
import myGameEngine as myGE
import sys #Imported for argv and loading settings.txt
import numpy as np

with open(sys.argv[1], 'r') as txt: ##LOADING SETTINGS FROM EXTERNAL FILE!
	exec(txt.read()) #Settings from external file are initialized in variable 'settings'
del txt #Cleanup

class main(myGE.GameEngine):
	def __init__(self):
		self.s = settings
		myGE.GameEngine.__init__(self, self.s['$res'], self.s['$fps'])
		self.icon = self.s['$icon'] #this line can be removed if needed
		self.caption = self.s['$name'] #this line can be removed if needed
		
		self.unit_pos = 0.5*np.array(self.s['$res'])
		self.target_pos = 0.5*np.array(self.s['$res'])
		
	def mouseUp(self, button, pos):
		self.target_pos = pos #Observe the versatility of the numpy array! Jesus christing mcBollockWaffle!
		pass
		
	def mouseMotion(self, buttons, pos, rel):
		if(buttons[0] == 1):
			self.target_pos = pos
		pass

	def update(self):
		u_vec = self.target_pos - self.unit_pos
		if(np.linalg.norm(u_vec) != 0):
			i_coef = 10 / np.linalg.norm(u_vec)
		else:
			i_coef = 0
		if(np.linalg.norm(u_vec) > 5):
			v_vec = u_vec * i_coef
			self.unit_pos = self.unit_pos + v_vec
	
	def draw(self):
		self.screen.fill(self.s["$bg_col"])
		pg.draw.circle(self.screen, (255,0,0), np.around(self.target_pos, 0).astype(int), 30, 1)
		pg.draw.circle(self.screen, (0,0,0), np.around(self.unit_pos, 0).astype(int), 21)
		pg.draw.circle(self.screen, (150,150,150), np.around(self.unit_pos, 0).astype(int), 20)

myGameObject = main()
myGameObject.mainLoop()
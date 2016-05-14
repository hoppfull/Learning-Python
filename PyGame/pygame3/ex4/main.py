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
		
		self.unit_img = pg.image.load(self.s['$u1_img']) ##LOADING 'unit' RESOURCES
		self.unit_size = np.array( pg.Surface.get_size(self.unit_img) )
		self.unit_pos = 0.5*( np.array([self.s['$res'][0], self.s['$res'][1]]) - self.unit_size )
		self.target_img = pg.image.load(self.s['$t1_img']) ##LOADING 'target' RESOURCES
		self.target_size = np.array( pg.Surface.get_size(self.target_img) )
		self.target_pos = 0.5*( np.array([self.s['$res'][0], self.s['$res'][1]]) - self.target_size )
		
	def mouseUp(self, button, pos):
		self.target_pos = pos - 0.5 * self.target_size #Observe the versatility of the numpy array! Jesus christing mcBollockWaffle!
		pass
		
	def mouseMotion(self, buttons, pos, rel):
		pass

	def draw(self):
		self.screen.fill(self.s["$bg_col"])
		self.screen.blit(self.target_img, self.target_pos)
		self.screen.blit(self.unit_img, self.unit_pos)

myGameObject = main()
myGameObject.mainLoop()
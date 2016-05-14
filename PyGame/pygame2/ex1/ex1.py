#These appear to be the absolute basics! But the program can't shut down. It will crash instead.

import pygame as pg
import numpy as np

class myGame:
	def __init__(self, resolution):
		pg.init()
		self.screen = pg.display.set_mode(resolution)
		self.clock = pg.time.Clock()
		
	def mainLoop(self, fps = 40):
		while(True):
			self.clock.tick(fps)

#Definitions:
res = np.array([800, 600])		

#Run program:
myObject = myGame(res)
myObject.mainLoop(40)

print("hello!")
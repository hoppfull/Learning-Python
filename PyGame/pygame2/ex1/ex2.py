#These are the basics + the ability to shut the program down.

import pygame as pg #This is where I get all the pygame stuff
import numpy as np #I import this becouse I'm in love with numpy
from pygame.locals import QUIT #QUIT is a constant (I think) that indicates wether the user is trying to quit the program by pushing the x in the top-right corner of the window

class myGame:
	def __init__(self, settings): #my class takes in one argument, settings
		pg.init() #the pygame program starts with this
		self.settings = settings #copying settings into a global variable with the same name
		self.screen = pg.display.set_mode(( settings["width"], settings["height"] ))
		self.clock = pg.time.Clock()
		self.running = False
		
	def handleEvents(self): #Here we check if the user is trying to quit the program
		for event in pg.event.get():
			if(event.type == QUIT):
				self.running = False
	
	def mainLoop(self):
		self.running = True
		
		while(self.running):
			self.handleEvents()
			self.clock.tick(self.settings["fps"])
			print("tick")

#Definitions: (This might not be the best way to do this but for now, I like it.)
settings = {#A dictionary containing my program specifications
"width"	: 800,				#resolution width
"height"	: 600,				#resolution height
"fps"		: 2					#frames per second
}
#Run program:
myObject = myGame(settings)
myObject.mainLoop()
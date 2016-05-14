#Some extra stuff like caption on top of window and background colour

import pygame as pg #This is where I get all the pygame stuff
import numpy as np #I import this becouse I'm in love with numpy
from pygame.locals import QUIT, KEYUP, K_ESCAPE #QUIT is a constant (I think) that indicates whether the user is trying to quit the program by pushing the x in the top-right corner of the window

class myGame:
	def __init__(self, settings): #my class takes in one argument, settings
		pg.init() #the pygame program starts with this
		self.settings = settings #copying settings into a global variable with the same name
		self.screen = pg.display.set_mode(( settings["width"], settings["height"] ))
		self.screen.fill(settings["bg_col"])
		pg.display.set_caption(self.settings["name"])
		pg.display.flip() #this paints the current composition (my own terminology here) onto the surface
		
		self.clock = pg.time.Clock()
		self.running = False
		
		
	def mainLoop(self):
		self.running = True
		while(self.running):
			self.handleEvents()
			self.draw()
			pg.display.flip()
			self.clock.tick(self.settings["fps"])
			
	def handleEvents(self): #This is used to check for user input
		for event in pg.event.get():
			if(event.type == QUIT): #Here we check if the user is trying to close the program with the x in the top right corner of the window
				self.running = False
			elif(event.type == KEYUP and event.key == K_ESCAPE): #This is strange. Apparently event.key cannot be checked on its own. Only after event.type == KEYUP is checked. Not slightly before even. Only after! Wierd...
				self.running = False #Here we check if the user is pressing escape in order to close the program
				
	def draw(self):
		self.screen.fill((0,200,255)) #This is overriding the background colour originally initiated
	

#Definitions: (This might not be the best way to do this but for now, I like it.)
settings = {#A dictionary containing my program specifications
"name"	: "myProgram",	#caption on top of program window
"width"	: 800,					#resolution width
"height"	: 600,					#resolution height
"fps"		: 30,						#frames per second
"bg_col"	: (255,100,50)	#the background colour
}

#Run program:
myObject = myGame(settings)
myObject.mainLoop()
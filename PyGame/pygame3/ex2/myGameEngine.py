import pygame as pg
from pygame.locals import KEYUP, K_ESCAPE, QUIT

class GameEngine:
	def __init__(self, size = (640, 480), fps = 1):
		pg.init()
		self.size, self.fps = size, fps
		self.screen = pg.display.set_mode(self.size)
		
		self.running = False
		
	def mainLoop(self):
		self.running = True
		while(self.running):
			self.handleEvents()
			self.console()
			self.draw()
			pg.display.flip()
			pg.time.Clock().tick(self.fps)
	
	def handleEvents(self):
		for events in pg.event.get():
			if(events.type == KEYUP and events.key == K_ESCAPE):
				self.running = False
			elif(events.type == QUIT) :
				self.running = False

	def console(self):
		pass
		
	def draw(self):
		pass
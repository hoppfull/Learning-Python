import pygame as pg
from pygame.locals import KEYUP, K_ESCAPE

class GameEngine:
	def __init__(self, w = 640, h = 480, fps = 1):
		pg.init()
		self.w, self.h, self.fps = w, h, fps
		self.screen = pg.display.set_mode((self.w, self.h))
		
		self.running = False
		
	def mainLoop(self):
		self.running = True
		while(self.running):
			self.handleEvents()
	
	def handleEvents(self):
		for events in pg.event.get():
			if(events.type == KEYUP and events.key == K_ESCAPE):
				self.running = False
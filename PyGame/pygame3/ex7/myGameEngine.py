import pygame as pg
import numpy as np
from pygame.locals import KEYUP, K_ESCAPE, QUIT, MOUSEBUTTONUP, MOUSEMOTION

class GameEngine:
	def __init__(self, size = (640, 480), fps = 1):
		pg.init()
		self.size, self.fps = size, fps
		self.screen = pg.display.set_mode(self.size)
		
		self.running = True
		
	def mainLoop(self):
		while(self.running):
			self.inputEvents()
			self.update()
			self.draw()
			pg.display.flip()
			pg.time.Clock().tick(self.fps)
	
	def inputEvents(self):
		for events in pg.event.get():
			if(events.type == QUIT): #trigger if user press the x on the top right corner of the program window
				self.running = False
			elif(events.type == KEYUP and events.key == K_ESCAPE): #trigger if user press escape
				self.running = False
			elif(events.type == MOUSEBUTTONUP): #trigger if user press any mousebutton and if user move the mouse
				self.mouseUp(events.button, events.pos)
			elif(events.type == MOUSEMOTION): #trigger if user press and hold any mousebutton while and if the user move the mouse
				self.mouseMotion(events.buttons, events.pos, events.rel)
		
	def mouseUp(self, button, pos):
		pass
	
	def mouseMotion(self, buttons, pos, rel):
		pass
		
	def update(self):
		pass
	
	def draw(self):
		pass

def collision(actors, radius):
	for a1 in actors:
		for a2 in actors:
			if(a1 == a2): continue
			distance = np.linalg.norm(a2.pos - a1.pos)
			if(distance > 45): continue
			if(distance <= radius*2):
				adjustment = radius - distance/2
				direction = a2.pos - a1.pos
				if(a1.selected):
					a2.pos = a2.pos + (2 * adjustment * direction / np.linalg.norm(direction))
				elif(a2.selected):
					a1.pos = a1.pos - (2 * adjustment * direction / np.linalg.norm(direction))
				elif(not(a1.selected or a2.selected)):
					a1.pos = a1.pos - (adjustment * direction / np.linalg.norm(direction))
					a2.pos = a2.pos + (adjustment * direction / np.linalg.norm(direction))
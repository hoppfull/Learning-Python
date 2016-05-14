import pygame as pg
import numpy as np

class Agent:
	def __init__(self):
		self.pos = (0,0)
		self.velocity = (0,0)
	
	def motion(self, acceleration = (0,0)):
		if(acceleration != (0,0)):
			self.velocity = (self.velocity[0] + acceleration[0], self.velocity[1] + acceleration[1])
		self. pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
		
	def draw(self, surface):
		surface.fill((200,150,20), (self.pos, (1,1)))
		
class Empty: 
	def __init__(self):
		self.pos = (0,0)
		
	def draw(self, surface):
		pg.draw.circle(surface, (0,0,255), np.around(self.pos).astype(int), 5, 1)
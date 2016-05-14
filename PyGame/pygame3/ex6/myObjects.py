import pygame as pg
import numpy as np

class Agent:
	def __init__(self):
		self.pos = np.array([100,100]) #Default value
		self.target = self.pos
		self.selected = False #Default value
		self.fill = (50,50,50) #Default value
		
	def mouse_selection(self, button, pos):
		pos = np.array(pos)
		if(button == 1 and (  np.linalg.norm(self.pos - pos) < 21  )):
			self.selected = True #Select
		elif(button == 1 and (  np.linalg.norm(self.pos - pos) > 21 )):
			self.selected = False #Deselect
		if(button == 3 and self.selected == True): #Target manipulation:
			self.target = pos
			
	def move_to_target(self, velocity = 1):
		delta = self.target - self.pos
		if(np.linalg.norm(delta) > velocity):
			self.pos = self.pos + delta * velocity/np.linalg.norm(delta)
		elif(np.linalg.norm(delta) <= velocity):
			self.pos = self.target
		
	def paint(self, canvas):
		if(self.selected):
			self.fill = (220,255,220)
			pg.draw.circle(canvas, (200,0,0), np.around(self.target, 0).astype(int), 30, 1)
		else:
			self.fill = (200,200,200)
			
		pg.draw.circle(canvas, (0,0,0),  np.around(self.pos, 0).astype(int), 21)
		pg.draw.circle(canvas, self.fill,  np.around(self.pos, 0).astype(int), 20)
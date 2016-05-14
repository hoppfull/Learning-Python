import pygame as pg
import pygame.locals as pg_locals

import OpenGL.GL as GL

class App:
	def __init__(self, title="PyGame Window", w=640, h=480, fps=30):
		self.size = (w, h)
		self.title = title
		self.fps = fps
	
	def start(self):
		pg.init()
		self.screen = pg.display.set_mode(self.size, pg_locals.HWSURFACE|pg_locals.OPENGL|pg_locals.DOUBLEBUF)
		pg.display.set_caption(self.title)
		GL.glClearColor(0.4, 0.4, 0.4, 0.0) # Set background color
		
		self.clock = pg.time.Clock()
		self.mainLoop()
	
	def mainLoop(self):
		self.running = True
		while self.running:
			# Handle events for this loop first:
			self.events()
			# Apply drawing to screen:
			self.draw()
			# Set target frames per seconds:
			self.clock.tick(self.fps)
	
	def draw(self):
		 # Clear window:
		GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
		# Draw everything onto screen:
		pg.display.flip()
	
	def events(self): # Here we handle all user input:
		for e in pg.event.get():
			if(e.type == pg_locals.KEYUP and e.key == pg_locals.K_ESCAPE):
				self.running = False
			if e.type == pg.QUIT:
				self.running = False
	
if __name__ == "__main__":
	app = App("Hello window! Press 'ESC' to close!", 800, 600, 30)
	app.start()
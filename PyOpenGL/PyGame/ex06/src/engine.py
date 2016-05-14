import pygame as pg
import pygame.locals as pg_locals

import OpenGL.GL as GL

class Engine:
	def __init__(self, title="PyGame Window", width=640, height=480, fps=30):
		self.screen_size = (width, height)
		self.title = title
		self.fps = fps
	
	def start(self):
		pg.init()
		self.screen = pg.display.set_mode(self.screen_size, pg_locals.HWSURFACE|pg_locals.OPENGL|pg_locals.DOUBLEBUF)
		pg.display.set_caption(self.title)
		
		GL.glEnable(GL.GL_CULL_FACE) # This isn't enabled by default
		GL.glFrontFace(GL.GL_CCW) # Standard, right hand rule
		GL.glCullFace(GL.GL_BACK) # This will increase performance
		GL.glEnable(GL.GL_DEPTH_TEST)
		GL.glEnable(GL.GL_STENCIL_TEST)
		
		
		# Run initialization for this session:
		self.setupSession()
		
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
		GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT | GL.GL_STENCIL_BUFFER_BIT)
		
		# Do stuff specific to session:
		self.runningSession()
		
		# Draw everything onto screen:
		pg.display.flip()
	
	def events(self): # Here we handle all user input:
		pass
	
	def setupSession(self):
		pass
	
	def runningSession(self):
		pass
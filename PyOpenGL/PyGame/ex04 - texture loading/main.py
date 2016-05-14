import numpy as np
import ctypes as c

import pygame as pg

import OpenGL.GL as GL
import OpenGL.GL.shaders as GL_shaders

import src.engine as eng
import src.resources as res
import src.mathematics as mthmtx

class App(eng.Engine):
	def __init__(self, title, w, h, fps):
		eng.Engine.__init__(self, title=title, width=w, height=h, fps=fps)
		self.screen_size = (w, h)
	
	def events(self):
		for e in pg.event.get():
			if e.type == pg.QUIT:
				# When quitting window:
				self.running = False
				
			elif e.type == pg.KEYUP and e.key == pg.K_ESCAPE:
				# When releasing escape key:
				self.running = False
			
			elif e.type == pg.MOUSEMOTION:
				if e.buttons[2] == 1:
					# If right mouse button is held while moving mouse up and down:
					self.ViewMatrix.approachTarget(-0.01*e.rel[1])
				if e.buttons[1] == 1:
					# If middle mouse button is held while moving mouse:
					self.ViewMatrix.orbitTarget(e.rel)
			
	def setupSession(self):
		GL.glClearColor(0.4, 0.4, 0.4, 0.0) # Set background color
		self.shader = res.loadShader("res/vertexshader.glsl", "res/fragmentshader.glsl")
		
		self.UNIFORMS = {
            'my_ModelMatrix':GL.glGetUniformLocation(self.shader, 'my_ModelMatrix'),
            'my_ViewMatrix':GL.glGetUniformLocation(self.shader, 'my_ViewMatrix'),
            'my_ProjectionMatrix':GL.glGetUniformLocation(self.shader, 'my_ProjectionMatrix'),
            'tex0':GL.glGetUniformLocation(self.shader, 'tex0'),
            'tex1':GL.glGetUniformLocation(self.shader, 'tex1')}
		
		self.myModel = res.model("res/plane.npz")
		self.myTexture2D = res.texture2D("res/tex0.png")
		self.whatevs = res.texture2D("res/tex1.png")
		
		# Setup a model matrix with initial position:
		self.ModelMatrix = mthmtx.ModelMatrix(mthmtx.vec3(0, 0, 0))
		# Setup a view matrix with initial perspective position:
		self.ViewMatrix = mthmtx.ViewMatrix(mthmtx.vec3(0, -8, 3))
		# Set view matrix to look at target coordinates (1st arg) and a vector defined as view up direction (2nd arg):
		self.ViewMatrix.lookAt(mthmtx.vec3(0, 0, 0), mthmtx.vec3(0, 0, 1))
		# Setup a projection matrix with parameters, screen size, near clipping plane,
		# far clipping plane, field of view in turns (1.0 will let you see a full 360 degree field of view):
		self.ProjectionMatrix = mthmtx.ProjectionMatrix(self.screen_size, 0.1, 100, 0.3)
	
	def runningSession(self):
		try:
			GL_shaders.glUseProgram(self.shader)
			self.myTexture2D.bind(0) # Passed an id which is also passed to shader via uniforms
			self.whatevs.bind(1)
			self.myModel.bind()
			
			GL.glUniformMatrix4fv(
				self.UNIFORMS['my_ModelMatrix'],1, GL.GL_TRUE,
				self.ModelMatrix.get())
            
			GL.glUniformMatrix4fv(
				self.UNIFORMS['my_ViewMatrix'],1, GL.GL_TRUE,
				self.ViewMatrix.get())
            
			GL.glUniformMatrix4fv(
				self.UNIFORMS['my_ProjectionMatrix'],1, GL.GL_TRUE,
				self.ProjectionMatrix.get())
			
			GL.glUniform1i(self.UNIFORMS['tex0'], 0) # same id as passed to texture2D.bind()
			GL.glUniform1i(self.UNIFORMS['tex1'], 1)
		finally:
			self.myModel.unbind()
			self.whatevs.unbind()
			self.myTexture2D.unbind()
			GL_shaders.glUseProgram(0)
	
if __name__ == "__main__":
	app = App("Hello window! Press 'ESC' to close!", 800, 600, 30)
	app.start()
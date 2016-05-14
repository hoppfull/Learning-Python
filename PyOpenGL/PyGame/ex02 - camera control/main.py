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
				if e.buttons[0] == 1 and e.buttons[2] == 1:
					# If left and right mouse buttons are held while moving mouse up and down:
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
            'my_ProjectionMatrix':GL.glGetUniformLocation(self.shader, 'my_ProjectionMatrix')}
		
		self.vertex_data = np.array([
			[-1.0, 1.0, 0.0],
			[-1.0,-1.0, 0.0],
			[ 1.0,-1.0, 0.0],
			[ 1.0, 1.0, 0.0]
			], dtype=np.float32)
			
		self.index_data = np.array([
			[0, 1, 2],
			[0, 2, 3]
			], dtype=np.uint32)
		
		self.vbo = GL.glGenBuffers(1)
		self.ibo = GL.glGenBuffers(1)
		
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo) # Select self.vbo
		GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertex_data, GL.GL_STATIC_DRAW) # Assign data to selected buffer
		
		GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ibo) # Select self.ibo
		GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, self.index_data, GL.GL_STATIC_DRAW) # Assign data to selected buffer
		
		GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0) # Deselect buffers
		
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
			GL_shaders.glUseProgram(self.shader) ##TODO: revise handling of shaders - objects?
			
			GL.glUniformMatrix4fv(
				self.UNIFORMS['my_ModelMatrix'],1, GL.GL_TRUE,
				self.ModelMatrix.get())
            
			GL.glUniformMatrix4fv(
				self.UNIFORMS['my_ViewMatrix'],1, GL.GL_TRUE,
				self.ViewMatrix.get())
            
			GL.glUniformMatrix4fv(
				self.UNIFORMS['my_ProjectionMatrix'],1, GL.GL_TRUE,
				self.ProjectionMatrix.get())
			try:
				GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
				
				GL.glVertexAttribPointer( # Vertex data
					0,                  # Attribute 0 in this attribute array
					3,                  # This attribute uses 3 elements
					GL.GL_FLOAT,        # These values are of type "GL_FLOAT"
					False,              # Normalize values? No!
					self.vertex_data.shape[1]*c.sizeof(c.c_float), # bits per row, 4 bits for floats, 6 elements in one row (doubles are 8)
					c.c_void_p(0))               # Where in each row does attribute start?
				GL.glEnableVertexAttribArray(0)

				GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ibo)
				GL.glDrawElements(
					GL.GL_TRIANGLES,
					self.index_data.size,
					GL.GL_UNSIGNED_INT, c.c_void_p(0))
			finally:
				GL.glDisableVertexAttribArray(0)
				GL.glDisableVertexAttribArray(1)
				GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
		finally:
			GL_shaders.glUseProgram(0)
	
if __name__ == "__main__":
	app = App("Hello window! Press 'ESC' to close!", 800, 600, 30)
	app.start()
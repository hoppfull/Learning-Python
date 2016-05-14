import pygame as pg

import OpenGL.GL as GL
import OpenGL.GL.shaders as GL_shaders

import src.engine as eng
import src.resources as res
import src.mathematics as mthmtx

class App(eng.Engine):
	def __init__(self, title, w, h, fps):
		eng.Engine.__init__(self, title=title, width=w, height=h, fps=fps)
	
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
		GL.glClearColor(0.3, 0.7, 0.3, 0.0) # Set background color
		self.shaderOpaque = res.loadShader("res/shaders/vs_opaque.glsl", "res/shaders/fs_opaque.glsl")
		self.shaderTranslucent = res.loadShader("res/shaders/vs_translucent.glsl", "res/shaders/fs_translucent.glsl")
		self.shaderComposition = res.loadShader("res/shaders/vs_composition.glsl", "res/shaders/fs_composition.glsl")
		
		self.UNIFORMSOpaque = {
            'my_ModelMatrix':GL.glGetUniformLocation(self.shaderOpaque, 'my_ModelMatrix'),
            'my_ViewMatrix':GL.glGetUniformLocation(self.shaderOpaque, 'my_ViewMatrix'),
            'my_ProjectionMatrix':GL.glGetUniformLocation(self.shaderOpaque, 'my_ProjectionMatrix'),
            'tex0':GL.glGetUniformLocation(self.shaderOpaque, 'tex0')}
			
		self.UNIFORMSTranslucent = {
            'my_ModelMatrix':GL.glGetUniformLocation(self.shaderTranslucent, 'my_ModelMatrix'),
            'my_ViewMatrix':GL.glGetUniformLocation(self.shaderTranslucent, 'my_ViewMatrix'),
            'my_ProjectionMatrix':GL.glGetUniformLocation(self.shaderTranslucent, 'my_ProjectionMatrix'),
            'tex0':GL.glGetUniformLocation(self.shaderTranslucent, 'tex0')}
		
		self.UNIFORMSComposition = {
            'tex0':GL.glGetUniformLocation(self.shaderComposition, 'tex0'),
            'tex1':GL.glGetUniformLocation(self.shaderComposition, 'tex1')}
		
		self.model1 = res.model("res/models/disc1.npz")
		self.model2 = res.model("res/models/suzanne.npz")
		self.canvas = res.model("res/models/screen.npz")
		self.tex1 = res.texture2D("res/textures/transparancy.png")
		
		self.ModelMatrix = mthmtx.ModelMatrix(mthmtx.vec3(0, 0, 0))
		self.ViewMatrix = mthmtx.ViewMatrix(mthmtx.vec3(3, -6, 3))
		self.ViewMatrix.lookAt(mthmtx.vec3(0, 0, 0), mthmtx.vec3(0, 0, 1))
		self.ProjectionMatrix = mthmtx.ProjectionMatrix(self.screen_size, 0.1, 100, 0.3)
		
		self.setupOpaque()
		self.setupTranslucent()
	
	def renderComposition(self):
		try:
			GL_shaders.glUseProgram(self.shaderComposition)
			GL.glActiveTexture(GL.GL_TEXTURE0 + 0)
			GL.glBindTexture(GL.GL_TEXTURE_2D, self.opaqueDEPTHtex)
			GL.glActiveTexture(GL.GL_TEXTURE0 + 1)
			GL.glBindTexture(GL.GL_TEXTURE_2D, self.translucentDEPTHtex)
			self.canvas.bind()
			
			GL.glUniform1i(self.UNIFORMSComposition['tex0'], 0)
			GL.glUniform1i(self.UNIFORMSComposition['tex1'], 1)
		finally:
			self.canvas.unbind()
			GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
			GL_shaders.glUseProgram(0)
	
	def setupOpaque(self):
		self.opaqueFBO = GL.glGenFramebuffers(1)
		GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.opaqueFBO)
		
		self.opaqueDEPTHtex = GL.glGenTextures(1)
		GL.glBindTexture(GL.GL_TEXTURE_2D, self.opaqueDEPTHtex)
		GL.glTexStorage2D(
			GL.GL_TEXTURE_2D, 1,
			GL.GL_DEPTH_COMPONENT32F,
			self.screen_size[0],
			self.screen_size[1])
		
		GL.glFramebufferTexture(
			GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT,
			self.opaqueDEPTHtex, 0)
			
		GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
		GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
	
	def setupTranslucent(self):
		self.translucentFBO = GL.glGenFramebuffers(1)
		GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.translucentFBO)
		
		self.translucentDEPTHtex = GL.glGenTextures(1)
		GL.glBindTexture(GL.GL_TEXTURE_2D, self.translucentDEPTHtex)
		GL.glTexStorage2D(
			GL.GL_TEXTURE_2D, 1,
			GL.GL_DEPTH_COMPONENT32F,
			self.screen_size[0],
			self.screen_size[1])
		
		GL.glFramebufferTexture(
			GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT,
			self.translucentDEPTHtex, 0)
			
		GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
		GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
	
	def renderOpaque(self):
		try:
			GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.opaqueFBO)
			GL.glClearBufferfv(GL.GL_DEPTH, 0, 1)
			GL_shaders.glUseProgram(self.shaderOpaque)
			self.tex1.bind(0)
			self.model1.bind()
			
			GL.glUniformMatrix4fv(
					self.UNIFORMSOpaque['my_ModelMatrix'],1, GL.GL_TRUE,
					self.ModelMatrix.get())
				
			GL.glUniformMatrix4fv(
				self.UNIFORMSOpaque['my_ViewMatrix'],1, GL.GL_TRUE,
				self.ViewMatrix.get())
			
			GL.glUniformMatrix4fv(
				self.UNIFORMSOpaque['my_ProjectionMatrix'],1, GL.GL_TRUE,
				self.ProjectionMatrix.get())
			
			GL.glUniform1i(self.UNIFORMSOpaque['tex0'], 0)
		finally:
			self.model1.unbind()
			self.tex1.unbind()
			GL_shaders.glUseProgram(0)
			GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
	
	def renderTranslucent(self):
		try:
			GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.translucentFBO)
			GL.glClearBufferfv(GL.GL_DEPTH, 0, 1)
			GL_shaders.glUseProgram(self.shaderTranslucent)
			self.tex1.bind(0)
			self.model2.bind()
			
			GL.glUniformMatrix4fv(
					self.UNIFORMSTranslucent['my_ModelMatrix'],1, GL.GL_TRUE,
					self.ModelMatrix.get())
				
			GL.glUniformMatrix4fv(
				self.UNIFORMSTranslucent['my_ViewMatrix'],1, GL.GL_TRUE,
				self.ViewMatrix.get())
			
			GL.glUniformMatrix4fv(
				self.UNIFORMSTranslucent['my_ProjectionMatrix'],1, GL.GL_TRUE,
				self.ProjectionMatrix.get())
			
			GL.glUniform1i(self.UNIFORMSTranslucent['tex0'], 0)
		finally:
			self.model2.unbind()
			self.tex1.unbind()
			GL_shaders.glUseProgram(0)
			GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
		
	def runningSession(self):
		self.renderOpaque()
		self.renderTranslucent()
		self.renderComposition()
	
if __name__ == "__main__":
	app = App("Galaxy", 800, 600, 30)
	app.start()
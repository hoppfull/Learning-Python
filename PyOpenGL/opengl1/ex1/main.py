import OpenGL.GL as GL
import OpenGL.GL.shaders as GLshaders
import OpenGL.arrays.vbo as GLvbo

import pygame as pg
import pygame.locals as pglocals

import numpy as np

class main:
    def __init__(self):
        pg.init()
        pg.display.set_mode((480,320), pg.OPENGL|pg.DOUBLEBUF)
        self.running = True
        
        self.myTriangle = np.array([
            [ 0, 1, 0],
            [-1, 0, 0],
            [ 1, 0, 0]
        ], dtype='f')
        
        VERTEX_SHADER = GLshaders.compileShader("""#version 120
        void main(){
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }""", GL.GL_VERTEX_SHADER)
        FRAGMENT_SHADER = GLshaders.compileShader("""#version 120
        void main(){
            gl_FragColor = vec4(0.2, 1.0, 1.0, 1.0);
        }""", GL.GL_FRAGMENT_SHADER)
        
        self.myShader = GLshaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
    
    def inputEvents(self):
        for events in pg.event.get():
            if events.type == pglocals.QUIT:
                self.running = False
                
    def updateScene(self):
        pass
    
    def drawScene(self):
        vbo = GLvbo.VBO(self.myTriangle)
        #The vbo cannot be 'selfed' or we get problems with dumping memory. But since the layout
        #of vertices are expected to change, this has to be loaded every frame anyway. So no reason
        #to 'self' it!
        
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GLshaders.glUseProgram(self.myShader)
        try: 
            vbo.bind()
            try:
                GL.glEnableClientState(GL.GL_VERTEX_ARRAY)
                GL.glVertexPointerf(vbo)
                GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
            finally:
                vbo.unbind()
                GL.glDisableClientState(GL.GL_VERTEX_ARRAY)
        finally:
            GLshaders.glUseProgram(0)
        
    def mainLoop(self):
        while self.running:
            self.inputEvents()
            self.updateScene()
            self.drawScene()
            pg.display.flip()
            pg.time.Clock().tick(40)


if __name__ == "__main__":
    object = main()
    object.mainLoop()
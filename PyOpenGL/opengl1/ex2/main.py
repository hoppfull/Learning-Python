import OpenGL.GL as GL
import OpenGL.GL.shaders as GLshaders
import OpenGL.arrays.vbo as GLvbo

import pygame as pg
import numpy as np

#I split up my code into several files to make things less cluttered
#I will also try to keep it standard practice not to make code too
#unclear and nested. I'll try to branch as much as possible from one point.
#I hate it when I try to understand someone elses code and it goes down
#a rabbit hole that branches into several directions and never seem to end.
import myGLEngine as myGE

class main(myGE.GLEngine):
    def __init__(self):
        myGE.GLEngine.__init__(self, resolution=(640,480), maxfps=25)
        
        self.myTriangle = np.array([ #The following are vertex coordinates
            [ 0, 1, 0],
            [-1, 0, 0],
            [ 1, 0, 0]
        ], dtype='f')
    
    def updateScene(self):
        #Here we change things like logic, physics and properties.
        #Additionally, I believe this code should actually be executed in
        #in as much cython as possible to increase performance!
        pass
    
    def drawScene(self):
        #This is where we change graphics. Things in here won't actually be applied right away
        #to the canvas. So when this function is done, drawing will be applied right after.
        
        vbo = GLvbo.VBO(self.myTriangle)
        #The vertex-buffer-object has to stay in here since
        #it cannot be "selfed" or we get errors
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
    
if __name__ == "__main__":
    myGameObject = main()
    myGameObject.mainLoop()
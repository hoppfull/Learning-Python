import OpenGL.GL as GL
import OpenGL.GL.shaders as GLshaders
import OpenGL.arrays.vbo as GLvbo

import numpy as np

import OpenGLContext.testingcontext as GLCtc

BaseContext = GLCtc.getInteractive()

class TestContext(BaseContext):
    def OnInit(self):
        VERTEX_SHADER = GLshaders.compileShader("""#version 120
        void main(){
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }""", GL.GL_VERTEX_SHADER) #Defining the vertex shader
        
        FRAGMENT_SHADER = GLshaders.compileShader("""#version 120
        void main(){
            gl_FragColor = vec4(0.2,1,0.5,1);
        }""", GL.GL_FRAGMENT_SHADER) #Defining the fragment shader
        
        myTriangle = np.array([
            [ 0, 2, 0],
            [-1, 0, 0],
            [ 1, 0, 0]
        ], dtype='f')
        
        self.myShader = GLshaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)
        self.vbo = GLvbo.VBO(myTriangle)
        
    def Render(self, mode):
        GLshaders.glUseProgram(self.myShader)
        try:
            self.vbo.bind()
            try:
                GL.glEnableClientState(GL.GL_VERTEX_ARRAY)
                GL.glVertexPointerf(self.vbo)
                GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
            finally:
                self.vbo.unbind()
                GL.glDisableClientState(GL.GL_VERTEX_ARRAY)
        finally:
            GLshaders.glUseProgram(0)

if __name__ == "__main__":
    TestContext.ContextMainLoop()
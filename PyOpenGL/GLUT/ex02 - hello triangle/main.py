import OpenGL.GLUT as GLUT
import OpenGL.GL as GL
import OpenGL.arrays.vbo as GL_vbo
import OpenGL.GL.shaders as GL_shaders
import sys
import numpy as np

class Window():
    def __init__(self, name, width, height):
        self.width = width
        self.height = height
        self.name = name
        # Create window:
        GLUT.glutInit()
        GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA | GLUT.GLUT_DOUBLE | GLUT.GLUT_DEPTH)
        GLUT.glutInitWindowSize(self.width, self.height)
        
    def run(self):
        # Create window:
        self.win = GLUT.glutCreateWindow(self.name)
        
        # Setup stuff for testing this time:
        self.mySetup()
        
        # Create update mechanism:
        GLUT.glutTimerFunc(30, self.update, 30)
        self.initOpenGL()
        
        # Create redraw mechanism:
        GLUT.glutDisplayFunc(self.draw)
        GLUT.glutMainLoop()
    
    def mySetup(self):
        # Get shader program:
        self.shader = self.loadShader("vertexshader.glsl", "fragmentshader.glsl")
        # Store geometry data to be pushed to the GPU later:
        self.vbo = GL_vbo.VBO(
                np.array([ # Convenient it can take a numpy array!
                [ 0.0, 1.0, 0.0],
                [-1.0,-1.0, 0.0],
                [ 1.0,-1.0, 0.0]
                ],'f'))
            
        
    def render(self):
        GL_shaders.glUseProgram(self.shader)
        try:
            self.vbo.bind()
            try:
                GL.glEnableClientState(GL.GL_VERTEX_ARRAY)
                GL.glVertexPointerf(self.vbo)
            
                # Draw triangles, start at 0 in vbo and continue for 3 entries (one triangle!)
                GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
            finally:
                self.vbo.unbind()
                GL.glDisableClientState(GL.GL_VERTEX_ARRAY)
        finally:
            GL_shaders.glUseProgram(0)
        
    
    def update(self, t):
        # Schedule next update:
        GLUT.glutTimerFunc(t, self.update, t)
        # Run "GLUT.glutDisplayFunc(self.draw)":
        GLUT.glutPostRedisplay()
    
    def draw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Clear window
        # Draw commands go here:
        self.render()
        
        GLUT.glutSwapBuffers() # Apply update to window
        
    def initOpenGL(self):
        pass
    
    def loadShader(self, vs, fs):
        # Load vertex shader file and compile:
        with open(vs, 'r') as vs_file:
            VERTEX_SHADER = GL_shaders.compileShader(
                vs_file.read(),
                GL.GL_VERTEX_SHADER)
        del vs_file; # Delete file object, good programming practice
        # Load fragment shader file and compile:
        with open(fs, 'r') as fs_file:
            FRAGMENT_SHADER = GL_shaders.compileShader(
                fs_file.read(),
                GL.GL_FRAGMENT_SHADER)
        del fs_file; # Delete file object, good programming practice
        # Compile and return shader program:
        return GL_shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
        
        
    
if __name__ == "__main__":
    w = Window("OpenGL", 640, 480)
    w.run()
import OpenGL.GLUT as GLUT
import OpenGL.GL as GL
import OpenGL.arrays.vbo as GL_vbo
import OpenGL.GL.shaders as GL_shaders
import OpenGL.GL.EXT.texture_compression_s3tc as GL_s3tc
import PIL.Image as PIL_Image
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
        self.vbo = GL_vbo.VBO( ##TODO: create a model loading mechanism!
            np.array([ # Convenient it can take a numpy array!
            [ 1.0, 1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 0.0],
            [-1.0, 1.0, 0.0,   0.0, 0.0, 0.0,   0.0, 0.0],
            [-1.0,-1.0, 0.0,   0.0, 0.0, 0.0,   0.0, 1.0],
            [ 1.0,-1.0, 0.0,   0.0, 0.0, 0.0,   1.0, 1.0]
            ],dtype=np.float32), target=GL.GL_ARRAY_BUFFER)
        
        self.ibo = GL_vbo.VBO(
            np.array([
            [0, 1, 3],
            [1, 2, 3]
            ],dtype=np.uint32), target=GL.GL_ELEMENT_ARRAY_BUFFER)
        
        self.UNIFORMS = {
            'a':GL.glGetUniformLocation(self.shader, 'a'),
            'b':GL.glGetUniformLocation(self.shader, 'b'),
            's':GL.glGetUniformLocation(self.shader, 's'),
            't':GL.glGetUniformLocation(self.shader, 't')}
        
        
        
        image_source = PIL_Image.open("tex0.png")
        image_source = image_source.convert('RGBA')
        image = image_source.tostring('raw', 'RGBA', 0, -1)
        self.ID = GL.glGenTextures(1)
        GL.glActiveTexture(GL.GL_TEXTURE0)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.ID)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL_s3tc.GL_COMPRESSED_RGB_S3TC_DXT1_EXT, ## Configure compression format!
            image_source.size[0],
            image_source.size[1],
            0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, image)
        del image
        
        
        image_source2 = PIL_Image.open("tex1.bmp")
        image_source2 = image_source2.convert('RGBA')
        image2 = image_source2.tostring('raw', 'RGBA', 0, -1)
        self.ID2 = GL.glGenTextures(1)
        GL.glActiveTexture(GL.GL_TEXTURE1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.ID2)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL_s3tc.GL_COMPRESSED_RGB_S3TC_DXT1_EXT, ## Configure compression format!
            image_source2.size[0],
            image_source2.size[1],
            0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, image2)
        del image2
        
    def render(self):
        GL_shaders.glUseProgram(self.shader)
        GL.glUniform1f(self.UNIFORMS['a'], 0.5)
        GL.glUniform4f(self.UNIFORMS['b'], 1.0, 1.0, 0.0, 1.0)
        GL.glUniform1i(self.UNIFORMS['s'], 0)
        GL.glUniform1i(self.UNIFORMS['t'], 1)
        
        try:
            self.vbo.bind() # Select "self.vbo"
            self.ibo.bind() # Select "self.ibo"
            #  It won't deselect "self.vbo" since they target different buffers
            try:
                GL.glEnableVertexAttribArray(0)
                GL.glEnableVertexAttribArray(1)
                GL.glEnableVertexAttribArray(2)
                
                GL.glVertexAttribPointer( # Vertex data, maybe...
                    0,              # Attribute 0 in this attribute array
                    3,              # This attribute uses 3 elements
                    GL.GL_FLOAT,    # These values are of type "GL_FLOAT"
                    False,          # Normalize values? No!
                    8*4,            # bits per row, 4 bits for floats, 6 elements in one row (doubles are 8)
                    self.vbo)       # Where in each row does attribute start? A little unintuitive...
                
                GL.glVertexAttribPointer( # Normal data, maybe...
                    1,
                    3,
                    GL.GL_FLOAT,
                    False,
                    8*4,
                    self.vbo + 3*4)
                    
                GL.glVertexAttribPointer( # UV-mapping data, maybe...
                    2,
                    2,
                    GL.GL_FLOAT,
                    False,
                    8*4,
                    self.vbo + 6*4)
                
                GL.glDrawElements(
                    GL.GL_TRIANGLES,
                    6, ##TODO: create method that gets number of indices in IBO!
                    GL.GL_UNSIGNED_INT, self.ibo)
            finally:
                self.vbo.unbind()
                self.ibo.unbind()
                GL.glDisableVertexAttribArray(0)
                GL.glDisableVertexAttribArray(1)
                GL.glDisableVertexAttribArray(2)
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
    w = Window("OpenGL", 1024, 768)
    w.run()
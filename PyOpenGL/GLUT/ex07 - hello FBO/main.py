import OpenGL.GLUT as GLUT
import OpenGL.GL as GL
import OpenGL.arrays.vbo as GL_vbo
import OpenGL.GL.shaders as GL_shaders
import OpenGL.GL.EXT.texture_compression_s3tc as GL_s3tc
import PIL.Image as PIL_Image
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
        
        # Create redraw mechanism:
        GLUT.glutDisplayFunc(self.draw)
        GLUT.glutMainLoop()
        
    def mySetup(self):
        # Create two shaders:
        self.shader_1 = self.loadShader("vs_1.glsl", "fs_1.glsl")
        self.UNIFORMS_1 = {
            'tex0':GL.glGetUniformLocation(self.shader_1, 'tex0')}
        self.shader_2 = self.loadShader("vs_2.glsl", "fs_2.glsl")
        self.UNIFORMS_2 = {
            'col_tex':GL.glGetUniformLocation(self.shader_2, 'col_tex')}
        #Define geometry:
        self.vbo = GL_vbo.VBO(
            np.array([
            [-1.0,-1.0, 0.0,   0.0, 0.0],
            [ 1.0,-1.0, 0.0,   1.0, 0.0],
            [ 1.0, 1.0, 0.0,   1.0, 1.0],
            [-1.0, 1.0, 0.0,   0.0, 1.0],
            ], dtype=np.float32), target=GL.GL_ARRAY_BUFFER)
        
        self.ibo = GL_vbo.VBO(
            np.array([
            [0, 1, 3],
            [1, 2, 3]
            ], dtype=np.uint32), target=GL.GL_ELEMENT_ARRAY_BUFFER)
        
        file = PIL_Image.open("tex0.png")
        file = file.convert('RGBA')
        file_stream = file.tostring('raw', 'RGBA', 0, -1)
        # Assign an ID to this texture:
        self.tex0_ID = 0;
        ID = GL.glGenTextures(1)
        GL.glActiveTexture(GL.GL_TEXTURE0 + self.tex0_ID)
        GL.glBindTexture(GL.GL_TEXTURE_2D, ID)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL_s3tc.GL_COMPRESSED_RGB_S3TC_DXT1_EXT,
            file.size[0],
            file.size[1],
            0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, file_stream)
        del file, file_stream
        
        self.fbo = GL.glGenFramebuffers(1) ## Look into ctypes and pointers!
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.fbo)
        
        self.col_tex_ID = 1
        self.col_tex = GL.glGenTextures(1)
        GL.glActiveTexture(GL.GL_TEXTURE0 + self.col_tex_ID)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.col_tex)
        GL.glTexStorage2D(GL.GL_TEXTURE_2D, 1, GL.GL_DEPTH_COMPONENT32F, 512, 512)
        # "GL.GL_DEPTH_COMPONENT32F" for depth testing
        # "GL.GL_RGBA8" for color testing
        
        GL.glFramebufferTexture(
            GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT,
            self.col_tex, 0)
        # "GL.GL_DEPTH_ATTACHMENT" for depth testing
        # "GL.GL_COLOR_ATTACHMENT0" for color testing
        
    
    def render(self):
        
        try: # Run first shader program:
            GL.glEnable(GL.GL_DEPTH_TEST) # Enable for depth test
            GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.fbo)
            GL.glViewport(0, 0, 512, 512)
            GL.glClearBufferfv(GL.GL_DEPTH, 0, 1) # last argument: 0 for depth, tuple for color (eg. (1.0, 0.0, 0.0, 1.0) for red etc)
            # "GL.GL_DEPTH" for depth testing
            # "GL.GL_COLOR" for color testing
            
            GL_shaders.glUseProgram(self.shader_1)
            GL.glUniform1i(self.UNIFORMS_1['tex0'], self.tex0_ID)
            self.vbo.bind()
            self.ibo.bind()
            try:
                GL.glEnableVertexAttribArray(0)
                GL.glEnableVertexAttribArray(1)
                
                GL.glVertexAttribPointer( # Vertex data
                    0,              # Attribute 0 in this attribute array
                    3,              # This attribute uses 3 elements
                    GL.GL_FLOAT,    # These values are of type "GL_FLOAT"
                    False,          # Normalize values? No!
                    5*4,            # bits per row, 4 bits for floats, 6 elements in one row (doubles are 8)
                    self.vbo)       # Where in each row does attribute start? A little unintuitive...
                    
                GL.glVertexAttribPointer( # UV-mapping data
                    1,
                    2,
                    GL.GL_FLOAT,
                    False,
                    5*4, ## OpenGL can calculate this for you, apparently. Try setting it to 0!
                    self.vbo + 3*4)
                    
                GL.glDrawElements(
                    GL.GL_TRIANGLES,
                    6, ##TODO: create method that gets number of indices in IBO!
                    GL.GL_UNSIGNED_INT, self.ibo)
            finally:
                GL.glDisableVertexAttribArray(0)
                GL.glDisableVertexAttribArray(1)
        finally:
            self.vbo.unbind()
            self.ibo.unbind()
            GL_shaders.glUseProgram(0)
            GL.glDisable(GL.GL_DEPTH_TEST)
            GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
            GL.glViewport(0, 0, self.width, self.height)
        
        try: # Run second shader program:
            GL.glBindTexture(GL.GL_TEXTURE_2D, self.col_tex)
            
            
            GL_shaders.glUseProgram(self.shader_2)
            GL.glUniform1i(self.UNIFORMS_2['col_tex'], self.col_tex_ID)
            self.vbo.bind()
            self.ibo.bind()
            try:
                GL.glEnableVertexAttribArray(0)
                GL.glEnableVertexAttribArray(1)
                
                GL.glVertexAttribPointer( # Vertex data
                    0,              # Attribute 0 in this attribute array
                    3,              # This attribute uses 3 elements
                    GL.GL_FLOAT,    # These values are of type "GL_FLOAT"
                    False,          # Normalize values? No!
                    5*4,            # bits per row, 4 bits for floats, 6 elements in one row (doubles are 8)
                    self.vbo)       # Where in each row does attribute start? A little unintuitive...
                    
                GL.glVertexAttribPointer( # UV-mapping data
                    1,
                    2,
                    GL.GL_FLOAT,
                    False,
                    5*4,
                    self.vbo + 3*4)
                    
                GL.glDrawElements(
                    GL.GL_TRIANGLES,
                    6, ##TODO: create method that gets number of indices in IBO!
                    GL.GL_UNSIGNED_INT, self.ibo)
            finally:
                GL.glDisableVertexAttribArray(0)
                GL.glDisableVertexAttribArray(1)
        finally:
            self.vbo.unbind()
            self.ibo.unbind()
            GL_shaders.glUseProgram(0)
            GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
        
        
    
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
        
    def loadShader(self, vs, fs):
        # Load vertex shader file and compile:
        with open(vs, 'r') as vs_file:
            VERTEX_SHADER = GL_shaders.compileShader(
                vs_file.read(),
                GL.GL_VERTEX_SHADER)
        del vs_file # Delete file object, good programming practice
        # Load fragment shader file and compile:
        with open(fs, 'r') as fs_file:
            FRAGMENT_SHADER = GL_shaders.compileShader(
                fs_file.read(),
                GL.GL_FRAGMENT_SHADER)
        del fs_file # Delete file object, good programming practice
        # Compile and return shader program:
        return GL_shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
    
if __name__ == "__main__":
    w = Window("OpenGL", 640, 480)
    w.run()
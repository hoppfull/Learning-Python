import utils_engine, utils_math, utils_resource
import OpenGL.GL as GL
import OpenGL.GL.shaders as GL_shaders
import numpy as np
import ctypes as c

class MyApp(utils_engine.GameEngine):
    def __init__(self, name, width, height):
        utils_engine.GameEngine.__init__(self, name, width, height)
        
    def setup(self): # Initialize this session
        GL.glClearColor(0.4, 0.4, 0.4, 0.0) # Set background color
        
        self.shader = utils_resource.loadShader("vertexshader.glsl", "fragmentshader.glsl")
        self.UNIFORMS = {
            'my_ModelMatrix':GL.glGetUniformLocation(self.shader, 'my_ModelMatrix'),
            'my_ViewMatrix':GL.glGetUniformLocation(self.shader, 'my_ViewMatrix'),
            'my_ProjectionMatrix':GL.glGetUniformLocation(self.shader, 'my_ProjectionMatrix')}
        
        #Define geometry:
        self.vertex_data = np.array([
            [-1.0, 0.0,-1.0,   0.0, 0.0, 1.0],
            [ 1.0, 0.0,-1.0,  -1.0, 0.0,-1.0],
            [-1.0, 0.0, 1.0,   1.0, 0.0,-1.0]
            ], dtype=np.float32)
        
        self.index_data = np.array([
            [0, 1, 2]
            ], dtype=np.uint32)
        
        self.vbo = GL.glGenBuffers(1)
        self.ibo = GL.glGenBuffers(1)
        
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo) # Select self.vbo
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertex_data, GL.GL_STATIC_DRAW) # Assign data to selected buffer
        
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ibo) # Select self.ibo
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, self.index_data, GL.GL_STATIC_DRAW) # Assign data to selected buffer
        
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0) # Deselect buffers
        
        #Set model in world coordinates:
        self.ModelMatrix = utils_math.ModelMatrix()
        #self.ModelMatrix.rotate(0, (1, 0, 0))
        self.ModelMatrix.setDirection(forward=(0,-1, 0), up=(0, 0, 1))
        #self.ModelMatrix.translate((0, 0, 0))
        self.ModelMatrix.setScale((0.5, 0.5, 0.5))
        
        #Set camera in world coordinates:
        self.ViewMatrix = utils_math.ViewMatrix()
        self.ViewMatrix.setPosition((0, -5, 0))
        self.ViewMatrix.setDirection(forward=(0, 1, 0), up=(0, 0, 1))
        #self.ViewMatrix.rotate(0.01, (0, 0, 1))
        
        # Setup frustum properties, near coords, far coords, field of view in turns
        self.ProjectionMatrix = utils_math.ProjectionMatrix(self.width, self.height, 0.1, 100.0, 0.3)
        
    def mainLoop(self): # Run this session
        try:
            GL_shaders.glUseProgram(self.shader)
            GL.glUniformMatrix4fv(
                self.UNIFORMS['my_ModelMatrix'],1, GL.GL_TRUE,
                self.ModelMatrix.get()
                )
            GL.glUniformMatrix4fv(
                self.UNIFORMS['my_ViewMatrix'],1, GL.GL_TRUE,
                self.ViewMatrix.get()
                )
            GL.glUniformMatrix4fv(
                self.UNIFORMS['my_ProjectionMatrix'],1, GL.GL_TRUE,
                self.ProjectionMatrix.get()
                )
            
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
                
                GL.glVertexAttribPointer( # Extra vertex data
                    1,
                    3,
                    GL.GL_FLOAT,
                    False,
                    self.vertex_data.shape[1]*c.sizeof(c.c_float),
                    c.c_void_p(3*4))
                GL.glEnableVertexAttribArray(1)
                
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
    app = MyApp("OpenGL!", 800, 600)
    app.run()
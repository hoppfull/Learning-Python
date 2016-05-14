import numpy as np
import ctypes as ct

import OpenGL.GL as GL
import OpenGL.GL.shaders as GL_shaders
import OpenGL.GL.EXT.texture_compression_s3tc as GL_s3tc

import PIL.Image as PIL_Img

def loadShader(vs, fs):
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

class texture2D:
	def __init__(self, texturefile):
		with PIL_Img.open(texturefile, 'r') as src:
			# Convert string to unsigned bytes: (Is that what happens?)
			image_data = src.convert('RGBA').tostring('raw', 'RGBA', 0, -1)
			
			# Generate a place in memory for our texture data:
			self.tex = GL.glGenTextures(1)
			GL.glBindTexture(GL.GL_TEXTURE_2D, self.tex) # Select tex
			
			GL.glTexStorage2D( # Allocate storage space for texture
				GL.GL_TEXTURE_2D, # Type of texture
				5, # Mipmap level
				GL_s3tc.GL_COMPRESSED_RGBA_S3TC_DXT1_EXT,
				src.size[0], src.size[1])
			
			GL.glTexSubImage2D(
				GL.GL_TEXTURE_2D,
				0, ## Level 0, what does that mean?
				0, 0, # Offset, if I want to store several textures in one big texture
				src.size[0], src.size[1],
				GL.GL_RGBA,
				GL.GL_UNSIGNED_BYTE,
				image_data) # pixels
			
			# Automatic mipmap generation:
			GL.glGenerateMipmap(GL.GL_TEXTURE_2D)
			GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
			GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
			GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
			GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR_MIPMAP_LINEAR)
			
			GL.glBindTexture(GL.GL_TEXTURE_2D, 0) # Deselect tex
		del src, image_data
	
	def bind(self, id):
		# id is a number from 0 and up which will indicate to shader where to find a texture.
		# the same number is passed to shader via glUniform1i(uniformName, id)
		GL.glActiveTexture(GL.GL_TEXTURE0 + id)
		GL.glBindTexture(GL.GL_TEXTURE_2D, self.tex)
	
	def unbind(self):
		GL.glBindTexture(GL.GL_TEXTURE_2D, 0)
	
class model:
	def __init__(self, meshfile):
		mesh =  np.load(meshfile)
		self.nindices = mesh['IBO'].size
		"""Currently, this format I've designed cannot handle anything
		less or more than a mesh with vertex data, normal data and uv data
		arranged accordingly in columns in a single numpy array. If I wish
		to make this adaptive, I could easily make this take in many
		more vertex attributes. With vertex colors defined in Blender 2.72.
		I will."""
		
		try:
			# Generate a place in memory for our vertex data:
			self.vboID = GL.glGenBuffers(1)
			GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vboID) # Select vbo
			# Send vertex data to GPU:
			GL.glBufferData(GL.GL_ARRAY_BUFFER, mesh['VBO'], GL.GL_STATIC_DRAW)
			
			# Generate a place in memory for our index data:
			self.iboID = GL.glGenBuffers(1)
			GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.iboID) # Select ibo
			# Send index data to GPU:
			GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, mesh['IBO'], GL.GL_STATIC_DRAW)
			
			self.vaoID = GL.glGenVertexArrays(1)
			GL.glBindVertexArray(self.vaoID)
			GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vboID) # Select vbo
			
			GL.glVertexAttribPointer(0, # Attribute number in this Vertex Array Object (VAO)
				3, # This attribute uses 3 elements. I could make this adaptive and probably will.
				GL.GL_FLOAT, # These values are of type "GL_FLOAT"
				GL.GL_FALSE, # These values will not be normalized (made to range between 0.0 and 1.0)
				8*4, # Bits per row. n*elements * bits/element. verts: 3, norms: 3, uv-coords: 2, floats: 4 bit
				ct.c_void_p(0)) # Where (in bits) in each row does this attribute start?)
			GL.glEnableVertexAttribArray(0) # Enable VBO, assign it to VAO at location = 0
			
			GL.glVertexAttribPointer(1, # Attribute number in this Vertex Array Object (VAO)
				3, # This attribute uses 3 elements. I could make this adaptive and probably will.
				GL.GL_FLOAT, # These values are of type "GL_FLOAT"
				GL.GL_FALSE, # These values will not be normalized (made to range between 0.0 and 1.0)
				8*4, # Bits per row. n*elements * bits/element. verts: 3, norms: 3, uv-coords: 2, floats: 4 bit
				ct.c_void_p(3*4)) # Where (in bits) in each row does this attribute start?)
			GL.glEnableVertexAttribArray(1) # Enable VBO, assign it to VAO at location = 1
			
			GL.glVertexAttribPointer(2, # Attribute number in this Vertex Array Object (VAO)
				2, # This attribute uses 3 elements. I could make this adaptive and probably will.
				GL.GL_FLOAT, # These values are of type "GL_FLOAT"
				GL.GL_FALSE, # These values will not be normalized (made to range between 0.0 and 1.0)
				8*4, # Bits per row. n*elements * bits/element. verts: 3, norms: 3, uv-coords: 2, floats: 4 bit
				ct.c_void_p(6*4)) # Where (in bits) in each row does this attribute start?)
			GL.glEnableVertexAttribArray(2) # Enable VBO, assign it to VAO at location = 2
		
		finally:
			GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0) # Deselect all
			GL.glBindVertexArray(0) # Deselect vao
		
		
	def bind(self):
		GL.glBindVertexArray(self.vaoID) # Select vao
		
		GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.iboID) # Select ibo
		GL.glDrawElements(
			GL.GL_TRIANGLES,
			self.nindices,
			GL.GL_UNSIGNED_INT, 
			ct.c_void_p(0))
		
	def unbind(self):
		GL.glBindVertexArray(0) # Deselect vao
import numpy as np

import OpenGL.GL as GL
import OpenGL.GL.shaders as GL_shaders

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

class obj:
	def __init__(self, filename):
		v, vt, vn = [], [], []
		fv, ft, fn = [], [], []
		
		with open(filename, 'r') as file:
			for line in file:
				# Lines to ignore:
				if line.startswith('\n'): continue
				if line.startswith('#'): continue
				if line.startswith('s'): continue
				if line.startswith('o'): continue
				
				# Split line by space into list:
				values = line.split()
				
				# If line contains vertex information:
				if values[0] == 'v':
					temp_ = [] # Temporary list to hold values for this line
					for value in values[1:]:
						# Go through line, convert strings to floats and assign them to temporary list:
						temp_.append(float(value))
					# Once line has been processed and stored in temp array, assign to vertex information list:
					v.append(temp_)
					
				# If line contains uvmap information:
				if values[0] == 'vt':
					temp_ = [] # Temporary list to hold values for this line
					for value in values[1:]:
						# Go through line, convert strings to floats and assign them to temporary list:
						temp_.append(float(value))
					# Once line has been processed and stored in temp array, assign to uvcoords information list:
					vt.append(temp_)
				
				# If line contains normal information:
				if values[0] == 'vn':
					temp_ = [] # Temporary list to hold values for this line
					for value in values[1:]:
						# Go through line, convert strings to floats and assign them to temporary list:
						temp_.append(float(value))
					# Once line has been processed and stored in temp array, assign to normal information list:
					vn.append(temp_)
				
				# If line contains index information:
				if values[0] == 'f':
					# Temporary lists to hold vertex indices, uvmap indices and normal indices:
					fv_, ft_, fn_ = [], [], []
					for value in values[1:]:
						# Split strings further by forward slash:
						temp_ = value.split('/')
						fv_.append(int(temp_[0])-1)
						ft_.append(int(temp_[1])-1)
						fn_.append(int(temp_[2])-1)
						# Subtract by one becouse obj indices start with first index at 1
					fv.append(fv_)
					ft.append(ft_)
					fn.append(fn_)
		del file
		#This setup assumes normals use an index buffer!
		self.vertices = np.array(v, dtype=np.float32)
		self.uvcoords = np.array(vt, dtype=np.float32)
		self.normals = np.array(vn, dtype=np.float32)
		self.vindices = np.array(fv, dtype=np.uint32)
		self.tindices = np.array(ft, dtype=np.uint32)
		self.nindices = np.array(fn, dtype=np.uint32)
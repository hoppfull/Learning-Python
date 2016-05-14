"""Turns out .obj file format has some bad special cases that
doesn't work well with OpenGL. Don't use it! Use stanford.sly instead!"""


import numpy as np

v = []
vt = []
vn = []
fv, ft, fn = [], [], []

filename = "plane.obj"

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

# print(np.array(v))
# print(np.array(vt))
# print(np.array(vn))
# print(np.array(fv))
# print(np.array(ft))
# print(np.array(fn))
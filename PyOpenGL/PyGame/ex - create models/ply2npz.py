"""When running this script, add model filename as argument
without the file ending to let script know which file to
convert to numpy binary file."""
import sys
import numpy as np

vertex_data = []
index_data = []

with open(sys.argv[1] + ".ply", 'r') as file:
	for line in file:
		# Ignore lines starting with:
		if line.startswith('#'): continue
		if line.startswith('vertex_data'): continue
		if line.startswith('index_data'): continue
		if line.startswith('\n'): continue
		
		if not line.startswith('\t'):
			# load vertex data (vertex coordinates,
			# normal coordinates and uv coordinates):
			values = line.split()
			temp_ = []
			for value in values:
				temp_.append(float(value))
			vertex_data.append(temp_)
		else:
			# load index data:
			values = line.split()
			temp_ = []
			for value in values[1:]:
				temp_.append(int(value))
			index_data.append(temp_)
del file

# print(np.array(vertex_data, dtype=np.float32))
# print(np.array(index_data, dtype=np.uint32))

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html#numpy.savez
np.savez(sys.argv[1],
	VBO=np.array(vertex_data, dtype=np.float32),
	IBO=np.array(index_data, dtype=np.uint32))

"""To load stored array simply use:
file = np.load(filename)
and 'file' will contain dictionary of the numpy arrays.
One named 'VBO' with vertex data in it and one named
'IBO' with index data in it."""
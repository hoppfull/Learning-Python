cimport numpy as np
import numpy as np

def LinReg(unsigned int n = 4, unsigned int m = 10):
	cdef np.ndarray[np.int_t, ndim = 1] mag
	cdef np.ndarray[np.float_t, ndim = 2] x, y, DATASET
	cdef np.ndarray[np.float_t, ndim = 1] w
	
	x = np.random.random((m,n))
	mag = np.random.random_integers(1, 3, n)
	x = np.hstack((np.ones([m,1]), x * 10**mag))
	
	w = np.random.uniform(-1, 1, n + 1)
	mag = np.random.random_integers(1, 2, n +1)
	w = w * 10**mag
	
	w = w * np.hstack((1, np.random.random_integers(0, 3, n).clip(max=1))) #Here we randomly turn off features x_1 to x_n
	y = np.sum(np.array(x * w), axis=1).reshape((m,1))
	
	DATASET = np.hstack((y, x[:, 1:])).round(2)

	return DATASET, w
import numpy as np

def logreg(n = 5, m = 11, o = 4):
	y = np.zeros((m, o))
	for i in range(o):
		r = 100
		k = round(m//o)
		if i == 0:
			cluster = np.random.uniform(-1000, 1000, (n))
			x = np.random.uniform(-r, r, (k, n)) + cluster
			y[:k, i] = 1
		elif i < o - 1 and i > 0:
			cluster = np.random.uniform(-1000, 1000, (n))
			x = np.vstack((x, np.random.uniform(-r, r, (k, n)) + cluster))
			y[i * k:(i+1) * k, i] = 1
		elif i == o - 1:
			cluster = np.random.uniform(-1000, 1000, (n))
			x = np.vstack((x, np.random.uniform(-r, r, (k + m%o, n)) + cluster))
			y[i * k:, i] = 1
	
	return np.hstack((y, x))
	
def linreg(n = 4, m = 10):
	x = np.around(np.random.random((m,n)), 2)
	mag = np.around(np.random.uniform(1, 2.6, n))
	x = np.hstack((np.ones([m,1]), x * 10**mag))
	
	w = np.random.uniform(-1, 1, n + 1)
	mag = np.around(np.random.uniform(1, 1.7, n + 1))
	w = w * 10**mag
	
	w = w * np.hstack((1, np.random.random_integers(0, 3, n).clip(max=1)))
	y = np.around(np.reshape(np.array(x * w).sum(axis=1), (m,1)), 2)

	return np.hstack((y, x[:, 1:])), w
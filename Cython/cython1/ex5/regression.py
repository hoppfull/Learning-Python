import numpy as np

def linreg(DATASET, parameters, precision = 10, max_iterations = 500, learningrate = 1, regularization = 1):
	m = DATASET.shape[0] #Number of training examples
	n = DATASET.shape[1] #Number of features
	y_raw = np.array(DATASET[:,0]).reshape((m, 1)) #Target variables
	x_raw = np.hstack((  np.ones((m, 1)), DATASET[:, 1:]  )) #Feature variables
	
	feature_scale = m/np.absolute(x_raw).sum(0) #feature scaling
	target_scale = m/np.absolute(y_raw).sum(0) #target scaling
	X = x_raw * feature_scale
	Y = y_raw * target_scale
	
	i = k = 0
	d0 = d1 = 1
	p0 = 1
	while i < max_iterations and k < 10:
		J = np.zeros(n)
		j = 0
		while j < n:
			J[j] = sum(np.hstack(((parameters * X), - Y)).sum(1) * X[:, j])/m
			j = j + 1
		if regularization != 1:
			parameters[1:] = parameters[1:] * regularization
		parameters = parameters - (learningrate * J)
		if k == 0: p0 = parameters
		# else:
		d2 = np.absolute(np.sum(x_raw * (parameters * feature_scale / target_scale), 1).reshape((m,1)) - y_raw).sum(0)/m
		learningrate = ((d0 / d1) * 0.01)**0.5
		
		i = i + 1
		k = k + 1
		if k != 10:
			continue
		k = 0
		y_predict = np.sum(x_raw * (parameters * feature_scale / target_scale), 1).reshape((m,1))
		d1 = np.absolute(y_predict - y_raw).sum(0)/m
		if(i > 0 and d1 > d0):
			learningrate = learningrate * 0.1
			parameters = p0
		
		print("Deviation: ", d1)
		if np.absolute(y_predict - y_raw).sum(0)/m < precision or i == max_iterations:
			# print("Deviation: ", np.absolute(y_predict - y_raw).sum(0)/m)
			break
		d0 = d1
	print("Finished in ", i, " steps!")
	parameters = parameters * feature_scale / target_scale
	print(parameters)

'''	
def linreg(DATASET, parameters, iterations = 200, learningrate = 0.4, regularize = 1):
	m = DATASET.shape[0] #Number of training examples
	n = DATASET.shape[1] #Number of features
	y_raw = np.array(DATASET[:,0]).reshape((m, 1)) #Target variables
	x_raw = np.hstack((  np.ones((m, 1)), DATASET[:, 1:]  )) #Feature variables
	
	feature_scale = m/np.absolute(x_raw).sum(0) #feature scaling
	target_scale = m/np.absolute(y_raw).sum(0) #target scaling
	X = x_raw * feature_scale
	Y = y_raw * target_scale
	
	i = 0
	while i < iterations:
		J = np.zeros(n)
		j = 0
		while j < n:
			J[j] = sum(np.hstack(((parameters * X), - Y)).sum(1) * X[:, j])/m
			j = j + 1
		if regularize != 1:
			parameters[1:] = parameters[1:] * regularize
		parameters = parameters - (learningrate * J)
		i = i + 1
		
	parameters = parameters * feature_scale / target_scale
	print(parameters)
'''
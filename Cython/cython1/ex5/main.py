import get_dataset
import regression
import numpy as np
import time
np.set_printoptions(precision=2, linewidth = 250) #This is a nifty little line. It allows the python console to print out arrays in the specified manner

n = 4 #Number of features
m = 100#Number of training examples
o = 3 #Number of logical classes

DATASET, w = get_dataset.linreg(n, m)
theta = np.ones(DATASET.shape[1])
for i in range(4):
	time.sleep(1)
	print((3 - i))
regression.linreg(DATASET, theta)
print(w)
#Normal equation test.
import numpy as np
np.set_printoptions(precision=2, linewidth = 250) #This is a nifty little line. It allows the python console to print out arrays in the specified manner
import get_dataset

n = 3000
m = 10000


DATASET, w0 = get_dataset.linreg(n, m)
y = DATASET[:, 0]
X = np.hstack((np.ones(m).reshape((m,1)), DATASET[:, 1:]))

# X = np.array([[1, 3, 1], [1, 1, 2]])
# y = np.array([11,10])

# w1 = np.dot(np.dot(np.linalg.pinv(np.dot(X.T, X)), X.T), y)
w = np.linalg.lstsq(X, y)[0]

# print(w1)
print(np.around(w - w0))
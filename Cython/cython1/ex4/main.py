import get_dataset
import numpy as np
np.set_printoptions(precision=2, linewidth = 250) #This is a nifty little line. It allows the python console to print out arrays in the specified manner

n = 5 #Number of features
m = 10 #Number of training examples
o = 3 #Number of logical classes


# DATASET, w = get_dataset.LinReg(n , m)
# print(DATASET)
# print(w)
DATASET = get_dataset.LogReg(n, m, o)
print(DATASET)

'''
Looks like the pure python version
of the get_dataset library is fast
enough that no cython optimization
is required.



'''
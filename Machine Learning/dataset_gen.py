import numpy as np

#m: number of training examples
#n: number of features
#o: number of targets or classes

#x = feature set
#y = target set

#w = parameters

def logreg_datagen(m, n, o = 1):
    magnitude = ( 10*np.ones(n) )**np.around(np.random.random()*3)
    x = np.around(np.column_stack((  np.ones([m,1]), (np.random.random([m,n])-0.5) * 10  )), 3)
    x[:, 1:] = x[:, 1:] * magnitude
    
    w = np.around( np.random.random([o, n+1])*5, 3 )
    y = np.zeros([m, o])
    
    for i in range(o):
        y[:, i] = (x * w[i, :]).sum(1)
    
    if(o > 1):
        for i in range(m):
            y_max = np.amax(y[i, :])
            for j in range(o):
                if(y[i, j] == y_max):
                    y[i, j] = 1
                else:
                    y[i, j] = 0
    else:
        for i in range(m):
            if(y[i] >= 0):
                y[i] = 1
            else:
                y[i] = 0

    return np.column_stack((y, x[:, 1:]))
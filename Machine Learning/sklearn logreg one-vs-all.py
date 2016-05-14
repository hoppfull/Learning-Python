import dataset_gen
import numpy as np
from sklearn import linear_model

m = 200 #Number of training (and testing examples) examples
m_training = 100 #Number of training examples (only)
n = 5  #Number of features
o = 3  #Number of targets/classes
DATASET = dataset_gen.logreg_datagen(m,n,o)
#IMPORTANT! If you have a class/ target with no members, i.e. all members of that class equal zero, you will get an error! Rerun the program if that happens!

def sigmoid(X):
    return (1/(1 + np.exp(-(X) )))

def main():
    LogReg = linear_model.LogisticRegression()
    
    w = np.zeros([o, n])
    w0 = np.zeros([o, 1])
    y_raw = DATASET[:, :o]
    x_raw = DATASET[:, o:]
    
    for i in range(o):
        LogReg_temp = LogReg.fit(x_raw[:m_training, :], y_raw[:m_training, i])
        w[i, :] = LogReg_temp.coef_
        w0[i, :] = LogReg_temp.intercept_
    
    y_result = np.zeros([m_training, o])
    
    for i in range(o):
        y_result[:, i] = (x_raw[m_training:] * w[i, :]).sum(1) + w0[i]
    y_result = np.around(sigmoid(y_result), 3)
    y_result = np.around(y_result/y_result.sum(1).reshape(m_training,1), 3)
    print(y_result)
    
    #Testing START
    for i in range(m_training):
        y_max = np.amax(y_result[i, :])
        for j in range(o):
            if(y_result[i, j] == y_max):
                y_result[i, j] = 1
            else:
                y_result[i, j] = 0
    
    print(y_result - y_raw[m_training:, :])        
    #Testing END
    
    return 0
main()
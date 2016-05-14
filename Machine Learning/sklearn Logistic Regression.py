from sklearn import linear_model
import numpy as np

#http://scikit-learn.org/stable/modules/linear_model.html
#almost identical to the linear regression algorithm

directory = "D:\Storage\Creations\Machine Learning\Linear Regression\\"
DATASET = np.load(directory + "DATASETlogreg.npy")

def sigmoid(X):
    return (1/(1 + np.exp(-(X) )))

def main():
    x_raw = DATASET[:, 1:]
    y_raw = DATASET[:, 0]
    
    LogReg = linear_model.LogisticRegression()
    LogReg.fit(x_raw[:250], y_raw[:250])
    
    w0 = LogReg.intercept_
    w = LogReg.coef_
    
    #Testing the prediction
    y_prediction = np.around(sigmoid(w0 + (x_raw[250:] * w).sum(1)), 2)
    
    y = y_raw[250:] - y_prediction
    print(np.around(y,1)) #the closer to zero, the better the prediction
    
main()
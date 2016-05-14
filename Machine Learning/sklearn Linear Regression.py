from sklearn import linear_model
import numpy as np

#http://scikit-learn.org/stable/modules/linear_model.html

directory = "D:\Storage\Creations\Machine Learning\Linear Regression\\"
DATASET = np.load(directory + "DATASETlinreg.npy") #272.8, 0.5, 0.5, 95.8, 83.9, 8.4

def main():
    x_raw = DATASET[:, 1:]
    y_raw = DATASET[:, 0]
    
    LinReg = linear_model.LinearRegression()
    LinReg.fit(x_raw, y_raw)
    
    w0 = np.around(LinReg.intercept_, 1)
    w = np.around(LinReg.coef_, 1)
    
    print(w0, w)
    
main()
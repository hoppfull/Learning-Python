import numpy as np
import scipy.optimize as opt
import myMachineLearning as myML

directory = "D:\Storage\Creations\Machine Learning\Linear Regression\\"
DATASETlinreg = np.load(directory + "DATASETlinreg.npy") #272.8, 0.5, 0.5, 95.8, 83.9, 8.4
DATASETlogreg = np.load(directory + "DATASETlogreg.npy") #-0.11816234  0.02735321 -0.01151663 -0.00269124 -0.10264381  0.01057927 -0.00115387

def RunLinReg():
    iterations = 150
    learningrate = 0.2
    
    theta = np.zeros(DATASETlinreg.shape[1])
    theta = myML.myLinear_Regression(DATASETlinreg, theta, iterations)
    
    print(np.around(theta, 1))

def RunLogReg():
    iterations = 1000
    learningrate = 0.5

    theta = np.zeros(DATASETlogreg.shape[1])
    theta = myML.myLogical_Regression(DATASETlogreg, theta, iterations)
    
    print(theta)

def main():
    



    return 0
    
    
main()
import numpy as np

def myLinear_Regression(DATASETlinreg, parameters, iterations, learningrate = 0.1):
    #Loading data into appropriate variables:
    m = DATASETlinreg.shape[0]    #Number of training examples
    n = DATASETlinreg.shape[1]    #Number of features
    
    y_raw = np.array([ DATASETlinreg[:,0] ]).transpose() #target variables
    x_raw = np.column_stack((   np.array([ np.ones(m) ]).transpose(), DATASETlinreg[:,1:]   )) #feature variables
    
    #feature scaling:
    feature_scale = m/np.absolute(x_raw).sum(0)
    target_scale = m/np.absolute(y_raw).sum(0)
    X = x_raw * feature_scale
    Y = y_raw * target_scale
    
    for i in range(iterations):
        J = np.zeros(n)
        for j in range(n):
            J[j] = sum(   ( np.column_stack(( (parameters * X), -Y )) ).sum(1) * X[:, j]   )/m
        
        parameters = parameters - (learningrate * J)
    
    parameters = parameters * feature_scale / target_scale
    return parameters

def myLogical_Regression(DATASETlogreg, parameters, iterations, learningrate = 0.5):
    #Loading data into appropriate variables:
    m = DATASETlogreg.shape[0]    #Number of training examples
    n = DATASETlogreg.shape[1]    #Number of features
    
    e = 2.71828182846 #Eulers number for use in the sigmoid function
    
    Y = np.array([ DATASETlogreg[:,0] ]).transpose() #target variables
    x_raw = np.column_stack((   np.array([ np.ones(m) ]).transpose(), DATASETlogreg[:,1:]   )) #feature variables
    
    #feature scaling:
    feature_scale = m/np.absolute(x_raw).sum(0)
    X = x_raw * feature_scale
    
    for i in range(iterations):
        J = np.zeros(n)
        for j in range(n):
            J[j] = sum(   np.column_stack(( 1/(1+np.e**(-parameters * X).sum(1)), -Y)).sum(1) * X[:, j]   )/m
        
        parameters = parameters - (learningrate * J)
    
    parameters = parameters * feature_scale
    return parameters

    
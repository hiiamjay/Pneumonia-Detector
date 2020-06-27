import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(Data,coef):
    length = Data.shape[0]
    XM = np.append(1,Data)
    pred = np.dot(XM,coef)
    pred = sigmoid(pred)
    if pred>=0.5:
        a = 1;
    else:
        a = 0;
    return(a)

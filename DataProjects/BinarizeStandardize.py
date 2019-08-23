# Python code for binarization 
import os.path
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import StandardScaler

import pandas 
import numpy 

file = 'diabetes.csv'
if os.path.exists(file):
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
    dataframe = pandas.read_csv(file)
    array = dataframe.values 

    # separate array into input and output components 
    X = array[:, 0:8] 
    Y = array[:, 8] #Diabetes = yes or no
    binarizer = Binarizer(threshold = 0.0).fit(X)
    binaryX = binarizer.transform(X)

    scaler=StandardScaler().fit(X)
    rescaledStd=scaler.transform(X)


    # summarize transformed data     
    numpy.set_printoptions(precision = 3)
    print (rescaledStd[0:5,:])
    print(binaryX[0:5, :])
    print()
else:
    print("File not found.")

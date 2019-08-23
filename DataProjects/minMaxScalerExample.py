import csv
import os.path
import pandas 
import scipy 
import numpy 
from sklearn.preprocessing import MinMaxScaler
#print ("Hello world")
#hello

# Python code to Rescale data (between 0 and 1) 

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
file='diabetes.csv' 
if os.path.exists(file):
    print('File found')
    dataframe = pandas.read_csv(file) 
    array = dataframe.values 
    
    #separate array into input and output components 
    X = array[:,0:8] 
    Y = array[:,8] 
    scaler = MinMaxScaler(feature_range=(0, 1)) 
    rescaledX = scaler.fit_transform(X)

    # summarize transformed data 
    numpy.set_printoptions(precision=3) 
    print(rescaledX[0:5,:]) #first 5 rows of every column
else:
    print('File does not exist')

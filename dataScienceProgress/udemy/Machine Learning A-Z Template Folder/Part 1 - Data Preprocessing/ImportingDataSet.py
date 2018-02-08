# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:25:35 2017

@author: Navneet
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.preprocessing import Imputer

dataSet = pd.read_csv("Data.csv")

#create matrix subfolder and dependent variable vector
X = dataSet.iloc[:,:-1].values
y = dataSet.iloc[:,3].values

#add missing values to nan
#imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
#imputer = imputer.fit(x[:,1:3])
#x[:,1:3]=imputer.transform(x[:,1:3])

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#taking care of categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

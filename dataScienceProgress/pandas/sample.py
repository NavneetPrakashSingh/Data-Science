# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:51:54 2017

@author: Navneet
"""
import numpy as np
import pandas
from pandas import DataFrame, Series
import statsmodels.api as sm
df = pandas.read_csv('/Users/Navneet/Desktop/pandas/titanic_data.csv')
total =0

dictionary = {}
for index,row in df.iterrows():
    if row['Sex']=="female" or (row['Age']<18 and row['Pclass']==1):
        dictionary[int(row['PassengerId'])]=1
    elif row['Sex']=="male":
        dictionary[int(row['PassengerId'])]=0
    else:
        dictionary[int(row['PassengerId'])]="NA"
predictions = dictionary
print("Predictions are:")
print(predictions)
array =[1,2,3]
dataFrame = {"Series":['a','b','c'],"Numbers":[1,2,3]}
finalDataFrame = DataFrame(dataFrame)
print(finalDataFrame)
print(np.mean(array))

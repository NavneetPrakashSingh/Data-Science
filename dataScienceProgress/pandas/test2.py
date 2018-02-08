# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:08:51 2017

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
    dictionary[int(row['PassengerId'])]=row["Survived"]
predictions = dictionary
print("Predictions are:")
print(predictions)
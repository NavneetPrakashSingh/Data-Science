# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:17:05 2017

@author: Navneet
"""

import pandas
import numpy as np

baseball = pandas.read_csv('/Users/Navneet/Desktop/pandas/Master.csv')
finalMean = np.mean(baseball['weight'])
baseball['weight']=baseball['weight'].fillna(finalMean)
print(baseball['weight'])

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:55:12 2017

@author: Navneet
"""

import numpy as np
data = [1,2,3,4,8]
predictions=[1,2,3,4,5]
mean=np.mean(data)
#print(mean)
i=0
temp=0
meanTotal =0
for x in data:
    temp = temp + np.square(data[i]-predictions[i])
    meanTotal = meanTotal + np.square(data[i]-mean)
    i=i+1
finalTemp = 1-temp
r_squared = finalTemp/meanTotal
print(r_squared)
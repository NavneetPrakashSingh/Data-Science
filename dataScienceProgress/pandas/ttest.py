# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:28:37 2017

@author: Navneet
"""

import scipy.stats
import pandas
df = pandas.read_csv('/Users/Navneet/Desktop/pandas/baseball_stats.csv')
#print(df["handedness"],df["avg"])
#get data related to right handed and left handed batsman
#store it in twolists and pass it to scipt function
temp=[]
rightTemp=[]
naTemp=[]
i=0
for index,row in df.iterrows():
    if(row["handedness"]=='R'):
       temp.append(row["avg"])
    elif(row["handedness"]=="L"):
        rightTemp.append(row["avg"])
    else:
        naTemp.append(row["avg"])
#print(rightTemp)
#print(scipy.stats.ttest_ind(temp,rightTemp,equal_var=False))
result = scipy.stats.ttest_ind(rightTemp,temp,equal_var=False)
if(result[1]<=0.5):
    return (False,result)
else:
    return (True,result)
print(var)
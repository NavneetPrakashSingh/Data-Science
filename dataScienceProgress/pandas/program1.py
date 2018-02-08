# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:03:00 2017

@author: Navneet
"""

import pandas as pd

#simple program for series data and understanding how series behave
#series is similar to array , they are zero based and values can be printed by placing index
#[values, index=[]]

#temp = pd.Series([1,2,3,4,5], index=["A","B","C","D","E"])
#print (temp)
#print (temp>3)
#print (temp[1])

#userstanding how dictionary behaves with series
#Q: Dataframe for which team won matches from 2010 to 2012
data = {
        "year":[2010,2011,2012],
        "teams":['A','B','C'],
        "wins":[5,6,7],
        "losses":[6,5,4]
       }
football=pd.DataFrame(data)
print(football.tail)
#print (football["teams"][0])

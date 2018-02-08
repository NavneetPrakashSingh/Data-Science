# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:46:13 2017

@author: Navneet
"""

import pandas
import pandasql

df = pandas.read_csv('/Users/Navneet/Desktop/pandas/weather-underground.csv')
df.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
#for index,row in df.iterrows():
#    print(row["date"],row['meantempi'])
# Q3 select avg(meantempi) from df where cast (strftime('%w', date) as integer) = 0 or cast (strftime('%w', date) as integer) =6
q ="""
    select avg(mintempi) from df where mintempi>55 and rain>0
    
    """
final_solution = pandasql.sqldf(q.lower(), locals())
print(final_solution)


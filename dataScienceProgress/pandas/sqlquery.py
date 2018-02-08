# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:51:43 2017

@author: Navneet
"""
import pandas
import pandasql


aadhaar_data = pandas.read_csv('/Users/Navneet/Desktop/pandas/aadhaar_data.csv')
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
q ="""
    select * from aadhaar_data limit 50
    """
aadhaar_solution = pandasql.sqldf(q.lower(), locals())
print(aadhaar_solution)


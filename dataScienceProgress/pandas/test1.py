# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:00:56 2017

@author: Navneet
"""

from pandas import DataFrame, Series
import numpy as np

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
olympic_medal_counts = {'country_name':Series(countries),
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
df = DataFrame(olympic_medal_counts)
#approach 1
print(np.mean(df['bronze'][df['gold']>0]))
#approach 2
i=0.0
sum=0.0
for index,row in df.iterrows() :
    if row['gold'] > 0:
        i = i+1
        sum=sum+row['bronze'] 
avg_bronze_at_least_one_gold = float(sum/i)
print(avg_bronze_at_least_one_gold)

#print(np.mean(df['gold'][0],df['gold'][1]))
    # YOUR CODE HERE

    #return avg_bronze_at_least_one_gold
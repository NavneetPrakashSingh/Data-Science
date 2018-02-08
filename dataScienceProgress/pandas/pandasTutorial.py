# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:31:04 2017

@author: Navneet
"""

import pandas as pd
import numpy as np

#data = {
#        "Countries":["Russia","Norway","Canada","United States","Neatherlands"],
#        "Gold":[13,11,10,9,8],
#        "Silver":[11,5,10,7,7],
#        "bronze":[9,10,5,12,9]
#       }
#olympic_medal_count_df = pd.DataFrame(data)
#
#print(olympic_medal_count_df)

data = {
        "one":pd.Series([1,2,3],index=['a','b','c']),
        "two":pd.Series([1,2,3,4],index=['a','b','c','d'])        
        }
dataFrame = pd.DataFrame(data)
#print(dataFrame.apply(np.mean))
print(dataFrame.applymap(lambda x: x>1))

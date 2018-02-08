# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:02:58 2017

@author: Navneet
"""

import pandas
from pandas import DataFrame, Series
df ={"ENTRIESn":Series([3144312,3144335,3144353,3144424,3144594,3144808,3144895,3144905])}
finalFrame = DataFrame(df)
shiftedValues = abs(finalFrame.ENTRIESn.shift(1)-finalFrame.ENTRIESn)

dataFrameToBeAppended = pandas.DataFrame({"ENTRIESn_hourly":Series(shiftedValues)})
dataFrameToBeAppended["ENTRIESn_hourly"].fillna(1, inplace = True)
finalDf = finalFrame.join(dataFrameToBeAppended)
print(finalDf)


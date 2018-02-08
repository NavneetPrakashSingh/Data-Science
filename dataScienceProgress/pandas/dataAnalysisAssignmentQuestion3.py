# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:46:48 2017

@author: Navneet
"""

import numpy as np
import scipy
import scipy.stats
import pandas

df = pandas.read_csv('/Users/Navneet/Desktop/pandas/turnstile_data.csv')
meanRain = np.mean(df[df.rain == 1]["ENTRIESn_hourly"])
meanNoRain = np.mean(df[df.rain == 0]["ENTRIESn_hourly"])
print(meanNoRain)
rainValue = scipy.stats.mannwhitneyu(df[df.rain == 1]["ENTRIESn_hourly"],df[df.rain == 0]["ENTRIESn_hourly"],True)
print(rainValue[0])
print(rainValue[1])

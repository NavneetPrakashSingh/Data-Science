# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:24:41 2017

@author: Navneet
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt

plt.figure()
df = pandas.read_csv('/Users/Navneet/Desktop/pandas/turnstile_data.csv')
df[df.rain == 1]["ENTRIESn_hourly"].hist(alpha=0.5)
df[df.rain == 0]["ENTRIESn_hourly"].hist(alpha=0.6)

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 17:27:44 2017

@author: Navneet
"""

from datetime import datetime, timedelta
lastHourDateTime = datetime.now() - timedelta(hours = 15)
time = lastHourDateTime.strftime('%H:%M:%S')
tempTime =time.split(':')
sample = "1"+"2"
print(sample)
print(int(tempTime[0]))
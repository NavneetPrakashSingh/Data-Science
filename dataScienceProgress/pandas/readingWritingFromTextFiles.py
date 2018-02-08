# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:03:23 2017

@author: Navneet
"""

import csv
f_in=open("/Users/Navneet/Desktop/pandas/sampleData.txt","r")
f_out=open("/Users/Navneet/Desktop/pandas/sampleOutData.txt","w")
reader_in =csv.reader(f_in,delimiter=',')
writer_out=csv.writer(f_out,delimiter=",")
#skiping the first line as it contains headers
next(reader_in)
i=0
for line in reader_in:    
    typeZero=line[0]
    typeOne=line[1]
    typeTwo=line[2]
    lineLength = len(line)
    i=3
    while i<lineLength:
        line_1=[typeZero,typeOne,typeTwo,line[i],line[i+1],line[i+2],line[i+3],line[i+4]]    
        writer_out.writerow(line_1)
        i=i+5
f_in.close()
f_out.close()


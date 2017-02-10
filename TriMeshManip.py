# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:16:40 2016

@author: ee10sjo
"""
import os
import numpy as np
import pandas as pd


#folder = 'E:\\NormalFault\\Tltd_1degS_2km_30L'
folder = 'Y:\\ee10sjo\\Oldfields_PhD\\4_Applications\\MOVE\\Tltd_1degS_2km_30L'

os.chdir(folder)

fl = os.listdir(folder)


### For testing, selects horizon Hz5.ts

with open(fl[26], 'r') as f:
    data = f.readlines()

def z_invert(data):
    # split lines, remove linebreak marker
    for i in np.arange(0, len(data)):
        data[i] = data[i].strip()
    
    # split columns deliminated by space
    for i in np.arange(0, len(data)):
        data[i] = data[i].split()
    
    # multiply z by -1
    for i in np.arange(0,len(data)):
        # select only vertices (does not edit individual triangles)
        if data[i][0] == 'VRTX':
            # Multiple each vertex z by -1
            data[i][-1] = str(np.multiply(float(data[i][-1]), -1))
            
            data[i][-1] = str((float(data[i][-1])+2000))
    
    # replace header keyword to indicate depth format
    data[10] = ['ZNEGATIVE', 'Depth']
    
    return data

data_inv = z_invert(data)

d = data_inv

with open(fl[26], 'w') as f:
    for i in d:
        out = "\n".join(str(d))
        f.writelines(out)

#for line in d:
#    d[line] = ['\t'.join(d[line])]

#adds tab to every break
with open("newfile.ts", "w") as f:
    for i in d:
        out = ["%s\t" % item for item in i]
        f.writelines(out)



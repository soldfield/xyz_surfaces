# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:16:40 2016

Series of tools for trimesh manipulation.  Initially this tool takes a trimesh
in gocad format and inverts the z axis by a '-1' multiplication.

Updates header information to say ['ZNEGATIVE', 'Depth'].

This annotation is one-way, i.e. positive to negative depth domain only currently.


@author: ee10sjo
"""
import os
import numpy as np
import pandas as pd


def grab_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data


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
            
            #data[i][-1] = str((float(data[i][-1])+2000))
    
    # replace header keyword to indicate depth format
    data[10] = ['ZNEGATIVE', 'Depth']
    
    return data


def output_file(fn, data):
    with open(fn, "w") as f:
        for i in data:
            out = ["%s\t" % item for item in i]
            #print(out)
            #return(out)
            out = out + ['\n']
            f.writelines(out)

def folder_Z_invert(folder):
    os.chdir(folder)
    fl = os.listdir(folder)
    for fn in fl:
        d = grab_data(fn)
        d = z_invert(d)
        name = str(fn[:-3])+'_Z_Inv.ts'
        output_file(name, d)



folder = 'Y:\\ee10sjo\\Oldfields_PhD\\4_Applications\\MOVE\\SimpleNF_Models\\ZZ_ExportedLayers\\Dmax5_Inverted'


folder_Z_invert(folder)

#file = fl[3]
#
#data = grab_data(file)
#
#d = z_invert(data)
#
#out = output_file("newfile.ts", d)



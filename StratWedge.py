# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:42:46 2017

Short script to generate a two-dimensional fold, based on a cosine curve.

Outputs xyz point cloud as a text file in the working directory.

@author: Simon J. Oldfield

   Copyright 2016 Simon Oldfield

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
   
"""

## Initially attemting to build a simple sin wave

import numpy as np
import matplotlib.pyplot as plt

## Name variables:
Xmin = 0.
Xmax = 4000.
Ymin = 0.
Ymax = 2000.
WaveXmin = 1000.
WaveXmax = 3000.
WaveAmp = 800.
Wavelength = 1600.
Spacing = 100.


def stratwedge(Xmin, Xmax, Ymin, Ymax, WaveXmin, WaveXmax, WaveAmp, Wavelength, Spacing):
    ## Calculate basic parameters
    Xrange = WaveXmax - WaveXmin
    Yrange = Ymax - Ymin
    XSamps = Xrange / Spacing
    YSamps = Yrange / Spacing
    
    ## Generate wavelet of desired size
    x = np.arange(WaveXmin, WaveXmax, Spacing)
    
    # Add *-1 for syncline
    z = ((np.cos(2 * np.pi * x / Xrange) / 2) + 0.5) * 1.
    z = z * WaveAmp
    
#    flat_x = np.arange(Xmin, Xmax, Spacing)
#    flat_z = np.zeros(flat_x)
    
    ## Add flats to either side of wavelet
    # Below X side
    x1 = np.arange(Xmin, WaveXmin, Spacing)
    z1 = np.zeros(int((WaveXmin - Xmin) / Spacing))
    
    # Above X side
    x2 = np.arange(WaveXmax, (Xmax + Spacing), Spacing)
    z2 = np.zeros(int(((Xmax - WaveXmax) + Spacing) / Spacing))
    
    # Append arrays for each coordinate
    Xall = np.hstack((x1, x, x2))
    Yall = np.zeros((len(Xall)))
    Zall = np.hstack((z1, z, z2))
    
    # Combine XYZ
    # ALL = np.vstack((Xall, Zall, Yall))
    xyz = np.column_stack((Xall, Yall, Zall))
    
    ## Stretch to pseudo-3D through the Y axis
    # Create loop to add sample offset for Y to each line and add output to the column stack

    Yarray = np.arange(Ymin, (Ymax + Spacing), Spacing)
    
    # Initialise array and iterate to duplicate teh first line for each value of y
    xyz_stk = np.array([0,0,0])
    
    for y in Yarray:
        xyz2 = xyz + [0, y, 0]
        xyz_stk = np.vstack(( xyz_stk, xyz2))
    
    # Delete the first row of the array generated in initiation
    xyz_stk = np.delete(xyz_stk, (0), axis = 0)
    
    ## Plot for reference
    plt.axis('equal')
    plt.plot(Xall, Zall)
    plt.xlabel('X Distance')
    plt.ylabel('Z Distance')
    #np.savetxt('anticline_xyz.txt', (xyz_stk), fmt='%16s')
    
    plt.show()
    
    #Output to text file in working directory, format 16 character string per column

def coswave(height, wavelength, spacing):
    xs = np.arange(0, wavelength+1, spacing)
    ys = (height/2)*np.cos((2*np.pi*x)/wavelength)

    return xs, ys

def stratwedge2(Xwidth, Ywidth, Ztop, spacing, layers):
#               Ymin, Ymax, WaveXmin, WaveXmax, WaveAmp, Wavelength, Spacing):
    Xmin = 0
    Xmax = Xmin + Xwidth
    Ymin = 0
    Ymax = Ywidth + Ymin
    
    surf_name = []
    
    for i in np.arange(layers):
        surf_name.append("line"+str(i+1))
    
    
    Xsi = np.arange(Xmin, Xmax, spacing)
    Ysi = np.arange(Ymin, Ymax, spacing)
    Zsi = 
    
    Xi
    Yi
    Zi
    
    surf_name[-1] = 
    
    
    x1 = np.arange(Xmin, Xmax, spacing)
    y1 = np.zeros((len(x1)))
    z1 = height * np.sin((x*2*np.pi())/wavelength)
    
    Xall = 
    Yall = 
    Zall = 
    


coswave(2, 32, 1)

    


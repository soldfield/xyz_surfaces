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
#Xmin = 0.
#Xmax = 4000.
#Ymin = 0.
#Ymax = 2000.
#WaveXmin = 1000.
#WaveXmax = 3000.
#WaveAmp = 800.
#Wavelength = 1600.
#Spacing = 100.


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

def coswave(depth, width, height, spacing):
    xs = np.arange(0, width+1, spacing)
    ys= depth + (np.cos((2*np.pi*xs)/width)*0.5)*height+ height/2
    
    return xs, ys

def planehz(depth, width, spacing):
    xs = np.arange(0, width+spacing, spacing)
    ys = np.empty_like(xs)
    ys = np.full(xs.size, depth)
    
    return xs, ys


def CosLayerStk(depth_top, dx, dz_pinch, dz_model, xspacing, Nl=12):
    Sx = xspacing # x sample rate
    
    xlen = int(dx/Sx)+1
    stk = np.zeros([Nl+2, xlen])
    
    ### Set parameters for cosine curve
    costop = depth_top + dz_pinch
    dz_cos = dz_model - dz_pinch
    
    stk[0,:], stk[1,:]= coswave(costop, dx, dz_cos, Sx)
    
    stk[-1, :] = planehz(depth_top, dx, Sx)[1]
    
    for i in np.arange(xlen):
        z_int = (stk[1,i]-stk[-1, i])/Nl
        for j in np.arange(2, Nl+1):
            stk[j,i]=stk[-1,i]+z_int*(j-1)
    
    for i in np.arange(1,stk.shape[0]):
        plt.plot(stk[0,:], stk[i,:])
    
    return stk



depth = 2000
width = 1000
dz_model = 500
dz_pinch = 50
xspacing = 10
Nl = 12

costop = depth + dz_pinch
dz_cos = dz_model - dz_pinch

a, b = coswave(costop, width, dz_cos, xspacing)

#plt.show()

stk = CosLayerStk(depth, width, dz_pinch, dz_model, xspacing)

plt.plot(stk[0,:], stk[-4,:])
plt.plot(a,b, 'k--')


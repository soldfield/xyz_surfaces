# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:27:39 2015

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
Xmax = 8000.
Ymin = 0.
Ymax = 2000.
WaveXmin = 3000.
WaveXmax = 5000.
WaveAmp = 800.
Wavelength = 1600.
Spacing = 100.

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

## Add flats to either side of wavelet
# Below X side
x1 = np.arange(Xmin, WaveXmin, Spacing)
z1 = np.zeros(((WaveXmin - Xmin) / Spacing))

# Above X side
x2 = np.arange(WaveXmax, (Xmax + Spacing), Spacing)
z2 = np.zeros((((Xmax - WaveXmax) + Spacing) / Spacing))

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
plt.show()

#Output to text file in working directory, format 16 character string per column

np.savetxt('anticline_xyz.txt', (xyz_stk), fmt='%16s')


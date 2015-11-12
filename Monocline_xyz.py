# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:05:58 2015

Script to generate simple monoclinal surfaces as point clouds.

@author: ee10sjo
"""

import numpy as np
import matplotlib.pyplot as plt
import math

## Name variables:
Xmin = 0.
Xmax = 8000.
Ymin = 0.
Ymax = 2000.
Spacing = 100.
Zmid = 5000.
RampWidth = 2000.
Slope = 60.

## Calculate basic parameters
Xrange = Xmax - Xmin
Yrange = Ymax - Ymin
XSamps = Xrange / Spacing
YSamps = Yrange / Spacing
RampXmin = ((Xmin + Xmax) / 2) - (RampWidth / 2)
RampXmax = ((Xmin + Xmax) / 2) + (RampWidth / 2)

## Calculate x values for the monoclinal ramp
x = np.arange(RampXmin, (RampXmax + Spacing), Spacing)

## Calculate y and z to match length for 2D shape
y = np.zeros((len(x)))
Zmin = Zmid - ((RampWidth / 2) * math.tan(math.radians(Slope)))
Zmax = Zmid + ((RampWidth / 2) * math.tan(math.radians(Slope)))

## Calculate z from x position (note degrees to radians conversion)
z = Zmin + ((x - RampXmin) * math.tan(math.radians(Slope)))

## Add flats to either side of ramp
# Below X side
x1 = np.arange(Xmin, RampXmin, Spacing)
z1 = np.zeros(((RampXmin - Xmin) / Spacing))
z1 = z1 + Zmin

# Above X side
x2 = np.arange(RampXmax, (Xmax + Spacing), Spacing)
z2 = np.zeros((((Xmax - RampXmax) + Spacing) / Spacing))
z2 = z2 + Zmax

###########################################
## Generate wavelet of desired size
# x = np.arange(WaveXmin, WaveXmax, Spacing)

# Add *-1 for syncline
# z = ((np.cos(2 * np.pi * x / Xrange) / 2) + 0.5) * 1.
# z = z * WaveAmp

## Add flats to either side of wavelet
# Below X side
# x1 = np.arange(Xmin, WaveXmin, Spacing)
# z1 = np.zeros(((WaveXmin - Xmin) / Spacing))

# Above X side
# x2 = np.arange(WaveXmax, (Xmax + Spacing), Spacing)
# z2 = np.zeros((((Xmax - WaveXmax) + Spacing) / Spacing))

# Append arrays for each coordinate
Xall = np.hstack((x1, x, x2))
Yall = np.zeros((len(Xall)))
Zall = np.hstack((z1, z, z2))

# Combine XYZ
# ALL = np.vstack((Xall, Zall, Yall))
xyz = np.column_stack((Xall, Yall, Zall))
######################################




# Combine XYZ
# ALL = np.vstack((Xall, Zall, Yall))
# xyz = np.column_stack((x, y, z))

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

np.savetxt('monocline60deg_xyz.txt', (xyz_stk), fmt='%16s')

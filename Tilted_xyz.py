# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:05:58 2015

@author: Simon J Oldfield

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
Slope = 55

## Calculate basic parameters
Xrange = Xmax - Xmin
Yrange = Ymax - Ymin
XSamps = Xrange / Spacing
YSamps = Yrange / Spacing

## Calculate xyz values independently for a 2D plane
x = np.arange(Xmin, (Xmax + Spacing), Spacing)
y = np.zeros((len(x)))

Zmin = Zmid - ((Xrange/2) * math.tan(math.radians(Slope)))

## Calculate z from x position (note degrees to radians conversion)
z = Zmin + ((x - Xmin) * math.tan(math.radians(Slope)))

# Combine XYZ
# ALL = np.vstack((Xall, Zall, Yall))
xyz = np.column_stack((x, y, z))

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
plt.plot(x, z)
plt.xlabel('X Distance')
plt.ylabel('Z Distance')
plt.show()

#Output to text file in working directory, format 16 character string per column

np.savetxt('tilted55deg_xyz.txt', (xyz_stk), fmt='%16s')

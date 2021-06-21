# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:17:39 2021

@author: dingxu
"""

from PyAstronomy import pyaGui
import numpy as np


# Data for the plot
x = np.linspace(0., 10., 100)
y = np.exp(-x/10.)

# Create Picker instance
pp = pyaGui.Picker()

# Create the plot in which points
# are to be selected
pp.a.plot(x, y, 'b.-')

points = pp.pick()

print("Number of selected points: ", len(points))
print("Selected points (x, y):")
for p in points:
    print("%g, %g" % p)
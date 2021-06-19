# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:18:18 2021

@author: dingxu
"""

import numpy as np
from astropy.timeseries import LombScargle
import matplotlib.pyplot as plt  

rand = np.random.RandomState(42)
t = 100 * rand.rand(100)
y = np.sin(2 * np.pi * t) + 0.1 * rand.randn(100)

frequency, power = LombScargle(t, y).autopower()

plt.figure(0)
plt.plot(frequency, power) 

dy = 0.1
frequency, power = LombScargle(t, y, dy).autopower()

dy = 0.1 * (1 + rand.rand(100))
y = np.sin(2 * np.pi * t) + dy * rand.randn(100)*2
frequency, power = LombScargle(t, y, dy).autopower()
plt.figure(1)
plt.plot(frequency, power)

print(frequency.max(), power.max(), frequency[np.argmax(power)])
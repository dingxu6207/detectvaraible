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
y = np.sin(2 * np.pi * t) + 0.1 * rand.randn(100)+10

frequency, power = LombScargle(t, y).autopower()

plt.figure(0)
plt.plot(frequency, power) 

dy = 0.1
best_frequency = frequency[np.argmax(power)]
t_fit = np.linspace(0, 1)
ls = LombScargle(t, y, dy)

y_fit = ls.model(t_fit, best_frequency)

plt.figure(1)
plt.plot(t_fit, y_fit, '.')

plt.figure(2)
plt.plot(t, y, '.')

theta = ls.model_parameters(best_frequency)
offset = ls.offset()
design_matrix = ls.design_matrix(best_frequency, t_fit)
npdata = np.allclose(y_fit, offset + design_matrix.dot(theta))


plt.figure(3)
plt.plot(t_fit, design_matrix.dot(theta), '.')



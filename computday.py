# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:38:58 2021

@author: dingxu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle 

data = pd.read_csv('AP3422309.csv', sep = ',' )

hjdmag = data[['hjd', 'mag']]
nphjmag = np.array(hjdmag)

t = nphjmag[:,0]
y = nphjmag[:,1]
ls = LombScargle(t, y)
frequency, power = ls.autopower(minimum_frequency=0.1, maximum_frequency=20, samples_per_peak=10)

plt.figure(0)
plt.plot(frequency, power, '.')
print(frequency.max(), power.max(), frequency[np.argmax(power)])

plt.figure(1)
plt.plot(t, y, '.')


from PyAstronomy.pyasl import foldAt
P=1/(3.2954000000025276)
phases = foldAt(t, P)
sortIndi = np.argsort(phases)
phases = phases[sortIndi]
resultmag = y[sortIndi]

plt.figure(2)
plt.plot(phases, resultmag, '.')


from PyAstronomy.pyTiming import pyPDM
S = pyPDM.Scanner(minVal=0.1, maxVal=20, dVal=0.0001, mode="frequency")
P = pyPDM.PyPDM(t, y)

#f1, t1 = P.pdmEquiBinCover(10, 3, S)
f2, t2 = P.pdmEquiBin(10, S)
plt.figure(3)
plt.plot(f2, t2, 'gp-')
#plt.plot(f1, t1, 'rp-')
plt.xlabel('frequency',fontsize=14)
plt.ylabel('Theta', fontsize=14)
print(f2[np.argmin(t2)])
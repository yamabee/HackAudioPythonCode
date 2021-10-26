# SLEWRATEEXAMPLE
# This script demonstrates how to use the slewRateDistortion
# function. Two examples are provided, with a sine wave and a
# square wave.
#
# See also SLEWRATEDISTORTION

import numpy as np
import matplotlib.pyplot as plt
from slewRateDistortion import slewRateDistortion

Fs = 48000
Ts = 1/Fs
f = 5
t = np.arange(0, Fs) * Ts

x = np.sin(2 * np.pi * f * t)
# x = np.sign(np.sin(2 * np.pi * f * t))

maxFreq = 3
y = slewRateDistortion(x, Fs, maxFreq)

plt.plot(t, x)
plt.plot(t,y)
plt.axis([0, 1, -1.1, 1.1])
plt.legend(['Input', 'Output'])
plt.show()
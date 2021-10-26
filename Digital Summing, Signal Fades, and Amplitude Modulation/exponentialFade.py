# EXPONENTIAL FADE
# This script creates exponential fades, both convex and
# concave examples are provided. These fades are applied
# to the beginning and end of a sine wave test signal.
#
# See also, LINEARFADE

import numpy as np
import matplotlib.pyplot as plt


Fs = 48000
Ts = 1/Fs
t = np.arange(0, 3*Fs) * Ts
f = 100
phi = 0
x = np.sin((2 * np.pi * f * t) + phi)
plt.figure(1)
plt.plot(t, x)

# Convex fades
numSamples = 1 * Fs # 1 second fade-in/out

# Exponent for curve
c = 2 # c can be any number > 1 (linear = 1)

a = np.linspace(0, 1, numSamples)
fadeOut = 1 - pow(a, c)

a = np.linspace(1, 0, numSamples)
fadeIn = 1 - pow(a, c)

plt.figure(2)
plt.plot(a, fadeIn, a, fadeOut)
plt.legend(['Fade-in', 'Fade-out'])

# Fade-in
temp = x
temp[0:numSamples] = fadeIn * x[0:numSamples]
plt.figure(3)
plt.plot(t, temp)

# Fade-out
out = temp
out[-1 - numSamples: -1] = fadeOut * temp[-1 - numSamples: -1]
plt.figure(4)
plt.plot(t, out)

a = np.linspace(0, 1, numSamples)
a = a.T
fadeOut = pow(a, c)

# (Alternate) concave fades
a = np.linspace(1, 0, numSamples)
a = a.T
fadeIn = pow(a, c)
plt.figure(5)
plt.plot(a, fadeIn, a, fadeOut)
plt.legend(['Fade-in', 'Fade-out'])
plt.show()
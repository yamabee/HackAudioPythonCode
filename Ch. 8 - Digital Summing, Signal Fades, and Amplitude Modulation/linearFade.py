# LINEARFADE
# This script creates linear fades. Then the 'fade-in'
# is applied to the beginning of a sine wave signal. The
# 'fade-out' is applied to the end.
#
# See also EXPONENTIALFADE

import numpy as np
import matplotlib.pyplot as plt

Fs = 48000
Ts = 1/Fs
f = 100
phi = 0
t = np.arange(0, Fs*3) * Ts
x = np.sin((2 * np.pi * f * t) + phi)

plt.figure(1)
plt.plot(t, x)
plt.show()

numSamples = 1 * Fs  # 1 second fade-in/out
a = np.linspace(0, 1, numSamples)
fadeIn = a
fadeOut = 1-a  # Equivalent = np.linspace(1, 0, numSamples)
plt.figure(2)
plt.plot(a, fadeIn, a, fadeOut)
plt.legend(['Fade-in', 'Fade-out'])

# Fade-in
# Index samples just at the start of the signal
temp = x
temp[0:numSamples] = fadeIn * x[0:numSamples]
plt.figure(3)
plt.plot(t, temp)

# Fade-out
# Index samples just at the end of the signal
out = temp
out[-1 - numSamples: -1] = fadeOut * temp[-1 - numSamples: -1]
plt.figure(4)
plt.plot(t, out)
plt.show()

# EQUALFADES
# This script analyzes an exponential crossfade for
# 'equal amplitude' or 'equal power'.

import numpy as np
import matplotlib.pyplot as plt

Fs = 44100

# Square-root fades
x = 2  # can be any number >= 2
numSamples = 1 * Fs  # 1 second fade-in/out
aIn = np.linspace(0, 1, numSamples)
fadeIn = pow(aIn, 1/x)

aOut = np.linspace(1, 0, numSamples)
fadeOut = pow(aOut, 1/x)

# Compare amplitude vs. power of crossfade
plt.plot(aIn, fadeIn, '--', aIn, fadeOut, ':', aIn, fadeIn + fadeOut, aIn, (pow(fadeIn, 2) + pow(fadeOut, 2)))
plt.axis([0, 1, 0, 1.5])
plt.legend(['Fade-in', 'Fade-out', 'Crossfade Amplitude', 'Crossfade Power'])
plt.show()
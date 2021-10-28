# SCURVEFADE
# This script demonstrates one approach to creating S-curve fades.
# This method involves concatenating a convex fade with a concave
# fade.
#
# See also LINEARFADE, EXPONENTIALFADE, SINECURVEFADE

import numpy as np
import matplotlib.pyplot as plt

Fs = 44100 # Arbitrary sampling rate

# S-curve fade-in
numSamples = round(1 * Fs) # 1 sec. fade, round to whole sample
halfSamples = round(numSamples/2)
a = np.linspace(0, 1, halfSamples)
x = 2 # can be any number >= 1
concave = 0.5 * pow(a, x)
convex = 0.5 * (1 - pow((1-a), x)) + 0.5
# fadeIn = np.concatenate(concave, convex)
fadeIn = np.hstack((concave, convex))

# S-curve fade-out
x = 3 # can be any number >= 1
convex = 0.5 * (1 - pow(a, x)) + 0.5
concave = 0.5 * pow(1 - a, x)
# fadeOut = np.concatenate(convex, concave)
fadeOut = np.hstack((convex, concave))

# Plot the S-curve
t = np.linspace(0, 1, numSamples)
plt.plot(t, fadeIn, t, fadeOut)
plt.legend(['Fade-in', 'Fade-out'])
plt.show()
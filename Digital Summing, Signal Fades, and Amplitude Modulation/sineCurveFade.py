# SINECURVEFADE
# This script demonstrates one approach to creating S-curve fades.
# This method involves using the sine function.
#
# See also, LINEARFADE, EXPONENTIALFADE, SCURVEFADE

import numpy as np
import matplotlib.pyplot as plt

Fs = 44100  # Arbitrary sampling rate
Ts = 1/Fs
# S-curve fade-in
lenSec = 1  # 1 second fade-in/out
N = round(lenSec * Fs)  # Convert to whole # of samples
t = np.arange(0, N) * Ts

# The S-curve fade is half a cycle of a sine wave. If
# fade is 1 sec., period of sine wave is 2 sec.
period = 2 * N * Ts  # units of seconds
freq = 1/period  # units of Hz
fadeIn = 0.5 * np.sin((2 * np.pi * freq * t) - np.pi/2) + 0.5
# S-curve fade-out
fadeOut = 0.5 * np.sin((2 * np.pi * freq * t) + np.pi/2) + 0.5

# Plot the S-curve
plt.plot(t, fadeIn, t, fadeOut)
plt.legend(['Fade-in', 'Fade-out'])
plt.show()
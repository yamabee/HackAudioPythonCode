# SINESYNTHESIS
# This script demonstrates two methods to synthesize sine waves
#
# Method 1: A loop is used to step through each element of the
# arrays.
#
# Method 2: Array processing is used to perform element-wise
# referencing by the 'sin' function internally.
#
# See also SINEANGLE, SINESPECTRUM

import matplotlib.pyplot as plt
import numpy as np

# Example - Sine wave signal
# Declare initial parameters
f = 2  # frequency in Hz
phi = 0  # phase offset
Fs = 100  # sampling rate
Ts = 1/Fs  # sampling period
lenSec = 1  # 1 second long signal
N = Fs * lenSec  # convert to time samples
out1 = np.zeros([N, 1])

# Method 1: Loop to perform element-wise referencing
for n in range(N):
    t = n * Ts
    out1[n] = np.sin(2 * np.pi * f * t + phi)

# Method 2: Create a signal using array processing
# Phase shifted signal of identical frequency
t = np.arange(0, N) * Ts
out2 = np.sin(2 * np.pi * f * t + np.pi/2)

plt.plot(t, out1, t, out2)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.legend(['out1', 'out2'])
plt.show()
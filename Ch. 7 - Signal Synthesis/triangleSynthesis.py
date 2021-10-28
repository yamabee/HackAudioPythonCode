# TRIANGLESYNTHESIS
# This script demonstrates a method to transform the 'sawtooth'
# function to a triangle wave
#
# See also SINESYNTHESIS, SAWTOOTHSYNTHESIS, SQUARESYNTHESIS

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from IPython.display import Audio
import plottf

# Example - Triangle wave signal
# 4 Hz signal for visualization
f = 4
phi = 0
Fs = 40
Ts = 1/Fs
numSec = 1
N = Fs * numSec
t = np.arange(0, N) * Ts

# Triangle wave => peak occurs at half (0.5) of cycle length
width = 0.5
triangleWave = signal.sawtooth(2 * np.pi * f * t + phi, width)
plt.plot(t, triangleWave)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.show()

# Sawtooth with peak at beginning of cycle, then decreasing amp
width = 0
triangleWave = signal.sawtooth(2 * np.pi * f * t + phi, width)
plt.plot(t, triangleWave)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.show()

# Sawtooth with increasing amp during cycle, peak at end
width = 1
triangleWave = signal.sawtooth(2 * np.pi * f * t + phi, width)
plt.plot(t, triangleWave)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.show()

# 880 Hz square wave for audition
f = 880
Fs = 44100
Ts = 1/Fs
numSec = 3
N = Fs * numSec
t = np.arange(0, N) * Ts
sawtoothWave = signal.sawtooth(2 * np.pi * f * t, 0.5)
Audio(sawtoothWave, rate=Fs)
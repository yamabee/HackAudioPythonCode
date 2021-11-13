# SQUARESYNTHESIS
# This script demonstrates the a square wave
#
# See also SINESYNTHESIS, SAWTOOTHSYNTHESIS, TRIANGLESYNTHESIS

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
from plottf import plottf

# Example - Square wave signal
# 2 Hz square wave for visualization
f = 2
phi = 0
Fs = 1000
Ts = 1/Fs
lenSec = 1  # seconds
N = Fs * lenSec
t = np.arange(0, N) * Ts
squareWave = np.sign(np.sin((2 * np.pi * f * t) + phi))

plt.plot(t, squareWave)
plt.axis([0, 1, -1.1, 1.1])
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
squareWave = np.sign(np.sin((2 * np.pi * f * t) + phi))

# plottf(squareWave, Fs)

Audio(squareWave, rate=Fs)

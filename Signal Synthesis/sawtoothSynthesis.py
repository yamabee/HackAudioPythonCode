# SAWTOOTHSYNTHESIS
# This script demonstrates the 'sawtooth' function.
#
# See also SINESYNTHESIS, SQUARESYNTHESIS, TRIANGLESYNTHESIS

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from IPython.display import Audio

# Example - Sawtooth wave signal
# 4 Hz signal for visualization
f = 4
phi = 0
Fs = 40
Ts = 1/Fs
numSec = 1
N = Fs * numSec
t = np.arange(0, N) * Ts
sq = signal.square((2 * np.pi * f * t))
sawtoothWave = signal.sawtooth(2 * np.pi * f * t)
plt.plot(t, sawtoothWave)
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
sawtoothWave = signal.sawtooth(2 * np.pi * f * t)
Audio(sawtoothWave, rate=Fs)
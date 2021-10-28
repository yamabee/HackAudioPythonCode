# DUTYCYCLE
# This script synthesizes a square wave with an asymmetrical
# duty cycle
#
# See also SQUARESYNTHESIS

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Example - Duty cycle = 25
f = 3
Fs = 1000
Ts = 1/Fs
numSec = 1
N = Fs * numSec
t = np.arange(0, N) * Ts
duty = 0.25
sq = signal.square((2 * np.pi * f * t), duty)
plt.plot(t, sq)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.show()
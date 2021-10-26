# PHASEREXAMPLE
# This script demonstrates the use of a phaser function to add the effect to
# white noise. Parameters of the phaser effect include the rate and depth of
# the LFO. In this implementation, the delay time of an APF (Direct Form II)
# is modulated.
#
# See also PHASEREFFECT

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from IPython.display import Audio
from phaserEffect import phaserEffect

Fs = 48000
Ts = 1/Fs
sec = 5
lenSamples = sec * Fs
x = 0.2 * np.random.randn(lenSamples)
N = len(x)

rate = 0.8 # Hz (frequency of LFO)
depth = 0.3 # samples (amplitude of LFO)

# Initialize delay buffers
buffer = np.zeros(3) # All-pass filter

# Wet/dry mix
wet = 50

# Initialize output signal
out = np.zeros(len(x))

for n in range(N):
    # Use phaser effect function
    out[n], buffer = phaserEffect(x[n], buffer, Fs, n, depth, rate, wet)

Audio(out, rate=Fs)

nfft = 2048  # Length of each time frame
window = signal.windows.hann(nfft)  # Calculated window function
overlap = 128  # Number of samples for frame overlap
spec, f, tSpec, imAxis = plt.specgram(out)
plt.show()
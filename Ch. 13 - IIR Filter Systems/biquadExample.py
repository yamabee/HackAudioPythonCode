# BIQUADEXAMPLE
# This script demonstrates the use of the bi-quad filter function. Various
# filter types and topologies can be tested.
#
# See also BIQUADFILTER

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from biquadFilter import biquadFilter

# Impulse response of bi-quad
x = np.append(1, np.zeros(4096))

# Filter parameters
Fs = 48000
f = 1000  # frequency in Hz
Q = 0.707
dBGain = -6

# FILTER TYPE >>> 'lpf', 'hpf', 'pkf', 'bp1', 'bp2', 'apf', 'lsf', 'hsf'
type = 'lpf'
# TOPOLOGY >> 1 - Direct Form I, 2 - II, 3 Transposed II
form = 3

y = biquadFilter(x, Fs, f, Q, dBGain, type, form)
W, H = signal.freqz(y, 1, 4096, fs=Fs)

# Plot amplitude response of filter
plt.semilogx(W, 20 * np.log10(abs(H)))
plt.axis([20, 20000, -20, 15])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.show()

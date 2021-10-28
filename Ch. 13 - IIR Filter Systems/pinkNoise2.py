# PINKNOISE2
# This script synthesizes an approximation of pink noise
# using an IIR filter.
#
# Pink noise can be created by filtering white noise. The
# amplitude response of the filter decreases by 10 dB/decade
# or -3 dB/octave.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 48000
Nyq = Fs/2
sec = 5
white = np.random.randn(sec*Fs)
b = [0.04992035, -0.095993537, 0.050612699, -0.004408786]
a = [1, -2.494956002, 2.017265875, -0.522189400]

F, H = signal.freqz(b, a, 4096, fs=Fs)

plt.semilogx(F, 20 * np.log10(abs(H)))
# plt.axis([20, 20000, -30, 0])

pink = signal.lfilter(b,a,white)
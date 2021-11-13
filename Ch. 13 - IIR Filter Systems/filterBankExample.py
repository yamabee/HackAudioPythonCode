# FILTERBANKEXAMPLE
# This script creates a two-band filter bank using a LPF and HPF.
#
# See also BUTTER

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 48000
Nyq = Fs/2

m = 2  # filter order
numBands = 4

# Logarithmically spaced cutoff frequencies
# 2 * 10^1 - 2 * 10^4 (20-20k Hz)
freq = 2 * np.logspace(1, 4, numBands+1)

b = np.zeros([numBands+1, numBands+1])
a = np.zeros([numBands+1, numBands+1])

for band in range(numBands):
    low = freq[band] / Nyq
    high = freq[band + 1] / Nyq
    Wn = [low, high]

    b[band, :], a[band, :] = signal.butter(m, Wn, btype='bandpass')

    W, H = signal.freqz(b[band, :], a[band, :], worN=4096, fs=Fs)
    plt.semilogx(W, 20*np.log10(abs(H)))

plt.axis([20, 20000, -24, 6])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.show()

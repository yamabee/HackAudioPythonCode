# PINKNOISE1
# This script synthesizes an approximation of pink noise using an FIR filter.
#
# Pink noise can be created by filtering white noise. The amplitude response
# of the filter has a gain of 1/sqrt(f), where 'f' is the frequency (Hz).
#
# See also FIR2

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 48000  # Sampling rate
Nyq = Fs/2  # Nyquist frequency for normalization
sec = 5  # 5 seconds of noise
white = np.random.randn(sec*Fs, 1)

f = 20  # starting frequency in Hz

numFreqs = int(np.floor(np.log2(Nyq/f)+1))
freqs = np.zeros(numFreqs)
gains = np.zeros(numFreqs)

for freq in range(numFreqs):
    # Normalized frequency vector
    freqs[freq] = f/Nyq
    # Amplitude vector, gain = 1/sqrt(f)
    gains[freq] = 1/np.sqrt(f)

    f = f*2

# Set starting frequency and amplitude
freqs = np.append(0, freqs)
gains = np.append(1/np.sqrt(20), gains)

# Set frequency and amplitude at Nyquist
freqs = np.append(freqs, 1)
gains = np.append(gains, 1/np.sqrt(Nyq))

# Filter normalization factor to unity gain
unity = np.sqrt(20)
gainNorm = unity * gains

# Plot frequency response of filter
order = 11
h = signal.firwin2(numtaps=order, freq=freqs, gain=gainNorm)
F, H = signal.freqz(h, worN=4096, fs=Fs)

plt.semilogx(F, 20 * np.log10(abs(H)))
plt.axis([20, 20000, -30, 0])

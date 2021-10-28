# PLOTTF
# Plot sampled signal in time and frequency domains. Plots the time-domain
# samples in vector x, assuming that Fs is an audio sampling rate
# (44.1k, 48k, etc.) in samples/second, and also plots the Fourier transform
# on the decibel scale between the frequencies of 20 Hz and 20 kHz,
# logarithmically spaced.
#
# See also PLOT

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft

def plottf(x, Fs):

    Ts = 1/Fs
    N = len(x)
    t = np.arange(0, N) * 1/Fs

    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.xlabel('Time (sec.)')
    plt.ylabel('Amplitude')

    # Fourier Transform
    length = N
    if length < 4096:
        length = 4096

    X = (2/N) * fft(x, n=length)  # do DFT/FFT
    f = np.arange(0, length) * (Fs / length)

    X[abs(X) < 0.000001] = 0.000001

    plt.subplot(2, 1, 2)
    plt.semilogx(f, 20 * np.log10(abs(X)))
    plt.axis([20, 20000, -80, 4])
    plt.xticks([20, 50, 100, 200, 300, 500, 1000, 2000, 5000, 10000, 20000], [20, 50, 100, 200, 300, 500, 1000, 2000, 5000, 10000, 20000])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.show()
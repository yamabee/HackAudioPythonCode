# CISIMULATION
# This script performs vocoding using speech and white noise. This process is used
# to simulate cochlear implants for listeners with acoustic hearing.
#
# See also VOCODEREXAMPLE

import soundfile
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from IPython.display import Audio

# Import audio files
x, Fs = soundfile.read('Voice.wav')
N = len(x)
noise = 0.1 * np.random.randn(N)

# Initialize filter parameters
Nyq = Fs/2  # Nyquist frequency
order = 2  # Filter order

numBands = 16

# Logarithmically space cutoff frequencies
# 2*10^1 - 2*10^4 (20-20k) Hz
freq = 2 * np.logspace(1,4,numBands)

g = 0.9992  # Smoothing filter gain
fb = 0  # Initialize feedback delay

voxBands = np.zeros((N, numBands))
noiseBands = np.zeros((N, numBands))
envBands = np.zeros((N, numBands))

for band in range(numBands-1):
    Wn = np.append(freq[band], freq[band+1])
    Wn = Wn / Nyq
    b, a = signal.butter(order, Wn=Wn, btype='bandpass')

    # Filterbank
    voxBands[:, band] = signal.lfilter(b, a, x)
    noiseBands[:, band] = signal.lfilter(b, a, noise)

    # Envelope measurement
    for n in range(N):
        envBands[n, band] = (1-g) * abs(voxBands[n, band]) + g * fb
        fb = envBands[n, band]

    fb = 0

# Perform amplitude modulation
outBands = np.zeros((N, numBands))
for band in range(numBands):
    outBands[:, band] = envBands[:, band] * noiseBands[:, band]

# Sum together all the bands
out = np.sum(outBands, 1)
# Make-up gain
out = 32 * out

plt.plot(out)

Audio(out, rate=Fs)

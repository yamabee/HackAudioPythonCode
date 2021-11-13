# VOCODEREXAMPLE
# This script demonstrates the process of creating a vocoder effect using a
# voice signal and a synth signal.

import soundfile
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from IPython.display import Audio

# # Import audio files
x, Fs = soundfile.read('Voice.wav')
synth, _ = soundfile.read('Synth.wav')

# Initialize filter parameters
Nyq = Fs/2  # Nyquist frequency
order = 2   # Filter order

numBands = 16

# Logarithmically spaced cutoff frequencies
# 2*10^1 - 2*10^4 (20-20k) Hz
freq = 2 * np.logspace(1, 4, numBands)

g = 0.9992  # smoothing filter gain
fb = 0  # initialized value for feedback

N = len(x)

# These arrays are used to store the filtered versions of
# the input signal. Each column stores the signal for
# each band. As an example, voxBands[:,3] stores the
# band-pass filtered signal in the fourth band.
voxBands = np.zeros((N, numBands))
synthBands = np.zeros((N, numBands))
envBands = np.zeros((N, numBands))

for band in range(numBands-1): # perform processing 1 band per loop
    # Determine lower and upper cutoff frequencies
    # of the current BPF on a normalized scale.
    Wn = np.append(freq[band], freq[band+1])
    Wn = Wn / Nyq
    b, a = signal.butter(order, Wn=Wn, btype='bandpass')

    # Filter signals and store the result
    voxBands[:, band] = signal.lfilter(b, a, x)
    synthBands[:, band] = signal.lfilter(b, a, synth)

    # Envelope measurement from vocal signal
    for n in range(N):
        envBands[n, band] = (1-g) * abs(voxBands[n, band]) + g * fb
        fb = envBands[n, band]

    fb = 0

# Perform amplitude modulation
outBands = np.zeros((len(x), numBands))
for band in range(numBands):
    # Apply the envelope of the vocal signal to the synthesizer
    # in each of the bands.
    outBands[:, band] = envBands[:, band] * synthBands[:, band]

# Sum together all the bands
out = np.sum(outBands, 1)
# Make-up gain
out = 32 * out

plt.plot(out)
plt.show()

# Listen to the output and plot it
Audio(out, rate=Fs)

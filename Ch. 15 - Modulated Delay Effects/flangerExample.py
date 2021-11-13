# FLANGEREXAMPLE
# This script creates a flanger effect, applied to white noise. Within the
# processing loop, a feedback flanger can be substituted for the feedforward
# flanger used by default.
#
# See also FLANGEREFFECT

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from flangerEffect import flangerEffect
from feedbackFlanger import feedbackFlanger

Fs = 48000
Ts = 1/Fs
sec = 5
lenSamples = sec*Fs
x = 0.2 * np.random.randn(lenSamples)  # White noise input

# Create delay buffer to hold maximum possible delay samples
maxDelay = 50 + 1
buffer = np.zeros(maxDelay)

rate = 0.2  # Hz (frequency of LFO)
depth = 4  # Samples (amplitude of LFO)
predelay = 5  # Samples (offset of LFO)
wet = 50  # Wet/dry mix

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):
    # Use flangerEffect function
    out[n], buffer = flangerEffect(x[n], buffer, Fs, n, depth, rate, predelay, wet)

    # Use feedbackFlanger function
    out[n], buffer = feedbackFlanger(x[n], buffer, Fs, n, depth, rate, predelay, wet)

# Spectrogram
nfft = 2048
window = np.hanning(nfft)  # or signal.windows.hann(nfft)
overlap = 128
spec, f, t, imAxis = plt.specgram(out, nfft, Fs, window=window, noverlap=overlap)
plt.axis('tight')
plt.axis('auto')
plt.xlabel('Time (sec.)')
plt.ylabel('Freq. (Hz)')
plt.show()

Audio(out, rate=Fs)

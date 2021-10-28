# BARBERPOLEEXAMPLE
# This script creates a barber-pole flanger effect using a single delay buffer.
# The delay time is modulated byt a sawtooth LFO. There is audible distortion
# each time the LFO starts a new cycle.
#
# This script produces a plot with a delay time of the LFO and the spectrogram
# of white noise processed by the effect
#
# See also BARBERPOLE2EXAMPLE

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from barberpoleFlanger import barberpoleFlanger

Fs = 48000
Ts = 1/Fs
sec = 8
lenSamples = sec*Fs
x = 0.2 * np.random.randn(lenSamples)
t = np.arange(0, lenSamples) * Ts

# Create delay buffer to hold maximum possible delay time
maxDelay = 50 + 1
buffer = np.zeros(maxDelay)

rate = 0.5 # Hz (frequency of LFO)
depth = 6 # samples (amplitude of LFO)
predelay = 12 # samples (offset of LFO)

# Wet/dry mix
wet = 50 # 0 = only dry, 100 = only wet

# Initialize output signal
N = len(x)
out = np.zeros(N)
lfo = np.zeros(N)

for n in range(N):
    # Use barberpoleFlanger function
    out[n], buffer, lfo[n] = barberpoleFlanger(x[n], buffer, Fs, n, depth, rate, predelay, wet)

# Waveform
plt.plot(t,lfo)
plt.axis([0, len(t)*Ts, 5, 20])
plt.ylabel('Delay')
plt.show()

# Spectrogram
nfft = 2048 # Length of each time frame
window = np.hanning(nfft) # Calculated windowing function
overlap = 128 # Number of samples for frame overlap
spec, f, t, imAxis = plt.specgram(out, nfft, Fs, window=window, noverlap=overlap)
plt.axis('tight')
plt.axis('auto')
plt.xlabel('Time (sec.)')
plt.ylabel('Freq. (Hz)')
plt.show()

Audio(out, rate=Fs)
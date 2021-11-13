# BARBERPOLE2EXAMPLE
# This script creates a barber-pole flanger effect using two delay buffers,
# which gradually fades back and forth between the buffers to have a smooth
# transition at the start of the sawtooth ramp.
#
# See also BARBERPOLEEXAMPLE

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from crossfades import crossfades
from barberpoleFlanger2 import barberpoleFlanger2

Fs = 48000
Ts = 1/Fs
sec = 8
lenSamples = sec*Fs
x = 0.2 * np.random.randn(lenSamples)
t = np.arange(0, lenSamples) * Ts

# Create a delay buffer to hold maximum delay time
maxDelay = 50 + 1
buffer = np.zeros(maxDelay)

rate = 0.5  # Hz (frequency of LFO)
depth = 6  # samples (amplitude of LFO)
predelay = 12  # samples (offset of LFO)

# Wet/dry mix
wet = 50  # 0 = only dry, 100 = only wet

# Initialize output signal
N = len(x)
out = np.zeros(N)
lfo1 = np.zeros(N)
lfo2 = np.zeros(N)
overlap = 18000  # Number of samples of overlap per crossfade
g1, g2 = crossfades(Fs, lenSamples, rate/2, overlap)

for n in range(N):
    out[n], buffer, lfo1[n], lfo2[n] = barberpoleFlanger2(x[n], buffer, Fs, n, depth, rate, predelay, wet, g1[n], g2[n])

# Waveform
plt.plot(t, lfo1, t, lfo2)
plt.axis([0, len(t)*Ts, 8, 16])
plt.ylabel('Delay')
plt.show()

plt.plot(t, g1, t, g2)  # Crossfade gains
plt.ylabel('Amplitude')

# Spectrogram
nfft = 2048  # Length of each time frame
window = np.hanning(nfft)  # Calculated windowing function
overlap = 128  # Number of samples for frame overlap
spec, f, t, imAxis = plt.specgram(out, nfft, Fs, window=window, noverlap=overlap)
plt.axis('tight')
plt.axis('auto')
plt.xlabel('Time (sec.)')
plt.ylabel('Freq. (Hz)')
plt.show()

Audio(out, rate=Fs)

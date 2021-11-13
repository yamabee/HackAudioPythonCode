# AMPMODULATION
# This script provides an example for modulating the amplitude
# of a carrier signal. this process is called tremolo when used
# as an audio effect.

import numpy as np
import soundfile
import matplotlib.pyplot as plt
from IPython.display import Audio

# Import carrier signal
[carrier, Fs] = soundfile.read('sw440.wav')
Ts = 1/Fs
N = len(carrier)
t = np.arange(0, N) * Ts

plt.plot(t, carrier)
plt.title('Original Sound File')
plt.xlabel('Time (sec)')
plt.figure()

# Tremolo parameters
depth = 100  # [0, 100]
speed = 5
amp = 0.5 * (depth / 100)
offset = 1 - amp

# Synthesize modulation signal
f = speed  # speed of effect
phi = 0
sw = np.sin(2 * np.pi * f * t + phi)

mod = (amp * sw) + offset

# Plot to compare the original sine wave with the modulator
# Index only the first second of signal for visualization purposes
plt.plot(t[0:Fs], sw[0:Fs], t[0:Fs], mod[0:Fs])
plt.title('Modulator Signal')
plt.figure()

# Modulate the amplitude of the carrier by the modulator
output = carrier * mod

# Plot the output and listen to the result
plt.plot(t[0:Fs], carrier[0:Fs])
plt.title('Carrier Signal (Unprocessed)')
plt.figure()
plt.plot(t[0:44100], output[0:44100])
plt.title('Output Signal (Processed)')
plt.show()

Audio(output, rate=Fs)

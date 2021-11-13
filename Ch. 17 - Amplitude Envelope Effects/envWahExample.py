# ENVWAHEXAMPLE
# This script implements an env-wah effect using a bi-quad filter as the resonant
# LPF after analyzing the amplitude envelope of the input signal.
#
# See also BIQUADWAH

import soundfile
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from biquadWah import biquadWah

x, Fs = soundfile.read('AcGtr.wav')
Ts = 1/Fs
N = len(x)

# Initialize feedforward delay buffer
# (stores 2 previous samples of input)
ff = np.append(0, 0)  # ff[n] = n samples of delay

# Initialize feedback delay buffer
# (stores 2 previous samples of output)
fb = np.append(0, 0)  # fb[n] = n samples of delay

# Bandwidth of resonant LPF
Q = 4

# Wet/dry mix
wet = 100

# Initialize output signal
y = np.zeros(N)
# Cutoff frequency from envelope
cutoff = np.zeros(N)

# Envelope LPF parameters
alpha = 0.9995
envPreviousValue = 0

for n in range(N):
    # Envelope detection
    rect = abs(x[n])
    env = (1 - alpha) * rect + alpha * envPreviousValue
    envPreviousValue = env

    # Scale envelope for cutoff frequency of LPF
    freq = 1500 + 10000 * env

    # Use bi-quad wah effect function
    y[n], ff, fb, = biquadWah(x[n], Fs, freq, Q, ff, fb, wet)

    # Store for plotting
    cutoff[n] = freq

t = np.arange(0, N) * Ts
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)
plt.plot(t, cutoff)
plt.xlabel('Time (sec.)')
plt.ylabel('Cutoff Freq. (Hz)')

Audio(y, rate=Fs)

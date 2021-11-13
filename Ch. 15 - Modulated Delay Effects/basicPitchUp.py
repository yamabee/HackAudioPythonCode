# BASICPITCHUP
# This script demonstrates a basic example of pitch shifting up an octave
# created by using a modulated time delay.
#
# See also BASICPITCHDOWN, BASICPITCH

import numpy as np
import matplotlib.pyplot as plt

# Synthesize 1 Hz signal
Fs = 48000
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
f = 1
x = np.sin(2 * np.pi * f * t)

d = Fs                   # Initial delay time

N = len(x)               # Number of samples
y = np.zeros(N)          # Initialize output signal
buffer = np.zeros(Fs+1)  # Delay buffer

for n in range(N):
    intDelay = int(np.floor(d))
    frac = d - intDelay
    if intDelay == 0:
        y[n] = (1-frac) * x[n] + frac * buffer[0]
    else:
        y[n] = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    # Store current input in delay buffer
    buffer = np.append(x[n], buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x[n]

    # Decrease the delay time by 1 sample
    d = d - 1

plt.plot(t, x)
plt.plot(t, y)
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.legend(['Input', 'Output'])
plt.show()

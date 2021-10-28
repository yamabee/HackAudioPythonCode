# BASICPITCHDOWN
# This script demonstrates a basic example of pitch shifting down an octave
# created by using a modulated time delay.
#
# See also BASICPITCHUP, BASICPITCH

import numpy as np
import matplotlib.pyplot as plt

# Synthesize 1 Hz test signal
Fs = 48000
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
f = 1
x = np.sin(2 * np.pi * f * t)
x = np.append(x, np.zeros(Fs))

# Initialize loop for pitch decrease
d = 0   # Initially start with no delay
N = len(x)
y = np.zeros(N)
buffer = np.zeros(Fs*2)

for n in range(N):
    intDelay = int(np.floor(d))
    frac = d - intDelay
    if intDelay == 0:   # When there are 0 samples of delay
                        # 'y' is based on input 'x'
        y[n] = (1-frac) * x[n] + frac * buffer[0]
    else:   # Greater than 0 samples of delay
            # Interpolate between delayed samples "in the past"
        y[n] = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    # Store the current input in delay buffer
    buffer = np.append(x[n], buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x[n]

    # Increase the delay time by 0.5 samples
    d = d + 0.5

plt.plot(t,x[0:48000])
time = np.arange(0,len(y)) * Ts
plt.plot(time,y)
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.legend(['Input', 'Output'])
plt.show()
# BASICPITCH
# This script demonstrates a basic example of pitch shifting created by using
# a modulated time delay.

import numpy as np
import matplotlib.pyplot as plt
from plottf import plottf

Fs = 48000
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
f = 110 # Musical note A2 = 110 Hz
x = np.sin(2 * np.pi * f * t)

# Pitch shift amount
semitones = -12
tr = pow(2, (semitones/12))
dRate = 1 - tr # Delay rate of change

# Conditional to handle pitch up or pitch down
if dRate > 0: # Pitch decrease
    d = 0
    x = np.pad(x, (0, Fs), 'constant') # Prepare for signal to be elongated

else: # Pitch increase
    # Initialize delay so it is always positive
    d = len(x) * -dRate

N = len(x)
y = np.zeros(N)
buffer = np.zeros(Fs*2)
M = len(buffer) - 1
wIndex = (Fs * 2) - 1

for n in range(N):
    intDelay = int(np.floor(d)) # round down to get previous sample
    frac = d - intDelay # find fractional amount

    rIndex = wIndex - intDelay  # set location of read index

    # Ensure read index is not exceeding the length of the buffer
    if rIndex < 0:
        rIndex += M

    # Ensure read index does not go out of bounds of the buffer
    if rIndex == 0:
        y[n] = (1-frac) * buffer[rIndex] + frac * buffer[M]
    else:
        y[n] = (1-frac) * buffer[rIndex] + frac * buffer[rIndex - 1]

    # Store the current output in circular buffer
    buffer[wIndex] = x[n]
    wIndex += 1
    if wIndex > M:
        wIndex = 1

    d += dRate

plottf(x, Fs)
plt.figure()
plottf(y, Fs)

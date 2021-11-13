# RT60
# This script analyzes the RT-60 of a feedback delay network by visualizing
# an impulse response on the decibel scale.

import numpy as np
import matplotlib.pyplot as plt
from modDelay import modDelay

Fs = 48000
Ts = 1/Fs
x = np.append(1, np.zeros(5 * Fs))

# Max delay of 70ms
maxDelay = int(np.ceil(0.07 * Fs))
# Initialize all buffers
buffer1 = np.zeros(maxDelay)
buffer2 = np.zeros(maxDelay)
buffer3 = np.zeros(maxDelay)
buffer4 = np.zeros(maxDelay)

d1 = np.fix(0.0297 * Fs)
d2 = np.fix(0.0371 * Fs)
d3 = np.fix(0.0411 * Fs)
d4 = np.fix(0.0437 * Fs)

# Stautner and Puckette feedback matrix
g11 = 0
g12 = 1
g13 = 1
g14 = 0
g21 = -1
g22 = 0
g23 = 0
g24 = -1
g31 = 1
g32 = 0
g33 = 0
g34 = -1
g41 = 0
g42 = 1
g43 = -1
g44 = 0

# LFO parameters
rate1 = 0.6
amp1 = 5
rate2 = 0.71
amp2 = 5
rate3 = 0.83
amp3 = 5
rate4 = 0.95
amp4 = 5

# Initialize output signal
N = len(x)
out = np.zeros(N)

fb1 = 0
fb2 = 0
fb3 = 0
fb4 = 0

# Gain to control reverb time
g = 0.67

for n in range(N):
    # Combine input with feedback for respective delay lines
    xDL1 = x[n] + fb1
    xDL2 = x[n] + fb2
    xDL3 = x[n] + fb3
    xDL4 = x[n] + fb4

    # Four parallel delay lines
    outDL1, buffer1 = modDelay(xDL1, buffer1, Fs, n, d1, amp1, rate1)
    outDL2, buffer2 = modDelay(xDL2, buffer2, Fs, n, d2, amp2, rate2)
    outDL3, buffer3 = modDelay(xDL3, buffer3, Fs, n, d3, amp3, rate3)
    outDL4, buffer4 = modDelay(xDL4, buffer4, Fs, n, d4, amp4, rate4)

    # Combine parallel paths
    out[n] = 0.25 * (outDL1 + outDL2 + outDL3 + outDL4)

    # Calculate feedback (including crossover)
    fb1 = g * (g11*outDL1 + g12*outDL2 + g13*outDL3 + g14*outDL4)
    fb2 = g * (g21*outDL1 + g22*outDL2 + g23*outDL3 + g24*outDL4)
    fb3 = g * (g31*outDL1 + g32*outDL2 + g33*outDL3 + g34*outDL4)
    fb4 = g * (g41*outDL1 + g42*outDL2 + g43*outDL3 + g44*outDL4)

out = out/max(abs(out))  # Normalize to unity gain (0 dB)

t = np.arange(0, N) * Ts
plt.plot(t, 20 * np.log10(abs(out)))
plt.axhline(-60, color='red', linestyle='--')
plt.axis([0, 4, -80, 0])
plt.show()

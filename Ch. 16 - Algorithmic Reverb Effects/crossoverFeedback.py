# CROSSOVERFEEDBACK
# This script implements two comb filters with crossover feedback.
#
# See also MODDELAY

import numpy as np
import matplotlib.pyplot as plt
from modDelay import modDelay
from IPython.display import Audio

Fs = 48000
x = np.append(1, np.zeros(int(Fs*0.5))) # Add zero-padding for reverb tail

# Max delay of 70ms
maxDelay = int(np.ceil(0.07 * Fs))
# Initialize all buffers
buffer1 = np.zeros(maxDelay)
buffer2 = np.zeros(maxDelay)

# Early reflections tapped delay line
bufferER = np.zeros(maxDelay)

# Delay and gain parameters
d1 = np.fix(0.0297 * Fs)
g11 = -0.75
g12 = -0.75
d2 = np.fix(0.0419 * Fs)
g21 = -0.75
g22 = -0.75

# LFO parameters
rate1 = 0.6
amp1 = 3
rate2 = 0.71
amp2 = 3

# Initialize output signal
N = len(x)
out = np.zeros(N)

fb1 = 0
fb2 = 0 # feedback holding variables

for n in range(N):
    # Combine input with feedback for respective delay lines
    xDL1 = x[n] + fb1
    xDL2 = x[n] + fb2


    # Two parallel delay lines
    outDL1, buffer1 = modDelay(xDL1, buffer1, Fs, n, d1, amp1, rate1)
    outDL2, buffer2 = modDelay(xDL2, buffer2, Fs, n, d2, amp2, rate2)

    # Combine parallel paths
    out[n] = 0.5 * (outDL1 + outDL2)

    # Calculate feedback (including crossover)
    fb1 = 0.5 * (g11 * outDL1 + g21 * outDL2)
    fb2 = 0.5 * (g12 * outDL2 + g22 * outDL2)

plt.plot(out)
plt.show()

Audio(out, rate=Fs)
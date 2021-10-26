# MORPHLFO
# This script demonstrates the method of morphing the LFO signal
# for the tremolo effect from a triangle wave to a square wave.
#
# See also AMPMODULATION

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Initial parameters
Fs = 48000
Ts = 1/Fs
f = 1 # 1 Hz LFO
numSec = 1
numSamples = Fs * numSec
t = np.arange(0, numSamples) * Ts

# Consider a parameter knob with values from 1-10
knobValue = 10
lfo = signal.sawtooth(((2 * np.pi * f * t) + np.pi/2), 0.5)
N = len(lfo)
lfoShape = np.zeros(N)
for n in range(N):
    if lfo[n] >= 0:
        # This process is similar to adding an exponent
        # to a linear fade. It turns into an exponential,
        # convex curve. In this case, it turns the straight
        # line of a triangle wave into a curve closer to a
        # square wave.
        lfoShape[n] = pow(lfo[n], (1/knobValue))

    else:
        # Need to avoid using negative numbers with power function
        lfoShape[n] = -1 * pow(np.abs(lfo[n]), (1/knobValue))

plt.plot(t, (0.5*lfo)+0.5, t, (0.5*lfoShape)+0.5)
plt.legend(['Triangle, Knob = 1', 'Square, Knob = 10'])
plt.show()
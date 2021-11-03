# MODDELAY
# This function creates a series delay effect using a buffer. The delay
# time can be modulated based on the LFO parameters 'depth' and 'rate'.
#
# Input Variables
#   x: single sample of the input signal
#   buffer: used to store delayed samples of the signal
#   n: current sample used for the LFO
#   depth: range of modulation (samples)
#   rate: speed of modulation (frequency, Hz)

import numpy as np

def modDelay(x, buffer, Fs, n, delay, depth, rate):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = depth * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(np.mod(n, M)) # Current index
    indexD = int(np.mod((n-delay+intDelay), M)) # Delay index
    indexF = int(np.mod((n-delay+intDelay+1), M)) # Fractional index

    out = (1-frac) * buffer[indexD] + frac * buffer[indexF]

    # Store the current output in appropriate index
    buffer[indexC] = x

    return out, buffer
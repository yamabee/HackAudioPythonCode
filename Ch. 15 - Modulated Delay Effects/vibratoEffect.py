# VIBRATOEFFECT
# This function implements a vibrato effect based on depth and rate LFO
# parameters.
#
# Input variables
#   x: single sample of the input signal
#   buffer: used to store delayed samples of the signal
#   n: current sample number used for the LFO
#   depth: range of modulation (samples)
#   rate: speed of modulation (frequency, Hz)
#
# See also CHORUSEFFECT

import numpy as np


def vibratoEffect(x, buffer, Fs, n, depth, rate):
    # Calculate lfo for current sample
    t = n/Fs
    lfo = (depth/2) * np.sin(2 * np.pi * rate * t) + depth

    # Determine indexes for circular buffer
    N = len(buffer)
    indexC = np.mod(n, N)  # Current index in circular buffer

    fracDelay = np.mod(n-lfo, N)  # Delay index in circular buffer
    intDelay = int(np.floor(fracDelay))  # Fractional delay indices
    frac = fracDelay - intDelay

    nextSamp = np.mod(intDelay, N) - 1  # Next index in circular buffer

    out = (1-frac) * buffer[intDelay-1] + frac * buffer[nextSamp]

    # Store the current output in appropriate index
    buffer[indexC] = x

    return out, buffer

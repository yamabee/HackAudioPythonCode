# APF
# This function creates an all-pass filter by processing an individual
# input sample and updating a delay buffer used in a loop to index each
# sample in a signal.
#
# Input Variables
#   n: current sample number of the input signal
#   delay: samples of delay
#   gain: feedback gain (linear scale)
#   amp: amplitude of LFO modulation
#   rate: frequency of LFO modulation

import numpy as np

def apf(x, buffer, Fs, n, delay, gain, amp, rate):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = amp * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(np.mod(n, M)) # Current index
    indexD = int(np.mod((n-delay+intDelay), M)) # Delay index
    indexF = int(np.mod((n-delay+intDelay+1), M)) # Fractional index

    # Temp variable for output of delay buffer
    w = (1 - frac) * buffer[indexD] + frac * buffer[indexF]

    # Temp variable used for the node after the input sum
    v = x + (-gain * w)

    # Summation at output
    out = (gain * v) + w

    # Store the current input to delay buffer
    buffer[indexC] = v

    return out, buffer
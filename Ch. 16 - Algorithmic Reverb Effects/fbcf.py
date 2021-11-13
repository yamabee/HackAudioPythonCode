# FBCF
# This function creates a feedback comb filter by processing an
# individual input sample and updating a delay buffer used in a loop
# to index each sample in a signal. Fractional delay is implemented
# to make it possible to modulate the delay time.
#
# Input Variables
#   n: current sample number of the input sample
#   delay: samples of delay
#   fbGain: feedback gain (linear scale)
#   amp: amplitude of LFO modulation
#   rate: frequency of LFO modulation
#
# See also FBCFNOMOD

import numpy as np


def fbcf(x, buffer, Fs, n, delay, fbGain, amp, rate):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = amp * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(np.mod(n, M))  # Current index
    indexD = int(np.mod((n-delay+intDelay), M))  # Delay index
    indexF = int(np.mod((n-delay+intDelay+1), M))  # Fractional index

    out = (1 - frac) * buffer[indexD] + frac * buffer[indexF]

    # Store the current output in appropriate index
    buffer[indexC] = x + fbGain * out

    return out, buffer

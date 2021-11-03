# FBCFNOMOD
# This function creates a feedback comb filter by processing an individual
# input sample and updating a delay buffer used in a loop to index each
# sample in a signal. This implementation does not use fractional delay.
# Therefore, the delay time cannot be modulated.
#
# Input Variables
#   n: current sample number of the input sample
#   delay: samples of delay
#   fbGain: feedback gain (linear scale)
#
# See also FBCF

import numpy as np

def fbcfNoMod(x, buffer, n, delay, fbGain):
    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = np.mod(n, M) # Current index
    indexD = int(np.mod((n - delay)), M) # Delay index

    out = buffer[indexD]

    # Store the current output in appropriate index
    buffer[indexC] = x + fbGain * buffer[indexD]

    return out, buffer
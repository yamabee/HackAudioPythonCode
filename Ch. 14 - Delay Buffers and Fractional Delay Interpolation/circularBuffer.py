# CIRCULARBUFFER
# This function performs series delay and uses a circular buffer. Rather than
# shifting all the values in the array buffer during each iteration, the index
# changes each time through based on the current sample, 'n'.
#
# Additional input variables
#   delay: samples of delay
#   n: current sample number used for circular buffer

import numpy as np

def circularBuffer(x, buffer, delay, n):
    # Determine indexes for circular buffer
    N = len(buffer)
    indexC = np.mod(n-1, N)  # current index in circular buffer
    indexD = np.mod(n-delay-1, N)  # delay index in circular buffer

    out = buffer[indexD]
    # Store current output in appropriate index
    buffer[indexC] = x

    return out, buffer
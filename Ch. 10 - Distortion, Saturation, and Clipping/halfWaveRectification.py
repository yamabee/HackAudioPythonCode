# HALFWAVERECTIFICATION
# This function implements half-wave rectification distortion. Amplitude values
# of the input signal that are negative are changed to zero in the output signal.
#
# See also FULLWAVERECTIFICATION, DISTORTIONEXAMPLE

import numpy as np

def halfWaveRectification(x):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        if x[n] >= 0:
            # If positive, assign input to output
            y[n] = x[n]

        else:
            # If negative, set output to zero
            y[n] = 0

    return y
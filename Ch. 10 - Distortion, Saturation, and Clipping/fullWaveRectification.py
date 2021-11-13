# FULLWAVERECTIFICATION
# This function implements full-wave rectification distortion. Amplitude values
# of the input signal that are negative are changed to positive in the output
# signal.
#
# See also HALFWAVERECTIFICATION, DISTORTIONEXAMPLE

import numpy as np


def fullWaveRectification(x):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        if x[n] >= 0:
            # If positive, assign input to output
            y[n] = x[n]

        else:
            # If negative, flip input
            y[n] = (-1) * x[n]

    return y

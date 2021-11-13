# HARDCLIP
# This function implements hard-clipping distortion. Amplitude values of the
# input signal that are greater than a threshold are clipped.
#
# Input variables
#   x: signal to be processed
#   thresh: maximum amplitude where clipping occurs
#
# See also INFINITECLIP, PIECEWISE, DISTORTIONEXAMPLE

import numpy as np


def hardClipping(x, thresh):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        if x[n] >= thresh:
            # If true, assign input = thresh
            y[n] = thresh

        elif x[n] <= -thresh:
            # If true, set output = -thresh
            y[n] = -thresh

        else:
            y[n] = x[n]

    return y

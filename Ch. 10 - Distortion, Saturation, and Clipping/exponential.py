# EXPONENTIAL
# This function implements exponential soft-clipping distortion. An input
# parameter 'drive' is used to control the amount of distortion applied to
# the input signal.
#
# Input variables
#   x: input signal
#   drive: drive amount (1-10)
#
# See also CUBICDISTORTION, ARCTANDISTORTION, DISTORTIONEXAMPLE

import numpy as np


def exponential(x, drive):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        y[n] = np.sign(x[n]) * (1 - np.exp(-np.abs(drive * x[n])))

    return y

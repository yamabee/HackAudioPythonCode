# CUBICDISTORTION
# This function implements cubic soft-clipping distortion. An input parameter
# 'a' is used to control the amount of distortion applied to the input
# signal.
#
# Input variables
#   x: input signal
#   a: drive amount (0-1), amplitude of 3rd harmonic
#
# See also ARCTANDISTORTION, DISTORTIONEXAMPLE

import numpy as np


def cubicDistortion(x, a):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        y[n] = x[n] - (a * (1/3) * pow(x[n], 3))

    return y

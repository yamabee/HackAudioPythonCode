# PIECEWISE
# This function implements a piece-wise distortion algorithm. Within one
# operating region, the input signal is not distorted. When the signal is
# outside of that operating region, it is clipped.
#
# See also HARDCLIP, DISTORTIONEXAMPLE

import numpy as np

def piecewise(x):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        if np.abs(x[n]) <= 1/3:
            y[n] = 2 * x[n]
        elif np.abs(x[n]) > 2/3:
            y[n] = np.sign(x[n])
        else:
            y[n] = (np.sign(x[n])) * (pow((3 - (2 - 3 * abs(x[n]))), 2)/3)

    return y
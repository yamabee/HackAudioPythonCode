# ARCTANDISTORTION
# This function implements arctangent soft-clipping distortion. An input
# parameter 'alpha' is used to control the amount of distortion applied to
# the input signal.
#
# Input variables
#   x: input signal
#   alpha: drive amount (1-10)
#
# See also CUBICDISTORTION, DISTORTIONEXAMPLE

import numpy as np

def arctanDistortion(x, alpha):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        y[n] = (2/np.pi) * np.arctan(x[n] * alpha)

    return y
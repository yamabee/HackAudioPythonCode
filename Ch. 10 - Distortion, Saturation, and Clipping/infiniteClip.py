# INFINITECLIP
# This function implements infinite clipping distortion. Amplitude values
# of the input signal that are positive are changed to 1 in the output signal.
# Amplitude values of the input signal that are negative are changed to -1 in
# the output signal.
#
# See also HARDCLIP, DISTORTIONEXAMPLE

import numpy as np


def infiniteClip(x):
    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        # Change all amplitude values to +1 or -1 (FS amplitude)
        # 'Pin the Rails' (description in audio electronics)
        if x[n] >= 0:
            # If positive, assign output = 1
            y[n] = 1

        else:
            # If negative, assign output = -1
            y[n] = -1

    return y

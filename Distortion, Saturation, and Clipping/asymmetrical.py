# ASYMMETRICAL
# This function creates a distortion effect that is neither 'even' or 'odd'.
# Therefore, the resulting signal has both even and odd harmonics.
#
# Input variables
#   x: input signal
#   dc: offset amount
#
# See also CUBICDISTORTION, DISTORTIONEXAMPLE

import numpy as np

def asymmetrical(x, dc):
    N = len(x)
    xOffset = x + dc # introduce DC offset
    yOffset = np.zeros([N, 1])

    for n in range(N):
        if np.abs(xOffset[n]) > 1:
            # Conditional to ensure 'out' is a monotonically increasing function
            xOffset[n] = np.sign(xOffset[n])

        # Nonlinear distortion function
        yOffset[n] = xOffset[n] - (1/5) * pow(xOffset[n], 5)

    y = yOffset - dc # remove DC offset

    return y
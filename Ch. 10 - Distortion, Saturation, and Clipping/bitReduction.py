# BITREDUCTION
# This function creates a bit reduction or bit crushing distortion. It uses
# an input variable, 'nBits', to determine the number of amplitude values
# in the output signal. This algorithm can have a fractional number of bits,
# similar to the processing found in some audio plug-ins.
#
# Input variables
#   x: input signal
#   nBits: scalar for the number of desired bits
#
# See also DISTORTIONEXAMPLE, ROUND, CEIL, FLOOR, FIX

import numpy as np


def bitReduction(x, nBits):
    # Determine the desired number of possible amplitude values
    ampValues = pow(2, nBits)

    # Shrink the full-scale signal (-1 to 1, peak-to-peak) to fit
    # within range of 0 to 1
    prepInput = 0.5 * x + 0.5

    # Scale the signal to fit within the range of the possible values
    scaleInput = ampValues * prepInput

    # Round the signal to the nearest integers
    roundInput = np.round(scaleInput)

    # Invert the scaling to fit the original range
    prepOut = roundInput/ampValues

    # Fit in full-scale range
    y = 2 * prepOut - 1

    return y

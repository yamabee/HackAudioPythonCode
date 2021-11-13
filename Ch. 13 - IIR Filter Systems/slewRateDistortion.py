# SLEWRATEDISTORTION
# This function implements slew rate distortion. Frequencies
# greater than the 'maxFreq' parameter are distorted.
# Frequencies less than 'maxFreq' are not distorted. This type
# of distortion occurs in op-amps used for audio.
#
# Input variables
#   x: input signal to be processed
#   Fs: sampling rate
#   maxFreq: the limiting/highest frequency before distortion

import numpy as np


def slewRateDistortion(x, Fs, maxFreq):
    Ts = 1/Fs
    peak = 1
    slewRate = maxFreq * 2 * np.pi * peak  # convert freq. to slew rate

    slope = slewRate * Ts  # Convert slew rate to slope/sample

    out = np.zeros(np.size(x)) # Total number of samples
    prevOut = 0 # Initialize feedback delay sample

    for n in range(len(x)):
        dlta = x[n] - prevOut
        if dlta > slope:  # Dont let dlta exceed max slope
            dlta = slope
        elif dlta < -slope:
            dlta = -slope

        out[n] = prevOut + dlta
        prevOut = out[n]  # Save current 'out' for next loop

    return out

# FEEDBACKFLANGER
# This function can be used to create a feedback flanger.
#
# Input variables
#   x: single sample of the input signal
#   buffer: used to store delayed samples of the signal
#   n: current sample number used for the LFO
#   depth: range of modulation (samples)
#   rate: speed of modulation (frequency, Hz)
#   predelay: offset of modulation (samples)
#   wet: percent of processed signal (dry = 100 - wet)
#
# See also FLANGEREFFECT

import numpy as np


def feedbackFlanger(x, buffer, Fs, n, depth, rate, predelay, wet):
    # Calculate time in seconds
    t = n/Fs
    lfo = depth * np.sin(2 * np.pi * rate * t) + predelay

    # Wet/dry mix
    mixPercent = wet  # 0 = only dry, 100 = only wet
    mix = mixPercent/100

    fracDelay = lfo
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Store dry and wet signals
    drySig = x
    wetSig = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    # Blend parallel paths
    out = (1-mix)*drySig + mix*wetSig

    # Feedback is created by storing the output in the buffer
    # instead of the input.
    buffer = np.append(x, buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = out

    return out, buffer

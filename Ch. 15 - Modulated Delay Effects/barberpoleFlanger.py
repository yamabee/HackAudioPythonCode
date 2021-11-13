# BARBERPOLEFLANGER
# This function can be used to create a barber-pole flanger.
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
# See also FLANGEREFFECT, FEEDBACKFLANGER, BARBERPOLEFLANGER2

import numpy as np
from scipy import signal


def barberpoleFlanger(x, buffer, Fs, n, depth, rate, predelay, wet):
    # Calculate time in seconds for the current sample
    t = n/Fs
    lfo = depth * signal.sawtooth(2 * np.pi * rate * t, 0) + predelay

    # Wet/dry mix
    mixPercent = wet
    mix = mixPercent/100

    fracDelay = lfo
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Store dry and wet signals
    drySig = x
    wetSig = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    # Blend parallel paths
    out = (1-mix)*drySig + mix*wetSig

    buffer = np.append(x, buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x

    return out, buffer, lfo

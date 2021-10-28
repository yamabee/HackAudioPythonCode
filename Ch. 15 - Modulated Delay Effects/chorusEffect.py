# CHORUSEFFECT
# This function can be used to create a chorus audio effect.
#
# Input variables
#   x: single sample of the input signal
#   buffer: used to store delayed samples of the signal
#   n: current sample number used for the LFO
#   depth: range of modulation (milliseconds)
#   rate: speed of modulation (frequency, Hz)
#   predelay: offset of modulation (milliseconds)
#   wet: percent of processed signal (dry = 100 - wet)
#
# See also VIBRATOEFFECT, FLANGEREFFECT

import numpy as np

def chorusEffect(x, buffer, Fs, n, depth, rate, predelay, wet):
    # Calculate time in seconds for current sample
    t = n/Fs
    lfoMS = depth * np.sin(2 * np.pi * rate * t) + predelay
    lfoSamples = (lfoMS/1000) * Fs

    # Wet/dry mix
    mixPercent = wet # 0 = only dry, 100 = only wet
    mix = mixPercent/100

    fracDelay = lfoSamples
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Store dry and wet signals
    drySig = x
    wetSig = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    # Blend parallel paths
    out = (1-mix) * drySig + mix * wetSig

    # Linear buffer implemented
    buffer = np.append(x, buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x

    return out, buffer
# BARBERPOLEFLANGER2
# This function can be used to create a barber-pole flanger. Specifically,
# the function is meant to crossfade between two flangers so that the rising
# flanger has a smooth transition at the start of each sawtooth ramp.
#
# Input variables
#   x: single sample of the input signal
#   buffer: used to store delayed samples of the signal
#   n: current sample number used for the LFO
#   depth: range of modulation (samples)
#   rate: speed of modulation (frequency, Hz)
#   predelay: offset of modulation (samples)
#   wet: percent of processed signal (dry = 100 - wet)
#   g1: amplitude of the first flanger in the crossfade
#   g2: amplitude of the second flanger in the crossfade
#
# See also BARBERPOLEFLANGER

import numpy as np
from scipy import signal

def barberpoleFlanger2(x, buffer, Fs, n, depth, rate, predelay, wet, g1, g2):
    # Calculate time in seconds for the current sample
    t = n/Fs
    # Rate/2 because alternating, overlapping LFOs
    lfo1 = depth * signal.sawtooth(2 * np.pi * rate/2 * t + np.pi/6, 0)
    # Hard-clipping at a negative value creates overlap
    if lfo1 < -1:
        lfo1 = -1

    lfo1 = lfo1 + predelay - 2
    lfo2 = depth * signal.sawtooth(2 * np.pi * rate/2 * t + 7*np.pi/6, 0)
    if lfo2 < -1:
        lfo2 = -1

    lfo2 = lfo2 + predelay - 2

    # Wet/dry mix
    mixPercent = wet # 0 = only dry, 100 = only wet
    mix = mixPercent/100

    fracDelay1 = lfo1
    intDelay1 = int(np.floor(fracDelay1))
    frac1 = fracDelay1 - intDelay1

    fracDelay2 = lfo2
    intDelay2 = int(np.floor(fracDelay2))
    frac2 = fracDelay2 - intDelay2

    # Store dry and wet signals
    drySig = x
    wetSig = g1 * ((1-frac1) * buffer[intDelay1-1] + frac1 * buffer[intDelay1]) + g2 * ((1-frac2) * buffer[intDelay2-1] + frac2 * buffer[intDelay2])

    # Blend parallel paths
    out = (1-mix)*drySig + mix*wetSig

    buffer = np.append(x, buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x

    return out, buffer, lfo1, lfo2
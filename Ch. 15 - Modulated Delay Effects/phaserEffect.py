# PHASEREFFECT
# This function can be used to create a phaser audio effect.
#
# Input Variables:
#   x: single sample of the input signal
#   buffer: used to store delayed samples of the signal
#   n: current sample number used for LFO
#   depth: range of modulation (samples)
#   rate: speed of modulation (frequency, Hz)
#   wet: percent of processed signal (dry = 100 - wet)
#
# See also BIQUADPHASER

import numpy as np

def phaserEffect(x, buffer, Fs, n, depth, rate, wet):
    # Calculate time in seconds for the current sample
    t = n / Fs
    lfo = depth * np.sin(2 * np.pi * rate * t) + 2

    # Wet/dry mix
    mixPercent = wet
    mix = mixPercent / 100

    fracDelay = lfo
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Store dry and wet signals
    drySig = x

    g = 0.25
    # All-pass filter
    wetSig = g * x + ((1 - frac) * buffer[intDelay - 1] + frac * buffer[intDelay])

    # Signal parallel paths
    out = (1 - mix) * drySig + mix * wetSig

    buffer = np.append(x, buffer[0:-1])

    return out, buffer
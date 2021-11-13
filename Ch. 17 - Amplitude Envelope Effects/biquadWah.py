# BIQUADWAH
# This function can be used to create a wah-wah audio effect.
#
# Input Variables
#   x: single sample of the input signal
#   Fs: sampling rate
#   lfo: used to determine the frequency of LPF
#   ff: buffer for feedforward delay
#   fb: buffer for feedback delay
#   wet: percent of processed signal (dry = 100 - wet)
#
# Use Table 13.1 to calculate LPF bi-quad coefficients.
#
# See also BIQUADPHASER

import numpy as np


def biquadWah(x, Fs, lfo, Q, ff, fb, wet):
    # Convert value of LFO to normalized frequency
    w0 = 2 * np.pi * lfo / Fs
    # Normalize bandwidth
    alpha = np.sin(w0) / (2 * Q)

    b0 = (1 - np.cos(w0)) / 2
    b1 = 1 - np.cos(w0)
    b2 = (1 - np.cos(w0)) / 2
    a0 = 1 + alpha
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha

    # Wet/dry mix
    mixPercent = wet  # 0 - only dry, 100 - only wet
    mix = mixPercent/100

    drySig = x

    # All-pass filter
    wetSig = (b0/a0) * x + (b1/a0) * ff[0] + (b2/a0) * ff[1] - (a1/a0) * fb[0] - (a2/a0) * fb[1]

    # Blend parallel paths
    out = (1 - mix) * drySig + mix * wetSig

    # Iterate buffers for next sample
    ff[1] = ff[0]
    ff[0] = x
    fb[1] = fb[0]
    fb[0] = wetSig

    return out, ff, fb

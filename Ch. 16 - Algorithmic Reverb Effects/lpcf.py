# LPCF
# This function creates a feedback comb filter with a LPF in the feedback
# path.
#
# Input Variables
#   n: current sample number of the input signal
#   delay: samples of delay
#   fbGain: feedback gain (linear scale)
#   amp: amplitude of LFO modulation
#   rate: frequency of LFO modulation
#   fbLPF: output delayed one sample to create basic LPF
#
# See also MOORERREVERB

import numpy as np

def lpcf(x, buffer, Fs, n, delay, fbGain, amp, rate, fbLPF):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = amp * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(np.mod(n, M))  # Current index
    indexD = int(np.mod((n - delay + intDelay), M))  # Delay index
    indexF = int(np.mod((n - delay + intDelay + 1), M))  # Fractional index

    out = (1 - frac) * buffer[indexD] + frac * buffer[indexF]

    # Store the current output in appropriate index. The LPF is created
    # by adding the current output with the previous sample, both are
    # weighted 0.5.
    buffer[indexC] = x + fbGain * (0.5 * out + 0.5 * fbLPF)

    # Store the current output for the feedback LPF to be used with the
    # next sample.
    fbLPF = out

    return out, buffer, fbLPF
# CROSSFADES
# This function is used for modulated delay effects which require a crossfade
# between two different delays. The function returns the amplitude values for
# two different paths assuming a sawtooth LFO.
#
# Input variables
#   Fs: sampling rate
#   len: total length in samples for a1 and a2
#   Hz: number of fades per second
#   fade: duration of overlap in samples

import numpy as np
from scipy import signal


def crossfades(Fs, length, Hz, fade):
    period = Fs/Hz
    win = signal.windows.hann(fade*2)

    n = 0
    g1 = np.zeros(length)
    g2 = np.zeros(length)
    while n < length:
        # Position of 'n' relative to a cycle
        t = n % period
        if t < period/2 - fade:  #fade/2
            g1[n] = 1
            g2[n] = 0
            c = 0
        elif t < period/2: #+ fade/2  # first fade
            g1[n] = pow(win[fade+c], 0.5)
            g2[n] = pow(win[c], 0.5)
            c = c + 1
        elif t < period - fade:
            g1[n] = 0
            g2[n] = 1
            c = 0
        else: # 2nd fade
            g1[n] = pow(win[c], 0.5)
            g2[n] = pow(win[fade+c], 0.5)
            c = c + 1

        n = n + 1

    return g1, g2

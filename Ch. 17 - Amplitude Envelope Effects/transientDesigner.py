# TRANSIENTDESIGNER
# This function implements the transient designer audio effect. First, a detection
# analysis is performed to determine the sections of the signal that should be
# labeled 'attack' and 'sustain'. Then the amplitude of these sections is scaled
# based on the input parameters.
#
# Input Variables
#   attack: amount to change transient (-1 dec, 0 unity, +1 inc)
#   sustain: amount to change sustain
#
# See also TRANSIENTANALYSIS

import numpy as np

def transientDesigner(x, attack, sustain):
    N = len(x)
    # Initialize filtering parameters
    gFast = 0.9991 # Feedback gain for the 'fast' envelope
    fbFast = 0 # Variable used to store previous envelope value
    gSlow = 0.9999 # Feedback gain for 'slow' envelope
    fbSlow = 0

    envFast = np.zeros(N)
    envSlow = np.zeros(N)
    differenceEnv = np.zeros(N)

    # Measure fast and slow envelopes
    for n in range(N):
        envFast[n] = (1-gFast) * 2 * abs(x[n]) + gFast * fbFast
        fbFast = envFast[n]

        envSlow[n] = (1-gSlow) * 3 * abs(x[n]) + gSlow * fbSlow
        fbSlow = envSlow[n]

        # Create the difference envelope between 'fast' and 'slow'
        differenceEnv[n] = envFast[n] - envSlow[n]
        # Note: difference envelope will have a positive value when
        # envFast is greater than envSlow. This occurs when the signal
        # is in 'attack'. If the difference envelope is negative, then
        # the signal is in 'sustain'.

    attEnv = np.zeros(N)
    susEnv = np.zeros(N)

    # Separate attack and sustain envelopes
    for n in range(N):
        if differenceEnv[n] > 0: # 'Attack' section
            attEnv[n] = (attack * differenceEnv[n]) + 1
            susEnv[n] = 1 # No change
        else:
            attEnv[n] = 1 # No change
            susEnv[n] = (sustain * -differenceEnv[n]) + 1

    # Apply the attack and sustain envelopes
    out = (x * attEnv) * susEnv

    return out
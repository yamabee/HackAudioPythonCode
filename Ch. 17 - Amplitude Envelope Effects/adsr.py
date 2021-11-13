# ADSR
# This function can be used to apply an ADSR envelope on to an input signal.
#
# Input Variables
#   attackTime: length of attack ramp in milliseconds
#   decayTime: length of decay ramp in milliseconds
#   sustainAmplitude: linear amplitude of sustain segment
#   releaseTime: length of release ramp in ms

import numpy as np

def adsr(x, Fs, attackTime, decayTime, sustainAmplitude, releaseTime):
    # Convert time inputs to seconds
    attackTimeSec = attackTime/1000
    decayTimeSec = decayTime/1000
    releaseTimeSec = releaseTime/1000

    # Convert seconds to samples and determine sustain time
    a = int(np.round(attackTimeSec * Fs))   # Round each to an integer
    d = int(np.round(decayTimeSec * Fs))    # number of samples.
    r = int(np.round(releaseTimeSec * Fs))
    s = len(x) - (a + d + r) # determine length of sustain

    # Create linearly spaced fades for A, D, and R. Create hold for S.
    aFade = np.linspace(0, 1, a)
    dFade = np.linspace(1, sustainAmplitude, d)
    sFade = sustainAmplitude * np.ones(s)
    rFade = np.linspace(sustainAmplitude, 0, r)

    # Concatenates total ADSR envelope
    env = np.append(aFade, dFade)
    env = np.append(env, sFade)
    env = np.append(env, rFade)

    # Applies ADSR shaping to x
    y = x * env

    return y
# DIODE
# This function implements the Shockley ideal diode equation for audio signals
# with an amplitude between -1 and 1 FS.
#
# See also ASYMMETRICAL, DISTORTIONEXAMPLE

import numpy as np

def diode(x):
    # Diode Characteristics
    Vt = 0.0253 # thermal voltage
    eta = 1.68 # emission coefficient
    Is = 0.105 # saturation current

    N = len(x)
    y = np.zeros([N, 1])

    for n in range(N):
        y[n] = Is * (np.exp(0.1 * x[n]/(eta * Vt)) - 1)

    return y
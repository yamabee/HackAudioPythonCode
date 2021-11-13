# FEEDBACKDELAY
# This function performs feedback delay by processing an individual input sample
# and updating a delay buffer used in a loop to index each sample in a signal.
#
# Additional input variables
#   delay: samples of delay
#   fbGain: feedback gain (linear scale)

import numpy as np


def feedbackDelay(x, buffer, delay, fbGain):
    out = x + fbGain * buffer[delay-1]

    # Store the current output in appropriate index
    buffer = np.append(out, buffer[0:-1])

    return out, buffer

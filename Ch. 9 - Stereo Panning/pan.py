# PAN
# This function pans a mono audio signal in a stereo field. It is implemented
# such that it can pan th entire signal to one location if 'panValue' is a scalar.
# It can also be used for auto-pan effects if 'panValue' is an array.
#
# Input Variables
# panType: 1 = linear, 2 = sqRt, 3 = sine law
# panValue: (-100 to 100) transformed to a scale of (0-1)

import numpy as np


def pan(x, panValue, panType):
    # Convert pan value to a normalized scale
    panTransform = (panValue/200) + 0.5

    # Conditional statements determining panType
    if panType == 1:
        leftAmp = 1 - panTransform
        rightAmp = panTransform

    elif panType == 2:
        leftAmp = np.sqrt(1 - panTransform)
        rightAmp = np.sqrt(panTransform)

    elif panType == 3:
        leftAmp = np.sin((1 - panTransform) * (np.pi/2))
        rightAmp = np.sin(panTransform * (np.pi/2))

    leftChannel = leftAmp * x
    rightChannel = rightAmp * x

    return [leftChannel, rightChannel]

# GONIOMETER
#
# This function analyzes a stereo audio signal and creates a goniometer plot.
# This visualization indicates the stereo width of a signal.
#
# Values along the vertical axis represent parts of the signal in the middle
# (or center) of the stereo field. This occurs when the left and right channels
# are identical. Conversely, values along the horizontal axis represent parts
# of the signal when the left and right channels have opposite polarities.
#
# Values at an angle of 45 degrees represent when there is a signal panned to
# the right channel and to the left channel has zeros amplitude. Similarly,
# values at an angle of 135 degrees represent when there is a signal panned
# to the left channel and the right channel has zero amplitude.
#
# See also GONIOMETEREXAMPLE

import numpy as np
import matplotlib.pyplot as plt

def goniometer(input):
    input = np.transpose(input)
    N = len(input)
    x = np.zeros([N, 1])
    y = np.zeros([N, 1])

    for n in range(N):
        L = input[n][0]
        R = input[n][1]

        radius = np.sqrt(pow(L, 2) + pow(R, 2))
        angle = np.arctan2(L, R)
        angle = angle + (np.pi/4) #  Rotate by convention

        x[n] = radius * np.cos(angle)
        y[n] = radius * np.sin(angle)

    plt.axline((-1, 0), (1, 0), color='dimgrey')
    plt.axline((0, -1), (0, 1), color='dimgrey')
    plt.axline((-1, 1), (1, -1), color='dimgrey')
    plt.axline((-1, -1), (1, 1), color='dimgrey')

    # Circle
    th = np.arange(0, 2 * np.pi, np.pi/50)
    xunit = np.cos(th)
    yunit = np.sin(th)
    plt.plot(xunit, yunit, color='dimgrey')

    # Left
    xL = -0.75
    yL = 0.8
    txtL = 'L'
    plt.text(xL, yL, txtL, color='dimgrey')

    # Right
    xR = 0.73
    yR = 0.8
    txtR = 'R'
    plt.text(xR, yR, txtR, color='dimgrey')

    # Mid
    xM = -0.018
    yM = 0.96
    txtM = 'M'
    plt.text(xM, yM, txtM, color='dimgrey')

    # Side
    xS = -0.98
    yS = 0
    txtS = 'S'
    plt.text(xS, yS, txtS, color='dimgrey')

    # Plot data
    plt.plot(x, y, '.r')
    plt.axis([-1, 1, -1, 1])
    plt.show()
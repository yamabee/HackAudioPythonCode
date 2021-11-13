# EARLYREFLECTIONS
# This function creates a tapped delay line to be used for the early
# reflections of a reverb algorithm. THe delays and gains of the taps
# are included in this function and were based on an IR measurement from a
# recording studio in Nashville, TN.
#
# Also see MOORERREVERB

import numpy as np


def earlyReflections(x, buffer, Fs, n):
    # Delay times converted from milliseconds
    delayTimes = [np.fix(0 * Fs), np.fix(0.01277 * Fs), np.fix(0.01283 * Fs), np.fix(0.01293 * Fs),
                  np.fix(0.01333 * Fs), np.fix(0.01566 * Fs), np.fix(0.02404 * Fs), np.fix(0.02679 * Fs),
                  np.fix(0.02731 * Fs), np.fix(0.02737 * Fs), np.fix(0.02914 * Fs), np.fix(0.02920 * Fs),
                  np.fix(0.02981 * Fs), np.fix(0.03389 * Fs), np.fix(0.04518 * Fs), np.fix(0.04522 * Fs),
                  np.fix(0.04527 * Fs), np.fix(0.05452 * Fs), np.fix(0.06958 * Fs)]

    numDelays = len(delayTimes)
    for delay in range(numDelays):
        delayTimes[delay] = int(delayTimes[delay])

    # There must be a 'gain' for each of the 'delayTimes'
    gains = [1, 0.1526, -0.4097, 0.2984, 0.1553, 0.1442,
             -0.3124, -0.4176, -0.9391, 0.6926, -0.5787, 0.5782,
             0.4206, 0.3958, 0.3450, -0.5361, 0.417, 0.1948, 0.1548]

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = np.mod(n, M)  # current index
    buffer[indexC] = x

    out = 0  # initialize the output to be used in loop

    # Loop through all the taps
    for tap in range(len(delayTimes)):
        # Find the circular buffer index for the current tap
        indexTDL = np.mod(n - delayTimes[tap], M)

        # 'Tap' the delay line and add current tap with output
        out = out + gains[tap] * buffer[indexTDL]

    return out, buffer

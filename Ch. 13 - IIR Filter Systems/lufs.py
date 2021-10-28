# LUFS
# This function calculates the loudness of a mono or stereo
# audio signal based on the LUFS/LKFS standard. The analysis
# involves multiple steps. First, the input signal is
# processed using the pre-filter followed by the RLB filter.
# Then, a mean-square calculation is performed. Finally,
# all the channels are summed together and loudness is converted
# to units of decibels (dB).
#
# See also LUFSEXAMPLE

import numpy as np
from scipy import signal

def lufs(x):
    # Number of samples
    N = len(x)
    # Determine whether mono or stereo
    numChannels = len(x.shape)

    # Initialize pre-filter
    b0 = 1.53512485958697
    a1 = -1.69065929318241
    b1 = -2.69169618940638
    a2 = 0.73248077421585
    b2 = 1.19839281085285
    a0 = 1

    b = [b0, b1, b2]
    a = [a0, a1, a2]

    # Perform pre-filtering
    w = np.zeros(np.shape(x))
    for channel in range(numChannels): # Loop in case it is stereo
        if numChannels == 1:
            w = signal.lfilter(b, a, x)
        elif numChannels == 2:
            w[:, channel] = signal.lfilter(b, a, x[:, channel])

    # RLB filter
    b0 = 1.0
    a1 = -1.99004745483398
    b1 = -2.0
    a2 = 0.99007225036621
    b2 = 1.0
    a0 = 1

    b = [b0, b1, b2]
    a = [a0, a1, a2]

    # Perform RLB filtering
    y = np.zeros(np.shape(x))
    for channel in range(numChannels):
        if numChannels == 1:
            y = signal.lfilter(b,a, w)
        elif numChannels == 2:
            y[:, channel] = signal.lfilter(b, a, w[:, channel])

    # Perform mean-square amplitude analysis
    z = np.zeros([1, numChannels])
    for channel in range(numChannels):
        # Add together the square of the samples
        # then divide by the number of samples
        if numChannels == 1:
            z = np.sum(pow(y, 2))/N
        elif numChannels == 2:
            z[:, channel] = np.sum(pow(y[:, channel], 2)) / N

    # Determine loudness (dB) by summing all channels
    loudness = -0.691 + 10 * np.log10(np.sum(z))

    return loudness
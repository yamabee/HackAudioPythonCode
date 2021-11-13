# COMPRESSOR
# This function implements a dynamic range compressor with separate attack and
# release times. To visualize the results, code is included at the end of the
# function to plot the input signal and the compressed output signal. As a default,
# this code is commented so it does not create a plot each time the function
# is called.
#
# Input Variables
#   T: threshold relative to 0 dBFS
#   R: ratio (R to 1)
#   attackTime: units of seconds
#   releaseTime: units of seconds
#
# See also COMPRESSOREXAMPLE, BASICCOMP

import numpy as np
import matplotlib.pyplot as plt


def compressor(x, Fs, T, R, attackTime, releaseTime):
    N = len(x)
    y = np.zeros(N)
    lin_A = np.zeros(N)

    # Initialize separate attack and release times
    alphaA = np.exp(-np.log(9)/(Fs * attackTime))
    alphaR = np.exp(-np.log(9)/(Fs * releaseTime))

    gainSmoothPrev = 0  # Initialize smoothing variable

    # Loop over each sample to see if it is above thresh
    for n in range(N):
        # Turn the input signal into unipolar signal on the dB scale
        x_uni = abs(x[n])
        x_dB = 20 * np.log10(x_uni/1)
        # Ensure there are no values of negative infinity
        if x_dB < -96:
            x_dB = -96

        # Static characteristics
        if x_dB > T:
            gainSC = T + (x_dB - T)/R  # Perform downwards compression
        else:
            gainSC = x_dB  # Do not perform compression

        gainChange_dB = gainSC - x_dB

        # Smooth over the gainChange
        if gainChange_dB < gainSmoothPrev:
            # attack mode
            gainSmooth = ((1 - alphaA) * gainChange_dB) + (alphaA * gainSmoothPrev)

        else:
            # release
            gainSmooth = ((1 - alphaR) * gainChange_dB) + (alphaR * gainSmoothPrev)

        # Convert to linear amplitude scalar
        lin_A[n] = pow(10, gainSmooth/20)

        # Apply linear amplitude to input sample
        y[n] = lin_A[n] * x[n]

        # Update gainSmoothPrev used in the next sample of the loop
        gainSmoothPrev = gainSmooth

    # Uncomment for visualization
    t = np.arange(0, N)/Fs
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.title('Input')
    plt.axis([0, t[-1], -1.1, 1.1])
    plt.subplot(2, 1, 2)
    plt.plot(t, y, t, lin_A)
    plt.title('Output')
    plt.axis([0, t[-1], -1.1, 1.1])
    plt.legend(['Output Signal', 'Gain Reduction'])
    plt.show()

    return y

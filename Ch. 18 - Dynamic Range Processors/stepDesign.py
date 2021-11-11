# STEPDESIGN
# This function can be used to design a second-order
# system with specified step response characteristics.
#
# Input Variables
#   Fs: sampling rate
#   OS: percent overshoot
#   T: time in seconds of "characteristic"
#   characteristic: 'pk' (peak) or 'ss' (settling time)

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def stepDesign(Fs, OS, T, characteristic):
    if OS < 0.00001: # Ensure a minimum value of overshoot
        OS = 0.00001

    # Convert percent overshoot to damping
    L = -np.log(OS/100)/np.sqrt(pow(np.pi, 2) + (pow(np.log(OS/100), 2)))

    # Find 'wn' - undamped natural frequency
    # based on characteristic type
    if characteristic == 'pk':
        # Peak time
        wn = np.pi/(T * np.sqrt(1-pow(L, 2)))
    elif characteristic == 'st':
        # Setting time (0.02 of steady-state)
        wn = -np.log(0.02 * np.sqrt(1-pow(L, 2))) / (L * T)

    else:
        # Return invalid type
        print('Please enter a characteristic, "pk" - peak, "st" - settling time')
        return

    # Continuous Filter:
    #
    #                   (wn)^2
    # H(s) = -----------------------------
    #           s^2 + 2*L*wn + (wn)^2
    #

    num = pow(wn, 2)
    den = [1, 2*L*wn, pow(wn, 2)]

    # Perform bilinear transform on continuous system
    # to find discrete system
    b, a = signal.bilinear(num, den, Fs)

    # Plot the step response
    # n = 2 * Fs
    # inst = signal.dlti(b, a, dt=1/Fs)
    # t, h = signal.dstep(inst, n=n)
    # phi = np.arctan(L/np.sqrt(1-pow(L, 2)))
    # yStep = 1 - np.exp(-L*wn*t) * np.cos(wn * np.sqrt(1-pow(L,2) * t - phi) / (np.sqrt(1-pow(L,2)))
    # plt.plot(t, yStep)

    return b, a
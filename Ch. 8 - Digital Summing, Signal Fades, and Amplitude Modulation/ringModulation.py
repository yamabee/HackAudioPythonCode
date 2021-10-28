# FIX THIS SCRIPT!!!!

# RINGMODULATION
# This script demonstrates the result of performing ring
# modulation with two different frequencies.
#
# By multiplying 300 Hz with 100 Hz the result is a signal
# with two harmonics.
# 200 Hz (300 - 100) and 400 Hz (300 + 100)

import numpy as np
import matplotlib.pyplot as plt
from plottf import plottf

# Initialize parameters
Fs = 48000
Ts = 1/Fs
lenSec = 2
N = lenSec * Fs
fHigh = 300
fLow = 100

# Synthesize signals and perform element-wise multiplication
x = np.zeros([N, 1])
for n in range(N):
    t = n * Ts
    x[n] = np.sin(2 * np.pi * fLow * t) * np.sin(2 * np.pi * fHigh * t)

# t = np.arange(0, Fs) * Ts
# plt.subplot(211)
# plt.plot(x)
# plt.xlabel('Time (sec)')
# plt.ylabel('Amplitude')
# plt.title('Ring Modulation')

plottf(x, Fs)
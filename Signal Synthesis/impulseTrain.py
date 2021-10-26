# IMPULSETRAIN
# This script demonstrates a method to create an impulse train
# signal. Initially, all values of the signal are set to zero.
# Then, individual samples are changed to a value of 1 based
# on the length of a cycle's period.

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
from plottf import plottf

# Example - Impulse Train Signal
# 5 Hz signal for visualization
Fs = 20
f = 5
Ts = 1/Fs
t = np.arange(0, Fs) * Ts  # time vector

impTrain = np.zeros(np.size(t))  # Initialize to all zeros
period = round(Fs/f)  # # of samples/cycle
# Change the single sample at the start of cycle to 1
impTrain[0::period] = 1
plt.stem(t, impTrain)
plt.axis([0, 1, -0.1, 1.1])
plt.show()

# Example - 440 Hz signal for audition
f = 440
Fs = 48000
Ts = 1/Fs
t = np.arange(0,3*Fs) * Ts
it = np.zeros(np.size(t))
period = round(Fs/f)  # # of samples/cycle
it[0::period] = 1
Audio(it, rate=Fs)  # Listen to signal

# 50 Hz signal for spectrum plot
f = 50
Fs = 48000
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
it = np.zeros(np.size(t))
period = round(Fs/f)  # # of samples/cycle
it[0::period] = 1

plottf(it, Fs)

# POLARITYINVERSION
# This script demonstrates the process of inverting the polarity
# of a signal. It is performed by multiplying the signal by -1.

import soundfile
import numpy as np
import matplotlib as plt

# 20 Hz signal for visualization
filename = 'sw20.wav'
[x, Fs] = soundfile.read(filename)
Ts = 1/Fs # Sampling period
N = len(x) # Total number of samples in signal
t = np.arange(0, N) * Ts
# Polarity inversion
y = -1 * x
plt.plot(t,x,t,y) # Plot the original signal and the processed
# signal. The processed signal should be a 'mirror image'
# version of the original reflected across the horizontal axis.
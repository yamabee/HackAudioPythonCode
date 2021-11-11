# STEPRESPONSE
# This script demonstrates the dstep(b,a) from the scipy library. The step response
# for several first-order systems is compared using different feedback gains.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 48000 # Initialize the sampling rate
sec = 1 # Time length in seconds
n = sec * Fs # Convert second to number or samples

# Define different gain values to test
gains = [0.9990, 0.9995, 0.9997, 0.9999]

# Determine new step response each time through the loop
for element in range(len(gains)):
    alpha = gains[element]
    b = (1-alpha)
    a = [1, -alpha]
    inst = signal.dlti(b, a, dt=1/Fs)
    t, h = signal.dstep(inst, n=n)
    plt.plot(t, np.squeeze(h))

plt.axis([0, sec, -0.1, 1.1])
plt.xlabel('Time (sec.)')
plt.legend(['0.9990', '0.9995', '0.9997', '0.9999'])
plt.show()
# SCALEAMP
# This script demonstrates two methods for scaling the amplitude
# of a signal. The first method uses a loop to perform element-wise
# indexing of the input signal. The second method uses element-wise
# multiplication of an array.

import soundfile
import numpy as np
import matplotlib.pyplot as plt

# Import input signal
filename = 'sw20.wav'
[x, Fs] = soundfile.read(filename)  # input signal

Ts = 1/Fs
N = len(x)
# Time vector for plotting
t = np.arange(0, N) * Ts

# Example 1 - loop
g1 = 0.5  # Gain Scalar
y1 = np.zeros(N)

# n - variable for sample number
for n in range(N):
    # Multiply each element of 'x' by 'g1'
    y1[n] = g1 * x[n]
plt.figure(1)
plt.plot(t, x, '--', t, y1)
plt.legend(['x', '0.5*x'])

# Example 2 - array operation
g2 = 0.25

# In this approach, it is not necessary to use a loop to index
# the individual elements of 'x'. By default, this operation
# performs element-wise processing.
y2 = g2 * x

plt.figure(2)
plt.plot(t, x, t, y2)
plt.show()

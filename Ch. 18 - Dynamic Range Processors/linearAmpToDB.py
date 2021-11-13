# LINEARAMPTODB
# This script demonstrates the process of converting the linear amplitude of a signal
# to a decibel scale. An additional step is included to prevent values of a negative
# infinity from happening.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1) * 0.01  # Linear amplitude values over FS range
N = len(x)
x_dB = np.zeros(N)

for n in range(N):
    x_dB[n] = 20 * np.log10(abs(x[n]))  # convert to dB
    if x_dB[n] < -144:  # Conditional to prevent values of negative infinity
        x_dB[n] = -144  # or anything below noise floor

plt.plot(x_dB)
plt.show()
# This plot shows the result of the initial block in the detection path converting
# a linear amplitude to a decibel amplitude.

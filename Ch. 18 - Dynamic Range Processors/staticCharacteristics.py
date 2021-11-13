# STATICCHARACTERISTICS
# This script demonstrates how to use the static characteristics of a compressor as
# part of the detection path. At the end of the script, the characteristic curve is
# plotted for the static characteristics.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1000) * 0.001  # Simple input signal
N = len(x)
# Initialize static characteristics
T = -12  # Threshold (dBFS)
R = 4  # Ratio (4:1)

x_dB = np.zeros(N)
g_sc = np.zeros(N)

for n in range(N):
    x_dB[n] = 20 * np.log10(abs(x[n]))
    if x_dB[n] < -144:
        x_dB[n] = -144

    # Comparison to threshold
    if x_dB[n] > T:
        # Perform compression
        g_sc[n] = T + ((x_dB[n] - T)/R)
    else:
        # Do not compress
        g_sc[n] = x_dB[n]

plt.plot(x_dB, g_sc)  # Compressor characteristic curve plot
plt.xlabel('Input Amplitude (dBFS)')
plt.ylabel('Output Amplitude (dBFS)')
plt.show()

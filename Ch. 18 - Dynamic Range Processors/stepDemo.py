# STEPDEMO
# This script demonstrates the process of measuring the step response of a
# first-order, feedback LPF. A plot is created showing a comparison between the
# input step signal and the output response.

import numpy as np
import matplotlib.pyplot as plt

# Initialize the sampling rate
Fs = 48000
Ts = 1/Fs

# Create step input signal
x = np.append(np.zeros(Fs), np.ones(Fs))
N = len(x)

# Initialize gain value
alpha = 0.9995  # Also try values between 0.999-0.9999
q = 0  # Initialize feedback variable

y = np.zeros(N)

for n in range(N):
    y[n] = (1 - alpha) * x[n] + alpha * q
    q = y[n]  # Stores the 'previous' value for the next loop cycle

t = np.arange(0, N) * Ts  # time vector for plot
plt.plot(t, x, t, y)
plt.axis([0, 2, -0.1, 1.1])
plt.xlabel('Time (sec.)')
plt.legend(['Step Input', 'Output'])
plt.show()

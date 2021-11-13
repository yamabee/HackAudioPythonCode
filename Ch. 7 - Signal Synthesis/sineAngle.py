# SINEANGLE
# This script demonstrates a method to synthesize sine waves
# using an angle of rotation
#
# See also SINESYNTHESIS

import matplotlib.pyplot as plt
import numpy as np

# Declare initial parameters
f = 2  # frequency in Hz
phi = 0  # phase offset
Fs = 1000  # sampling rate
Ts = 1/Fs  # sample period
lenSec = 1  # seconds
N = Fs * lenSec  # number of samples
t = np.arange(0, N) * Ts  # array of sample times

# Calculate angle of rotation
angleChange = f*Ts*2*np.pi
currentAngle = phi

out = np.zeros([N, 1])
# Update the value of the currentAngle each iteration through loop
for n in range(N):
    out[n][0] = np.sin(currentAngle)
    # Update phase angle for next loop
    currentAngle += angleChange

    if currentAngle > 2 * np.pi:  # Ensure angle is not > 2*pi
        currentAngle -= 2 * np.pi

# Plot synthesized signal
plt.plot(t, out)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.legend(['out'])
plt.show()

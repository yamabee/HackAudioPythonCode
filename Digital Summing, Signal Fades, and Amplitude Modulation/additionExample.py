# ADDITIONEXAMPLE
# This script provides two examples for combining signals
# together using addition.
#
# The first example is for signals of the same frequency and
# phase.
#
# The second example is for signals of different frequencies.
#
# See also SUBTRACTIONEXAMPLE

import numpy as np
import matplotlib.pyplot as plt

# Example 1 - Same Frequencies
# Declare initial variables
f = 1
a = 1
phi = 0
Fs = 100
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
sw1 = a * np.sin((2 * np.pi * f * t) + phi)
sw2 = a * np.sin((2 * np.pi * f * t) + phi)

N = len(sw1)
sw3 = np.zeros([N,1])
# Loop through arrays to perform element-wise addition
for n in range(N):
    sw3[n] = sw1[n] + sw2[n]

# Plot the result
plt.plot(t, sw1, '--', t, sw2, ':', t, sw3)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Addition of 2 Sine Waves - Same Freq.')
plt.legend(['SW1', 'SW2', 'SW1 + SW2'])
plt.show()

# Example 2 - Different frequencies
# Declare initial parameters
f = 1
a = 1
phi = 0
Fs = 100
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
sw1 = a * np.sin((2 * np.pi * f * t) + phi)
sw2 = a * np.sin((2 * np.pi * (f*2) * t) + phi) # Change frequency x2

sw3 = sw1 + sw2

plt.plot(t, sw1, '--', t, sw2, ':', t, sw3)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Addition of 2 Sine Waves - Diff. Freq.')
plt.legend(['SW1', 'SW2', 'SW1 + SW2'])
plt.show()
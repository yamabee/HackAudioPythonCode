# SUBTRACTIONEXAMPLE
# This script provides two examples for combining signals
# together using subtraction.
#
# The first example is for signals of the same frequency and
# phase.
#
# The second example shows the addition of signals where one
# signal has a phase offset of 180 degrees (pi radians).
#
# See also ADDITIONEXAMPLE

import numpy as np
import matplotlib.pyplot as plt

# Example 1 - Same frequency and phase
# Declare initial parameters
f = 1
a = 1
phi = 0
Fs = 100
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
sw1 = a * np.sin((2 * np.pi * f * t) + phi)
sw2 = a * np.sin((2 * np.pi * f * t) + phi)
# Element-wise subtraction
sw3 = sw2 - sw1
# Plot the result
plt.plot(t, sw1, '--', t, sw2, ':', t, sw3)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Subtraction of 2 Sine Waves - Same Freq.')
plt.legend(['SW1', 'SW2', 'SW1 + SW2'])
plt.show()

# Example 2 - Same frequency with a phase offset
f = 1
a = 1
phi = 0
Fs = 100
Ts = 1/Fs
t = np.arange(0, Fs) * Ts
sw1 = a * np.sin((2 * np.pi * f * t) + phi)
sw2 = a * np.sin((2 * np.pi * f * t) + np.pi) # Phase offset by 180 degrees
sw3 = sw1 + sw2

plt.plot(t, sw1, '--', t, sw2, ':', t, sw3)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Subtraction of 2 Sine Waves - Same Freq.')
plt.legend(['SW1', 'SW2', 'SW1 + SW2'])
plt.show()
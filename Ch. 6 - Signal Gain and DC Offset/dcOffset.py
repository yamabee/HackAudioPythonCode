# DCOFFSET
# This script demonstrates a method to perform element-wise
# scalar addition, the equivalent of a DC offset

import numpy as np
import matplotlib.pyplot as plt
import soundfile

# Example - Sine wave signal
[x, Fs] = soundfile.read('sw20.wav')  # import sound file
Ts = 1/Fs
# Assign input to out1, for comparison purposes
out1 = x

N = len(x)
out2 = np.zeros(N)  # Initialize output array

# Loop through arrays to perform element-wise scalar addition
for n in range(N):
    out2[n] = x[n] + 1

# Element-wise addition can also be accomplished by adding a
# scalar directly to an array.
out3 = x - 0.5

plt.figure(1)  # Create new figure window
# Plot the output amplitude vs. time
t = np.arange(0, N) * Ts
plt.plot(t, out1, t, out2, t, out3)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.legend(['out = x', 'out2 = x + 1', 'out3 = x - 0.5'])

plt.figure(2)
# Plot the input vs. output
plt.plot(x, out1, x, out2, x, out3)
plt.xlabel('Input Amplitude')
plt.ylabel('Output Amplitude')
plt.legend(['out1 = x', 'out2 = x + 1', 'out3 = x - 0.5'])
# Draw axes through origin
plt.axhline(0)
plt.axvline(0)
plt.show()

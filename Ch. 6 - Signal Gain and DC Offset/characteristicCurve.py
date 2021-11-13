# CHARACTERISTICCURVE
# This script provides two examples for analyzing the
# characteristic curve of an audio effect which uses
# element-wise processing.
#
# This first example creates an input array with values
# from -1 to 1. The second example uses a sine wave signal.

import soundfile
import numpy as np
import matplotlib.pyplot as plt

# Example 1: Array [-1 to 1] to span entire full-scale range
input = np.arange(-1, 1, 0.1)

# Example 2: Sine wave test signal. This example shows the
# characteristic curve can be created using any signal which
# spans the full-scale range, even if it is periodic.
# Uncomment this code to switch examples.
# input, Fs = soundfile.read('sw20.wav')

# Assign input to out1, for comparison purposes
out1 = input  # no amplitude change

N = len(input)
out2 = np.zeros(N)
# Loop through arrays to perform element-wise multiplication
for n in range(N):
    out2[n] = 2 * input[n]

# Element-wise multiplication can also be accomplished by
# multiplying an array directly by a scalar
out3 = 3 * input

# Plot the characteristic curve (Input vs. Output)
plt.plot(input, out1, input, out2, input, out3)
plt.xlabel('Input Amplitude')
plt.ylabel('Output Amplitude')
plt.legend(['out1 = input', 'out2 = 2 * input', 'out3 = 3 * input'])
# Draw axes through origin
plt.axhline(0)
plt.axvline(0)
plt.show()

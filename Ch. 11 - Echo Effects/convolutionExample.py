# CONVOLUTIONEXAMPLE
# This script demonstrates the numpy convolution function - y = np.convolve(x, h)
# The example demonstrated is with a single cycle of a sine wave. When the sine
# wave is convolved with the impulse response for an echo effect, the output
# signal has delayed copies of the sine wave at different amplitudes at
# different times.
#
# See also CONV

import soundfile
import numpy as np
import matplotlib.pyplot as plt

# Import previously saved IR
[h, Fs] = soundfile.read('impResp.wav')
N = len(h)

# Synthesize input signal
f = 4
t = np.arange(0, N*0.125)/Fs
sinWave = np.sin(2 * np.pi * f * t)
pad = np.zeros([int(N*0.875)])
x = np.concatenate((sinWave, pad))

# Perform convolution
y = np.convolve(x, h)

# Plot signals
xAxis = np.arange(0, N)/Fs
plt.subplot(3, 1, 1)
plt.plot(xAxis, x)
plt.axis([-0.1, 2, -1.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Input Signal - x[n]')

plt.subplot(3, 1, 2)
plt.stem(xAxis, h)
plt.axis([-0.1, 2, -1.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Impulse Response')

plt.subplot(3, 1, 3)
plt.plot(xAxis, y[0:Fs*2])
plt.axis([-0.1, 2, -1.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Output Signal - y[n]')

plt.show()

# IMPFIR
# This script demonstrates one example to measure the impulse response of an
# FIR system.
#
# See also IMPIIR

import numpy as np
import matplotlib.pyplot as plt
import soundfile

Fs = 48000
N = Fs * 2
# Synthesize the impulse signal
imp = np.zeros([N,1])
imp[1] = 1  # Change the first sample = 1

d1 = int(0.5 * Fs)  # 1/2 second delay
b1 = 0.7  # Gain of first delay line

d2 = int(1.5 * Fs)  # 3/2 second delay
b2 = 0.5  # Gain of second delay line

# Zero-pad the beginning of the signal for indexing based on the maximum
# delay time
pad = np.zeros([d2, 1])
impPad = np.concatenate((pad, imp))

out = np.zeros([N, 1])

# Index each element of our signal to create the output
for n in range(N):
    index = n + d2
    out[n] = impPad[index] + b1 * impPad[index - d1] + b2 * impPad[index - d2]

t = np.arange(0, N) / Fs
plt.subplot(1, 2, 1)
plt.stem(t, imp)  # Plot the impulse response
plt.axis([-0.1, 2, -0.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Input Impulse')
plt.show()

plt.subplot(1, 2, 2)
plt.stem(t, out)  # Plot the impulse response
plt.axis([-0.1, 2, -0.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Output Impulse Response')
plt.show()

soundfile.write('impResp.wav', out, Fs)

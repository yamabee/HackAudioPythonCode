# ALLPASSFILTER
# This script demonstrates an implementation of an all-pass filter using a
# delay buffer (Direct Form II).

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = np.append(1, np.zeros(100))

buffer = np.zeros(5)  # Longer buffer than delay length

# Number of samples of delay
delay = 2  # Does not need to be the same length as buffer

g = 0.5

N = len(x)
out = np.zeros(N)

for n in range(N):
    # Series all-pass filters
    out[n] = g * x[n] + buffer[delay]
    buffer = np.append(x[n] + -g * out[n], buffer[0:-1])

[W, H] = signal.freqz(out)

Hamp = abs(H)
Hphase = np.angle(H)

plt.subplot(2,1,1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.axis([0,1,-20, 20])
plt.title('Amplitude Response - HPF')
plt.subplot(2,1,2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')
plt.show()

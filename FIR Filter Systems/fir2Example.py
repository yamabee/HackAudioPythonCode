# FIR2EXAMPLE
# This script demonstrates the syntax of the 'signal.firwin2' function to
# create a filter with arbitrary frequency response.
#
# See also FIR2

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

n = 31 # filter order
freqs = [0, 0.2, 0.5, 0.8, 1] # normalized frequencies
amps = [2, 4, 0.25, 2, 1] # linear amplitudes for each freq

# Syntax for function
h = signal.firwin2(n, freqs, amps)

# Plot frequency response
W, H = signal.freqz(h)
Hamp = abs(H)
Hphase = np.angle(H)

plt.subplot(2,1,1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.title('Amplitude Response')
plt.subplot(2,1,2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')
plt.show()
# BANDSTOPFILTER
# This script creates a band-stop filter by performing parallel processing
# with an LPF and HPF.
#
# See also FIR1

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Design filters
# Note: W_lpf must be less than W_hpf to create a band-stop filter
order = 24
if not order % 2: order += 1

W_lpf = 0.25  # Normalized freq of LPF
lpf = signal.firwin(order, W_lpf, window='hamming', pass_zero='lowpass')

W_hpf = 0.75  # Normalized freq of HPF
hpf = signal.firwin(order, W_hpf, window='hamming', pass_zero='highpass')

# Impulse input signal
input = [1, 0]

# Separately, find impulse response of LPF and HPF
u = np.convolve(input, lpf)
w = np.convolve(input, hpf)

# Create combined parallel output by adding together IRs
output = u + w

# Plot the frequency response
W, H = signal.freqz(output)
Hamp = abs(H)
Hphase = np.angle(H)

plt.subplot(2, 1, 1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.title('Amplitude Response')
plt.subplot(2, 1, 2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')
plt.show()

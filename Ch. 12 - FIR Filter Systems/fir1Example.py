# FIR1EXAMPLE
# This script demonstrates the various uses of the 'signal.firwin' filter function
#
# See also FIR1

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Declare initial parameters for filters
Fs = 48000
nyq = Fs/2

n = 12 # order of filter = number of delay lines + 1
if not n % 2: n += 1 # make sure it's an odd number

f1 = 6000.0 # cutoff frequency (Hz)
Wn = f1/nyq

# Syntax for low-pass filter
h_lpf = signal.firwin(n, Wn, window='hamming', pass_zero='lowpass')

# Syntax for high-pass filter
h_hpf = signal.firwin(n, Wn, window='hamming', pass_zero='highpass')

# Declare second frequency for BPF and BSF
f2 = 18000
Wn2 = f2/nyq

# Syntax for band-pass filter
h_bpf = signal.firwin(n,[Wn, Wn2], window='hamming', pass_zero='bandpass')

# Syntax for band-stop filter
h_bsf = signal.firwin(n,[Wn, Wn2], window='hamming', pass_zero='bandstop')

# Plots
# Low-pass filter
W, H = signal.freqz(h_lpf)
Hamp = abs(H)
Hphase = np.angle(H)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.title('Amplitude Response - LPF')
plt.subplot(2,1,2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')

# High-pass filter
W, H = signal.freqz(h_hpf)
Hamp = abs(H)
Hphase = np.angle(H)

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.title('Amplitude Response - HPF')
plt.subplot(2,1,2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')

# Band-pass filter
W, H = signal.freqz(h_bpf)
Hamp = abs(H)
Hphase = np.angle(H)

plt.figure(3)
plt.subplot(2,1,1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.title('Amplitude Response - BPF')
plt.subplot(2,1,2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')

# Band-stop filter
W, H = signal.freqz(h_bsf)
Hamp = abs(H)
Hphase = np.angle(H)

plt.figure(4)
plt.subplot(2,1,1)
plt.plot(W/np.pi, 20*np.log10(Hamp))
plt.title('Amplitude Response - BSF')
plt.subplot(2,1,2)
plt.plot(W/np.pi, Hphase*(180/np.pi))
plt.title('Phase Response')
plt.show()
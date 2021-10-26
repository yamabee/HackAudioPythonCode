# BASICFILTERBANK
# This script creates a two-band filter bank using a LPF and HPF. The
# Butterworth filter design function is used to create the LPF and HPF, both
# with the same cutoff frequency. The magnitude response of each filter is
# plotted together.
#
# See also BUTTER, FREQZ

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 48000
Nyq = Fs/2

n = 8
Wn = 1000/Nyq

[bLow, aLow] = signal.butter(n, Wn, output='ba')
[bHi, aHi] = signal.butter(n, Wn, 'highpass', output='ba')

[W, hLow] = signal.freqz(b=bLow, a=aLow, worN=4096, fs=Fs)
[_,hHi] = signal.freqz(b=bHi, a=aHi, worN=4096, fs=Fs)

plt.semilogx(W, 20*np.log10(abs(hLow)), W, 20*np.log10(abs(hHi)))
plt.axis([20, 20000, -24, 6])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.legend(['LPF', 'HPF'])
plt.show()
# CONVOLUTIONFILTERING
# This script demonstrates how to use a built-in FIR filter design function
# to create the impulse response for an LPF. Then, the filtering is performed
# on an audio signal using the convolution operation.

import numpy as np
import soundfile
from scipy import signal
from IPython.display import Audio

# Import audio file
[x, Fs] = soundfile.read('AcGtr.wav')
Nyq = Fs/2

n = 30 # Order of the filter

freqHz = 500 # frequency in Hz
Wn = freqHz/Nyq # Normalized frequency for firwin

h = signal.firwin(n, Wn, window='hamming', pass_zero='lowpass') # filter design function
# 'h' is the impulse response of the filter

# Convolution applies the filter to a signal
y = np.convolve(x, h)

Audio(y, rate=Fs)
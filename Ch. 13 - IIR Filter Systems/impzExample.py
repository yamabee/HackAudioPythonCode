# IMPZEXAMPLE
# This script demonstrates how to use the 'impz' function to
# approximate an IIR system as an FIR system. Then filtering is
# performed on an audio signal using the convolution operation.
#
# See also IMPZ, CONV, BUTTER

import numpy as np
import soundfile
from scipy import signal
from IPython.display import Audio
from impz import impz

# Import audio file
[x, Fs] = soundfile.read('AcGtr.wav')
Nyq = Fs/2

m = 4 # order of the filter

freqHz = 2000 # frequency in Hz
Wn = freqHz/Nyq

[b,a] = signal.butter(m, Wn)
h = impz(b,a) # approximate system

y = np.convolve(x, h)
Audio(y, rate=Fs)
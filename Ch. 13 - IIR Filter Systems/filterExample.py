# FILTEREXAMPLE
# This script demonstrates how to use built-in IIR filter design
# function to create the impulse response for an LPF. Then, the
# filtering is performed on an audio signal using the
# 'signal.lfilter' function.

import soundfile
from scipy import signal
from IPython.display import Audio

[x, Fs] = soundfile.read('AcGtr.wav')
Nyq = Fs/2

m = 4  # Order of the filter

freqHz = 500  # frequency in Hz
Wn = freqHz/Nyq

[b, a] = signal.butter(m, Wn)
y = signal.lfilter(b, a, x)

Audio(y, rate=Fs)

# APFEXAMPLE
# This script uses an all-pass filter function applied to an acoustic
# guitar recording.
#
# See also APF

import numpy as np
import soundfile
from apf import apf
from IPython.display import Audio

x, Fs = soundfile.read('AcGtr.wav')

maxDelay = int(np.ceil(0.05 * Fs)) # maximum delay of 50ms
buffer = np.zeros(maxDelay)

d = np.ceil(0.042 * Fs) # 42ms of delay
g = 0.9

rate = 0.9 # Hz (frequency of LFO)
amp = 6 # Range of +/- 6 samples for delay

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):
    # Use apf function
    out[n], buffer = apf(x[n], buffer, Fs, n, d, g, amp, rate)

Audio(out, rate=Fs)
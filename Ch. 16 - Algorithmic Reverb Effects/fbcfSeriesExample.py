# FBCFSERIESEXAMPLE
# This script uses series feedback comb filter (FBCF) functions, applied to
# an acoustic guitar recording.
#
# See also FBCFPARALLELEXAMPLE

import soundfile
import numpy as np
from fbcf import fbcf
from IPython.display import Audio

x, Fs = soundfile.read('AcGtr.wav')

maxDelay = int(np.ceil(0.07 * Fs))  # max delay of 70ms
buffer1 = np.zeros(maxDelay)
buffer2 = np.zeros(maxDelay)

d1 = np.fix(0.042 * Fs) # 42ms of delay
g1 = 0.5
d2 = np.fix(0.053 * Fs) # 53ms of delay
g2 = -0.5

rate1 = 0.6 # Hz (frequency of LFO)
amp1 = 6 # Range of +/- 6 samples for delay
rate2 = 0.5 # Hz (frequency of LFO)
amp2 = 8 # Range of +/- 8 samples for delay

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):

    # Two series FBCFs
    w, buffer1 = fbcf(x[n], buffer1, Fs, n, d1, g1, amp1, rate1)

    # The output 'w' of the first FBCF is used as the input
    # of the second FBCF
    out[n], buffer2 = fbcf(w, buffer2, Fs, n, d2, g2, amp2, rate2)

Audio(out, rate=Fs)
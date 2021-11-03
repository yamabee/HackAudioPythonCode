# SCHROEDERREVERB
# This script implements the Schroeder reverb algorithm by using feedback
# comb filters (fbcf) and all-pass filters (apf).
#
# See also FBCF, APF

import soundfile
import numpy as np
from fbcf import fbcf
from apf import apf
from IPython.display import Audio

x, Fs = soundfile.read('AcGtr.wav')

# Max delay of 70ms
maxDelay = int(np.ceil(0.07 * Fs))
# Initialize all buffers (there are 6 total = 4 FBCFs, 2 APFs)
buffer1 = np.zeros(maxDelay)
buffer2 = np.zeros(maxDelay)
buffer3 = np.zeros(maxDelay)
buffer4 = np.zeros(maxDelay)
buffer5 = np.zeros(maxDelay)
buffer6 = np.zeros(maxDelay)

# Delay and gain parameters
d1 = np.fix(0.0297 * Fs)
g1 = 0.75
d2 = np.fix(0.0371 * Fs)
g2 = -0.75
d3 = np.fix(0.0411 * Fs)
g3 = 0.75
d4 = np.fix(0.0437 * Fs)
g4 = -0.75
d5 = np.fix(0.005 * Fs)
g5 = 0.7
d6 = np.fix(0.0017 * Fs)
g6 = 0.7

# LFO parameters
rate1 = 0.6
amp1 = 8
rate2 = 0.71
amp2 = 8
rate3 = 0.83
amp3 = 8
rate4 = 0.95
amp4 = 8
rate5 = 1.07
amp5 = 8
rate6 = 1.19
amp6 = 8

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):
    # Four parallel FBCFs
    w1, buffer1 = fbcf(x[n], buffer1, Fs, n, d1, g1, amp1, rate1)
    w2, buffer2 = fbcf(x[n], buffer2, Fs, n, d2, g2, amp2, rate2)
    w3, buffer3 = fbcf(x[n], buffer3, Fs, n, d3, g3, amp3, rate3)
    w4, buffer4 = fbcf(x[n], buffer4, Fs, n, d4, g4, amp4, rate4)

    # Combine parallel paths
    combPar = 0.25 * (w1 + w2 + w3 + w4)

    # Two series all-pass filters
    w5, buffer5 = apf(combPar, buffer5, Fs, n, d5, g5, amp5, rate5)
    out[n], buffer6 = apf(w5, buffer6, Fs, n, d6, g6, amp6, rate6)

Audio(out, rate=Fs)
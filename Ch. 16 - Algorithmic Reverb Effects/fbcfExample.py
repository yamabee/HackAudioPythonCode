# FBCFEXAMPLE
# This script uses a feedback comb filter (FBCF) function applied
# to an acoustic guitar recording.
#
# See also FBCFNOMOD, FBCF

import soundfile
import numpy as np
from fbcf import fbcf
from IPython.display import Audio

x, Fs = soundfile.read('AcGtr.wav')

maxDelay = int(np.ceil(0.05 * Fs))  # maximum delay of 50ms
buffer = np.zeros(maxDelay)  # initialize delay buffer

d = 0.04 * Fs  # 40ms of delay
g = -0.7  # feedback gain value

rate = 0.6  # Hz (frequency of LFO)
amp = 6  # Range of +/- 6 samples for delay

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):

    # Uncomment to use fbcfNoMod function
    # out[n], buffer = fbcfNoMod(x[n], buffer, n, d, g)

    # Use fbcf function
    out[n], buffer = fbcf(x[n], buffer, Fs, n, d, g, amp, rate)

Audio(out, rate=Fs)

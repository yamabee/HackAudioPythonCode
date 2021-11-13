# CHORUSEXAMPLE
# This script creates a chorus effect, applied to an acoustic guitar
# recording. Parameters for the effect include 'rate' and 'depth,' which can
# be used to control the intensity of the vibrato. At the end of the script,
# the sound of the result is played.
#
# See also CHORUSEFFECT

import numpy as np
import soundfile as sf
from IPython.display import Audio
from chorusEffect import chorusEffect

x, Fs = sf.read('../Audio Files/AcGtr.wav')
Ts = 1/Fs

maxDelay = int(np.ceil(0.05*Fs))  # Maximum delay of 50 ms
buffer = np.zeros(maxDelay)

rate = 0.6  # Hz (frequency of LFO)
depth = 5  # Milliseconds (amplitude of LFO)
predelay = 30  # Milliseconds (offset of LFO)

wet = 50  # Percent wet (dry = 100 - wet)

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):
    # Use chorusEffect function
    out[n], buffer = chorusEffect(x[n], buffer, Fs, n, depth, rate, predelay, wet)

Audio(out, rate=Fs)

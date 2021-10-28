# VIBRATOEXAMPLE
# This script creates a vibrato effect, applied to an acoustic guitar
# recording. Parameters for the effect include 'rate' and 'depth,' which can
# be used to control the intensity of the vibrato. At the end of the script,
# the sound of the result is played.
#
# See also VIBRATOEFFECT

import numpy as np
import soundfile as sf
from IPython.display import Audio
from vibratoEffect import vibratoEffect

x, Fs = sf.read('../Audio Files/AcGtr.wav') # Input signal
Ts = 1/Fs
N = len(x)

# Initialize the delay buffer
maxDelay = 1000 # Samples
buffer = np.zeros([maxDelay])

# LFO parameters
t = np.arange(0, N) * Ts
rate = 4 # Frequency of LFO in Hz
depth = 75 # Range of samples of delay

# Initialize output signal
out = np.zeros([N])

for n in range(N):
    out[n], buffer = vibratoEffect(x[n], buffer, Fs, n, depth, rate)
    if n == 70:
        out[n], buffer = vibratoEffect(x[n], buffer, Fs, n, depth, rate)

Audio(out, rate=Fs)
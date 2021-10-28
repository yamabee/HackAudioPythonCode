
import matplotlib.pyplot as plt
import numpy as np
import soundfile
import audiofile
import pandas as pd
from scipy import signal
from scipy.io import wavfile
import IPython.display as ipd
from pydub import AudioSegment
from scipy.fftpack import fft, fftfreq, ifft


def apf(x, buffer, Fs, n, delay, gain, amp, rate):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = amp * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(n % M) # Current index
    indexD = int((n-delay+intDelay) % M) # Delay index
    indexF = int((n-delay+intDelay+1) % M) # Fractional index

    # Temp variable for output of delay buffer
    w = (1 - frac) * buffer[indexD] + frac * buffer[indexF]

    # Temp variable used for the node after the input sum
    v = x + (-gain * w)

    # Summation at output
    out = (gain * v) + w

    # Store the current input to delay buffer
    buffer[indexC] = v

    return out, buffer

#%%

# APFEXAMPLE
# This script uses an all-pass filter function applied to an acoustic
# guitar recording.
#
# See also APF

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

import matplotlib.pyplot as plt
import numpy as np
import soundfile
import wave
import audiofile
import pandas as pd
from scipy import signal
from scipy.io import wavfile
from IPython.display import Audio
from pydub import AudioSegment
from scipy.fftpack import fft, fftfreq, ifft
from biquadFilter import biquadFilter

# BIQUADSTEP
# This script demonstrates the result of taking the step response of a bi-quad LPF.
# Examples include changing the cutoff frequency and Q.
#
# See also BIQUADFILTER

# Input signal
Fs = 48000
Ts = 1/Fs
x = np.ones(2 * Fs)
N = len(x)
t = np.arange(0, N) * Ts

# Changing the cutoff frequency
Q = 1.414
dBGain = Q
plt.figure(1)
for freq in range(4):
    y = biquadFilter(x, Fs, freq, Q, dBGain, 'lpf', 1)
    plt.plot(t, y)
plt.legend(['f = 1', 'f = 2', 'f = 3', 'f = 4'])
plt.xlabel('Time (sec.)')

# Changing the bandwidth Q
freq = 1
dbGain = 0
plt.figure(2)
Q = np.arange(1, 5)*(0.707/2)
for q in range(4):
    y = biquadFilter(x, Fs, freq, Q[q], dbGain, 'lpf', 1)
    plt.plot(t, y)
plt.legend('Q = 0.3535', 'Q = 0.707', 'Q = 1.0605', 'Q = 1.414')
plt.xlabel('Time (sec.)')

# ECHOSYNC
# This script demonstrates one example to create a feedforward,
# tempo-synchronized echo effect.
#
# See also CONVERTTEMPOSAMPLES

import soundfile
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio

# Import our audio file
[x, Fs] = soundfile.read('sw20.wav')
Ts = 1/Fs

# Known tempo of recording
beatsPerMin = 102 # units of beats/minute

# Calculate beats fore second
beatsPerSec = beatsPerMin / 60 # 1 minute/60 seconds

# Calculate # of seconds per beat
secPerBeat = 1/beatsPerSec

# Note division
# 4 = whole, 2 = half, 1 = quarter, 0.5 = 8th, 0.25 = 16th
noteDiv = 0.5
# Calculate delay time in seconds
timeSec = noteDiv * secPerBeat

# Convert to units of samples
d = int(np.fix(timeSec * Fs)) # round to nearest integer sample

b = 0.75 # amplitude of delay branch

# Total number of samples
N = len(x)
y = np.zeros([N, 1])

# Index each element of our signal to create the output
for n in range(N):
    # When the sample number is less than the time delay
    # Avoid indexing a negative number
    if n < d + 1:
        # output = input
        y[n] = x[n]

    # Now add in the delayed signal
    else:
        # output = input + delayed version of input
        # reduce relative amplitude of delay to 3/4
        echo = n - d
        y[n] = x[n] + b * x[echo]

t = np.arange(0, N) * Ts

plt.plot(t, x, t, y)
plt.axis([0, 1, -1.1, 1.1])
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.show()

Audio(y, rate=Fs)

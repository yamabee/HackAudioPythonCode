# ECHOFEEDBACK
# This script demonstrates one example to create a feedback, tempo-synchronized
# echo effect.
#
# See also ECHOSYNC

import soundfile
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio

# Import audio file
[x, Fs] = soundfile.read('sw20.wav')
Ts = 1/Fs

# Known tempo of recording
beatsPerMin = 102 # units of beats per minute

# Calculate beats per second
beatsPerSec = beatsPerMin / 60 # 1 minute / 60 seconds

# Calculate # of seconds per beat
secPerBeat = 1/beatsPerSec

# Note division
# 4 = whole, 2 = half, 1 = quarter, 0.5 = 8th, 0.25 = 16th
noteDiv = 0.5
timeSec = noteDiv * secPerBeat

# Convert to units of samples
d = int(np.fix(timeSec * Fs)) # round to nearest integer sample

a = -0.75 # amplitude of delay branch

# Index each element of our signal to create the output
N = len(x)
y = np.zeros([N, 1])

for n in range(N):
    # When the sample number is less than the time delay
    # Avoid indexing negative sample number
    if n < d + 1:
        # output = input
        y[n] = x[n]

    # Now add in the delayed signal
    else:
        # output = input + delayed version of output
        # reduce relative amplitude of delay to 3/4
        y[n] = x[n] + (-a) * y[n-d]

t = np.arange(0, N) * Ts

plt.plot(t, x, t, y)
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.show()

Audio(y, rate=Fs)

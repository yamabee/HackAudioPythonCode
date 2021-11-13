# IMPORTSOUNDFILE
# This script demonstrates converting a time in units of samples
# to time in units of seconds. First, it is accomplished
# sample-by-sample inside a loop. Second, it is accomplished all
# at once using array multiplication

import soundfile
import numpy as np

# Import Sound File
filename = 'sw20.wav'
[x, Fs] = soundfile.read(filename)
Ts = 1/Fs
N = len(x)

# Method 1 - inside a loop
for n in range(N):
    # convert sample number 'n' to units of seconds 't'
    t = n * Ts  # sec = sample * (sec/sample)
    # Note: Python indexing starts at n = 0
    # Time in seconds starts at t = 0

# Method 2 - array multiplication
# In this case, an array of sample numbers is created
# np.arange(0,N). Then it is multiplied by the sampling period
# to create a time vector with units of seconds
t = np.arange(0, N) * Ts  # sec = sample * (sec/sample)

print(t)

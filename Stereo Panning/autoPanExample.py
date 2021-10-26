# AUTOPANEXAMPLE
# This script implements the automatic panning (auto-pan) effect. The function
# 'pan' is used to process an input signal, along with an array of pan values
# for each sample number in the signal.
#
# See also PAN

import numpy as np
import matplotlib.pyplot as plt
import soundfile
from pan import pan
from IPython.display import Audio

# Import test sound file
[x, Fs] = soundfile.read('AcGtr.wav')
N = len(x)
Ts = 1/Fs
t = np.arange(0, N) * Ts
f = 1

panValue = 100 * np.sin(2 * np.pi * f * t)
panType = 2

out = pan(x, panValue, panType)
plt.plot(t, out[:][0], t, out[:][1])
plt.show()

Audio(out, rate=Fs)
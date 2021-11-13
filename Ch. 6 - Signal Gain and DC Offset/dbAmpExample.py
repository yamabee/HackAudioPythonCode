# DBAMPEXAMPLE
# This script provides an example for changing the amplitude
# of a signal on a decibel (dB) scale.
#
# See also DBAMPCHANGE

import matplotlib.pyplot as plt
import numpy as np
import soundfile
import dbAmpChange as dbac

# Example - Sine wave test signal
[x, Fs] = soundfile.read('sw20.wav')
x2 = dbac.dbAmpChange(x, 6)
x3 = dbac.dbAmpChange(x, -6)

Ts = 1/Fs
N = len(x)  # Total number of samples in signal
t = np.arange(0, N) * Ts

# Plot the result
plt.plot(t, x, t, x2, t, x3)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Change Amp of Signal on a dB Scale')
plt.legend(['x', 'x2', 'x3'])
plt.show()

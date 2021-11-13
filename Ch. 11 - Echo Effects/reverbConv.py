# REVERBCONV
# This script demonstrates the process to create a stereo convolution reverb
# by using a two-channel impulse response. This impulse response is based
# on a measurement of a recording studio in Nashville, TN.

import soundfile
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio

# Import sound file and IR measurement
x, Fs = soundfile.read('AcGtr.wav')  # Mono signal
h, _ = soundfile.read('reverbIR.wav')  # Stereo IR

# Visualize one channel of the impulse response
plt.plot(h[:, 0])
plt.plot(h[:, 1])
plt.show()

# Perform convolution
yLeft = np.convolve(x, h[:, 0])
yRight = np.convolve(x, h[:, 1])

y = [yLeft, yRight]

Audio(y, rate=Fs)

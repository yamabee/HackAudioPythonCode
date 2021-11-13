# STEREOIMAGER
# This script demonstrates the stereo image widening effect. The effect
# is based on mid/side processing. The parameter 'width' can be used to
# make the example drum file sound wider or narrower.
#
# See also MIDSIDEPROCESSING

import numpy as np
import matplotlib.pyplot as plt
import soundfile
from IPython.display import Audio

[x, Fs] = soundfile.read('distDrums.wav')
N = len(x)
Ts = 1/Fs
t = np.arange(0, N) * Ts

# Splitting signal into right and left channels
L = x[:, 0]
R = x[:, 1]

# Create mid and side channels
side = 0.5 * (L - R)
mid = 0.5 * (L + R)

# Width amount (wider if > 1, narrower if < 1)
width = 1.5

# Scale the mid/side with width
sideNew = width * side
midNew = (2 - width) * mid

# Create new M/S signal
newLeft = midNew + sideNew
newRight = midNew - sideNew

# Combine signals, concatenated side-by-side, 2 columns
out = [newLeft, newRight]

plt.plot(t, out[:][0], t, out[:][1])
plt.show()

Audio(out, rate=Fs)

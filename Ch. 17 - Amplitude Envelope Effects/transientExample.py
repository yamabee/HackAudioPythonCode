# TRANSIENTEXAMPLE
# This script demonstrates the transient designer function.
#
# See also TRANSIENTDESIGNER, TRANSIENTANALYSIS

import soundfile
import matplotlib.pyplot as plt
from IPython.display import Audio
from transientDesigner import transientDesigner

x, Fs = soundfile.read('AcGtr.wav')

# Attack and sustain parameters [-1, +1]
attack = 0
sustain = 1

out = transientDesigner(x, attack, sustain)

plt.plot(out, 'r')
plt.plot(x, 'b')
plt.legend(['Output', 'Input'])
plt.show()

Audio(out, rate=Fs)

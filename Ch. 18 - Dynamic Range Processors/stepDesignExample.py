# STEPDESIGNEXAMPLE
# This script demonstrates the stepDesign function for designing a second-order system
# with specified characteristics. The system is designed based on the percent overshoot,
# settling time, and peak time.
#
# See also STEPDESIGN

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from stepDesign import stepDesign

Fs = 48000

# Example - filter design based on settling time
OS = 20  # Percent overshoot
# Settling time in seconds
ts = 0.25  # (within 2% of steady-state)

b, a = stepDesign(Fs, OS, ts, 'st')
n = 1 * Fs  # number of seconds for step response
inst = signal.dlti(b, a, dt=1/Fs)
t, h = signal.dstep(inst, n=n)
plt.plot(t, np.squeeze(h))

plt.figure()

# Example - filter designed based on peak time
OS = 10  # Percent overshoot
tp = 0.75  # Peak time in seconds
b, a = stepDesign(Fs, OS, tp, 'pk')
n = 2 * Fs  # number of seconds for step response
inst = signal.dlti(b, a, dt=1/Fs)
t, h = signal.dstep(inst, n=n)
plt.plot(t, np.squeeze(h))
plt.show()

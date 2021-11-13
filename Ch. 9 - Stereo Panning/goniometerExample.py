# GONIOMETEREXAMPLE
#
# This script demonstrates several example plots of the goniometer.
#
# Examples include a signal panned to the center, left, and right. Finally,
# an example is shown when the left and right channels have opposite polarity.
#
# See also GONIOMETER

import numpy as np
import matplotlib.pyplot as plt
from goniometer import goniometer

# Test signal
Fs = 48000
Ts = 1/Fs
f = 10
t = np.arange(0, 1*Fs) * Ts
x = np.sin(2 * np.pi * f * t)

# Center
panCenter = [0.707 * x, 0.707 * x]
# must convert tuple to list
panCenter = list(panCenter)
plt.subplot(2, 2, 1)
goniometer(panCenter)

# Left
panLeft = [x, np.zeros(np.size(x))]
panLeft = list(panLeft)
plt.subplot(2, 2, 2)
goniometer(panLeft)

# Right
panRight = [np.zeros(np.size(x)), x]
panRight = list(panRight)
plt.subplot(2, 2, 3)
goniometer(panRight)

# Opposite polarities
polarity = [0.707 * x, 0.707 * (-x)]
polarity = list(polarity)
plt.subplot(2, 2, 4)
goniometer(polarity)

# LINEARINTERPOLATIONDELAY
# This script demonstrates how to introduce a fractional (non-integer) delay.
# Linear interpolation is used to estimate an amplitude value in between
# adjacent samples.

import numpy as np

x = np.append(1, np.zeros(9))  # Horizontal for displaying in command window

fracDelay = 3.2  # Fractional delay length in samples
intDelay = int(np.floor(fracDelay))  # Round down to get the previous (3)
frac = fracDelay - intDelay  # Find the fractional amount (0.2)

buffer = np.zeros(5)  # len(buffer) >= ceil(fracDelay)
N = len(x)

out = np.zeros(N)

# Series Fractional Delay
for n in range(N):
    out[n] = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    buffer = np.append(x[n], buffer[0:-1])
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x[n]

# Compare the input and output signals
np.disp(['The orig. input signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])

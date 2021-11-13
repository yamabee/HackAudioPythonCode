# CUBICINTERPOLATIONDELAY
# This script demonstrates how to introduce a fractional (non-linear) delay.
# Cubic interpolation is used to estimate an amplitude value in-between
# adjacent samples.

import numpy as np
import matplotlib.pyplot as plt

x = np.append(1, np.zeros(9))

fracDelay = 3.2  # Fractional delay length in samples
intDelay = int(np.floor(fracDelay))  # Round down to get the previous (3)
frac = fracDelay - intDelay  # Find the fractional amount (0.2)

buffer = np.zeros(5)  # len(buffer) >= ceil(fracDelay) + 1
N = len(x)

out = np.zeros(N)
# Series fractional delay
for n in range(N):
    # Calculate intermediate variable for cubic interpolation
    a0 = buffer[intDelay+1] - buffer[intDelay] - buffer[intDelay-2] + buffer[intDelay-1]
    a1 = buffer[intDelay-2] - buffer[intDelay-1] - a0
    a2 = buffer[intDelay] - buffer[intDelay-2]
    a3 = buffer[intDelay-1]
    out[n] = a0 * pow(frac, 3) + a1 * pow(frac, 2) + a2 * frac + a3

    buffer = np.append(x[n], buffer[0:-1])  # Shift buffer
    # buffer[1:] = buffer[0:-1]
    # buffer[0] = x[n]

# Compare input and output signals
np.disp(['The orig. input signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])

plt.plot(out)
# Observe in this plot that the impulse at sample n=1 is delayed by 3.2
# samples. Therefore, the output signal should have an impulse at time 4.2
# samples. With cubic interpolation this impulse contributes to the amplitude
# of the output signal at samples 3, 4, 5, 6. The result of cubic
# interpolation is a closer approximation to the underlying (smooth)
# continuous signal than linear interpolation.

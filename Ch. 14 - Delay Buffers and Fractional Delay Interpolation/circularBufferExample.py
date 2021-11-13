# CIRCULARBUFFEREXAMPLE
# This script tests a circular buffer function and demonstrates how it works.
#
# See also CIRCULARBUFFER

import numpy as np
from circularBuffer import circularBuffer

x = np.append(np.array([1, -1, 2, -2, 3]), np.zeros(5))

buffer = np.zeros(6)

# Number of samples of delay
delay = 4

N = len(x)
out = np.zeros(N)

# Series delay
for n in range(N):
    out[n], buffer = circularBuffer(x[n], buffer, delay, n)

    # Display current status values
    np.disp(['The current sample number is: ', str(n)])
    np.disp(['The current buffer index is: ', str(np.mod(n-1, 6))])
    np.disp(['The current delay index is: ', str(np.mod(n-delay-1, 6))])
    np.disp(['The input is: ', str(x[n])])
    np.disp(['The delay buffer is: [', str(buffer), ']'])
    np.disp(['The output is: ', str(out)])

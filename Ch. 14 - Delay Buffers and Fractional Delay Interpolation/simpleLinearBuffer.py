# SIMPLELINEARBUFFER
# This script demonstrates the basics of creating a linear buffer.
# An input signal is processed by a loop to index the 'current' sample
# and store it in the delay buffer. Each time through the loop the delay
# buffer is shifted to make room for a new sample. The output of the
# process is determined by indexing an element at the end of the delay
# buffer.
#
# Execution of the script is set to 'pause' during the iteration to allow
# a user to view the contents of the delay buffer during each step.
#
# See also DELAYBUFFEREXAMPLE

import numpy as np

x = np.append(np.array([1, -1, 2, -2]), np.zeros([6]))
# Buffer should be initialized without any value
# Length of buffer = 5, output is indexed from end of buffer.
# Therefore, a delay of 5 samples is created
buffer = np.zeros([5])

N = np.size(x)
out = np.zeros([N])

for n in range(N):
    # Read the output at the curretn time sample
    # from the end of the delay buffer
    out[n] = buffer[-1]
    np.disp(['For sample ', str(n), ' the output is: ', str(out[n])])

    # Shift each value in the buffer by one element
    # to make room for the current sample to be stored
    # in the first element
    buffer = np.append(x[n], buffer[0:-1])
    # buffer[0, 1:] = buffer[0, 0:-1]
    # buffer[0, 0] = x[0, n]
    np.disp(['For sample ', str(n), ' the buffer is: ', str(buffer)])

# Compare the input and output signals
np.disp(['The original signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])
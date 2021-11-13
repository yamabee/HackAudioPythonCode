# FEEDBACKDELAYEXAMPLE
# This script calls the feedback delay function and passes in the delay buffer.
#
# See also FEEDBACKDELAY

import numpy as np
from feedbackDelay import feedbackDelay

x = np.append(np.array([1, -1, 2, -2]), np.zeros([6]))  # Input signal
x = np.vstack(x)
# Longer buffer than delay length to demonstrate delay
# doesn't just have to be the 'end' of the buffer.
buffer = np.zeros([20])

# Number of samples of delay
delay = 5

# Feedback gain coefficient
fbGain = 0.5

# Initialize output vector
N = len(x)
out = np.zeros([N])

# Series delay
for n in range(N):
    # Pass 'buffer' into feedbackDelay function
    out[n], buffer = feedbackDelay(x[n], buffer, delay, fbGain)
    # Return updated 'buffer' for next loop iteration

# Print and compare input and output signals
np.disp('Feedback Delay: 5 samples')
np.disp(['The orig. input signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])

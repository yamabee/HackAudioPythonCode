# DELAYBUFFEREXAMPLES
# This script demonstrates several examples of creating different types (FIR, IIR)
# of systems by using a delay buffer.
#
# See also SIMPLELINEARBUFFER

import numpy as np

x = np.append(np.array([1, -1, 2, -2]), np.zeros([6]))
buffer = np.zeros([20])  # longer buffer than delay length

# Number of samples of delay
delay = 5  # does not need to be same length as buffer

N = np.size(x)
out = np.zeros([N])

# Series Delay
for n in range(N):
    out[n] = buffer[delay-1]

    buffer = np.append(x[n], buffer[0:-1])
    # buffer[0, 1:] = buffer[0, 0:-1]
    # buffer[0, 0] = x[0, n]

# Compare input & output signals
np.disp('Series Delay: 5 samples')
np.disp('out(n) = x(n-5)')
np.disp(['The orig. input signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])

# Feedforward (FIR) system
out = np.zeros([N])
buffer = np.zeros([20])
delay = 3  # Number of samples of delay

# Parallel delay line
for n in range(N):
    out[n] = x[n] + buffer[delay-1]

    buffer = np.append(x[n], buffer[0:-1])
    # buffer[0, 1:] = buffer[0, 0:-1]
    # buffer[0, 0] = x[0, n]

np.disp('Feed-forward Delay: 3 samples')
np.disp('out(n) = x(n) + x(n-3)')
np.disp(['The orig. input signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])

# Feedback (IIR) system
out = np.zeros([N])
buffer = np.zeros([20])

for n in range(N):
    out[n] = x[n] + buffer[delay-1]

    buffer = np.append(out[n], buffer[0:-1])
    # buffer[0, 1:] = buffer[0, 0:-1]
    # buffer[0, 0] = out[0, n]

np.disp('Feedback Delay: 3 samples')
np.disp('out(n) = x(n) + out(n-3)')
np.disp(['The orig. input signal was: ', str(x)])
np.disp(['The final output signal is: ', str(out)])

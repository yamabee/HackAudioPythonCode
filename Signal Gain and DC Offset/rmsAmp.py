import numpy as np
import soundfile


# RMSAMP
# This script demonstrates the process of calculating the RMS
# amplitude of a signal. First, the samples in the signal are squared.
# Second, the mean (arithmetic average of the squared signal
# is found. Third, the square root of the mean of the squared
# signal is determined.

# Sine wave signal for testing
[x, Fs] = soundfile.read('sw20.wav') # have to use [x, Fs] rather than just x, problems arise
N = len(x) # total number of samples

# Square the individual samples of the signal
sigSquared = np.square(x) # Element-wise power operation; result is an array
# Find the mean. Note: result is now scalar
sigMeanSquared = (1/N) * np.sum(sigSquared)

# Take the square root
sigRootMeanSquared = np.sqrt(sigMeanSquared)
print(sigRootMeanSquared)
# RMS amplitude for a sine wave -> 0.707
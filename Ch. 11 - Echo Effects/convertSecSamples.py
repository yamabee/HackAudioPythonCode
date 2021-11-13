# CONVERTSECSAMPLES
# This script provides two examples for converting a time delay in units of
# seconds to samples and milliseconds to samples.
#
# See also CONVERTTEMPOSAMPLES

import numpy as np

# Example 1 - Seconds to samples
Fs = 48000  # arbitrary sampling rate
timeSec = 1.5  # arbitrary time in units of seconds

# Convert to units of samples
timeSamples = np.fix(timeSec * Fs)  # round to nearest integer sample

# Example 2 - Milliseconds to samples
timeMS = 330  # arbitrary time in units of milliseconds

# Convert to units of seconds
timeSec = timeMS/1000
# Convert to units of samples
timeSamples = np.fix(timeSec * Fs)  # round to nearest integer samples


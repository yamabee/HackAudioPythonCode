# EXPANDEREXAMPLE
# This script demonstrates an expander/gate DR processor
#
# See also EXPANDER, COMPRESSOREXAMPLE

import soundfile
from IPython.display import Audio
from expander import expander

# Drums sound file
x, Fs = soundfile.read('monoDrums.wav')

# Parameters for compressor
T = -20  # Threshold = -20 dBFS
R = 3  # Ratio = 3:1

# Initialize separate attack and release times
attackTime = 0.005  # time in seconds
releaseTime = 0.4  # time in seconds

out = expander(x, Fs, T, R, attackTime, releaseTime)
Audio(out, rate=Fs)
# Audio(x, rate=Fs) # For comparison

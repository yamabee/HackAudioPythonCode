# COMPRESSOREXAMPLE
# This script creates a dynamic range compressor with separate attack and release
# times.
#
# See also COMPRESSOR, BASICCOMP

import soundfile
from IPython.display import Audio
from compressor import compressor

# Acoustic guitar 'audio' sound file
x, Fs = soundfile.read('AcGtr.wav')

# Parameters for compressor
T = -15  # Threshold = -15 dBFS
R = 10  # Ratio = 10:1

# Initialize separate attack and release times
attackTime = 0.05  # time in seconds
releaseTime = 0.25  # time in seconds

# Compressor function
out = compressor(x, Fs, T, R, attackTime, releaseTime)

Audio(out, rate=Fs)

# MIDSIDEPROCESSING
# This script performs mid/side (sum and difference) encoding
# and decoding.

import soundfile

[x, Fs] = soundfile.read('distDrums.wav')

# Separate stereo signal into two mono signals
left = x[:, 0]
right = x[:, 1]

# Mid/side encoding
mid = 0.5 * (left + right)
sides = 0.5 * (left - right)

# Add additional processing here
# (e.g.. distortion, compression, etc.)
#########################################################


#########################################################

# Mid/side decoding
newL = mid + sides
newR = mid - sides

output = [newL, newR]
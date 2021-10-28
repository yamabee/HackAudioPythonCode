# PARALLEL DISTORTION
# This script demonstrates how to create parallel distortion. It allows for the
# 'dry' unprocessed signal to be blended with the 'wet' processed signal.
#
# See also ARCTANDISTORTION

import soundfile
from arctanDistortion import arctanDistortion

[x, Fs] = soundfile.read('sw20.wav')

# Alpha - amount of distortion
alpha = 8

# Wet path - distortion
dist = arctanDistortion(x, alpha)
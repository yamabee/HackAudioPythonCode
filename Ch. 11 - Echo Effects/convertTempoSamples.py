# CONVERTTEMPOSAMPLES
# This script provides an example for calculating a delay time in units of
# samples that will be synchronized with the tempo of a song in units of
# beats per minutes (BPM).
#
# Assume a (4/4) time signature where BEAT = QUARTER NOTE
#
# See also CONVERTSECSAMPLES

import numpy as np

Fs = 48000

beatsPerMin = 90
beatsPerSec = beatsPerMin/60
secPerBeat = 1/beatsPerSec

noteDiv = 1
timeSec = noteDiv * secPerBeat
timeSamples = np.fix(timeSec * Fs)

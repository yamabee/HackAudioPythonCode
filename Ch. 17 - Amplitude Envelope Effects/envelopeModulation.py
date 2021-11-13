# ENVELOPEMODULATION
# This script demonstrates the process of measuring an amplitude envelope from
# the waveform of a voice recording and using it io modulate the amplitude of
# synth recording.

import soundfile
import numpy as np
from IPython.display import Audio

# Import audio files
x, Fs = soundfile.read('Voice.wav')
synth, _ = soundfile.read('Synth.wav')

alpha = 0.9997 # feedback gain
fb = 0 # initialized value for feedback
N = len(x)
env = np.zeros(N)

for n in range (N):
    # Analyze envelope
    env[n] = (1 - alpha) * abs(x[n]) + alpha * fb
    fb = env[n]

# Make-up gain
env = 4 * env

# Amplitude modulation of envelope applied to synthsizer
out = synth * env

Audio(out, rate=Fs)
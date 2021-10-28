# PITCHSHIFTEREXAMPLE
# This script is an example to demonstrate the pitchShifter function
# for processing an audio signal. The desired number of semitones
# can be set from within this script.

import soundfile as sf
from pitchShifter import pitchShifter
from IPython.display import Audio

# Import acoustic guitar recording for processing
x, Fs = sf.read('../Audio Files/AcGtr.wav')

# Experiment with different values
semitones = 4

out = pitchShifter(x, Fs, semitones=semitones)

Audio(out, rate=Fs)
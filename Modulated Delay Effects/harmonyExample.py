# HARMONYEXAMPLE
# This script creates a harmony effect by blending together a pitch shifted
# signal with the original, unprocessed signal.
#
# See also PITCHSHIFTER, PITCHSHIFTEREXAMPLE

import soundfile as sf
from pitchShifter import pitchShifter
from IPython.display import Audio

# Import acoustic guitar recording for processing
x, Fs = sf.read('AcGtr.wav')

# Pitch shifted down a perfect fourth
semitones = -5
processed = pitchShifter(x, Fs, semitones=semitones)

# Blend together input and processed
out = 0.5 * (x + processed)

Audio(out, rate=Fs)
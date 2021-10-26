# LFOPITCH
# This script demonstrates an example of pitch shifting using a sawtooth LFO
# to modulate delay time. The result is a signal that has been pitch shifted
# based on the 'semitones' variable.
#
# An important aspect of this algorithm is to avoid having the processed
# signal to be a different length than the original signal. To make this
# possible, the maximum delay time is 50 ms. A sawtooth LFO is used to
# modulate the delay time between 0ms and 50ms based on the necessary rate
# of change. If the delay time is about to go outside of this range, a new
# cycle of the sawtooth begins.
#
# The output signal has audible clicks and pops due to the discontinuities
# of the modulated delay. This motivates the use of two parallel delay lines
# that crossfade back and forth to smooth over the discontinuities.
#
# See also BASICPITCH, PITCHSHIFTER, PITCHSHIFTEREXAMPLE

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
from IPython.display import Audio

# Synthesize 1 Hz test signal
x, Fs = sf.read('AcGtr.wav')
Ts = 1/Fs

semitones = 3
tr = pow(2, semitones/12)
dRate = 1 - tr          # Delay rate of change

maxDelay = int(Fs * 0.05)    # Maximum delay is 50ms

# Conditional to handle pitch up and pitch down
if dRate > 0:   # Pitch decrease
    d = 0

else:           # Pitch increase
    # Initialize delay so it is always positive
    d = maxDelay

N = len(x)
out = np.zeros(N)
lfo = np.zeros(N)
buffer = np.zeros(maxDelay)

for n in range(N):
    # Determine output of delay buffer
    # which could be a fractional delay time
    intDelay = int(np.floor(d)) - 1
    frac = d - intDelay

    if intDelay == 0:   # When delay time = zero
                        # 'out' comes 'in', not just delay buffer
        out[n] = (1-frac) * x[n] + frac * buffer[0]

    else:
        out[n] = (1-frac) * buffer[intDelay-1] + frac * buffer[intDelay]

    # Store the current output in appropriate index
    buffer = np.append(x[n], buffer[0:-1])

    # Store the current delay in signal for plotting
    lfo[n] = d
    d = d + dRate # Change the delay time for the next loop

    # If necessary, start a new cycle in LFO
    if d < 0:
        d = maxDelay
    elif d > maxDelay:
        d = 0

t = np.arange(0, N) * Ts

plt.subplot(3, 1, 1)
plt.plot(t, lfo) # Crossfade gains
plt.ylabel('Delay (Samples)')
plt.tight_layout()

# Spectrogram
plt.subplot(3,1,2)
nfft = 2048 # length of each time frame
window = signal.windows.hann(nfft) # calculated windowing function
overlap = 128 # number of samples for frame overlap
spec, f, tSpec, imAxis = plt.specgram(out, nfft, Fs, window=window, noverlap=overlap)
plt.axis('tight')
plt.axis('auto')
plt.xlabel('Time (sec.)')
plt.ylabel('Freq. (Hz)')
plt.show()

plt.figure()
tau = (maxDelay/dRate) * Ts
f = 1/tau
plt.plot(t, lfo, t, maxDelay * (0.5 * signal.sawtooth(2 * np.pi * f * t)+ 0.5), 'r--')
plt.tight_layout()
plt.show()

Audio(out, rate=Fs)
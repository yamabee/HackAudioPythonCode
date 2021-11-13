# TRANSIENTANALYSIS
# This script plots the amplitude envelopes used in the transient designer effect. A
# comparision is plotted of the 'fast' and 'slow' envelopes used to determine when
# 'attack' and 'sustain' is occuring in the signal.
#
# See also TRANSIENTDESIGNER, TRANSIENTEXAMPLE

import soundfile
import numpy as np
import matplotlib.pyplot as plt

x, Fs = soundfile.read('AcGtr.wav')

gFast = 0.9991  # Gain smoothing for the 'fast' envelope
fbFast = 0  # Feedback for the 'fast' envelope
gSlow = 0.9999  # Gain smoothing for the 'slow' envelope
fbSlow = 0  # Feedback for the 'slow' envelope

N = len(x)
envFast = np.zeros(N)
envSlow = np.zeros(N)
transientShaper = np.zeros(N)

for n in range(N):
    envFast[n] = (1 - gFast) * 2 * abs(x[n]) + gFast * fbFast
    fbFast = envFast[n]

    envSlow[n] = (1 - gSlow) * 3 * abs(x[n]) + gSlow * fbSlow
    fbSlow = envSlow[n]

    transientShaper[n] = envFast[n] - envSlow[n]

plt.figure(1)
plt.plot(envFast)
plt.plot(envSlow)
plt.plot(transientShaper)
plt.legend(['alpha = 0.9991', 'alpha = 0.9999', 'envFast - envSlow'])
plt.axis([1, N, -0.5, 1])
plt.show()

attack = np.zeros(N)
sustain = np.zeros(N)
for n in range(N):
    if transientShaper[n] > 0:
        attack[n] = transientShaper[n] + 1
        sustain[n] = 1

    else:
        attack[n] = 1
        sustain[n] = transientShaper[n] + 1

plt.figure(2)
plt.subplot(2, 1, 1)  # Plot the detected attack envelope
plt.plot(attack)
plt.title('Attack Envelope')
plt.axis([1, N, 0.5, 1.5])
plt.subplot(2, 1, 2)
plt.plot(sustain)
plt.title('Sustain Envelope')
plt.axis([1, N, 0.5, 1.5])
plt.show()

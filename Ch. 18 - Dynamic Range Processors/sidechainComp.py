# SIDECHAINCOMP
# This script creates a side-chain compressor with a synthesizer signal and kick drum
# signal.
#
# See also COMPRESSOR

import numpy as np
import matplotlib.pyplot as plt
import soundfile
from IPython.display import Audio

# Synthesizer input signal
x, Fs = soundfile.read('Synth.wav')
# Kick drum for the detection path
sc, _ = soundfile.read('Kick.wav')

# Parameters for compressor
T = -24  # Threshold = -24 dBFS
R = 10  # Ratio = 10:1

# Initialize separate attack and release times
attackTime = 0.05  # time in seconds
alphaA = np.exp(-np.log(9)/(Fs * attackTime))
releaseTime = 0.25  # time in seconds
alphaR = np.exp(-np.log(9)/(Fs * releaseTime))

gainSmoothPrev = 0  # Initialize smoothing variable

N = len(sc)
y = np.zeros(N)
lin_A = np.zeros(N)

# Loop over each sample to see if it is above threshold
for n in range(N):
    ##### Detection path based on the kick drum input signal
    # Turn the input signal into a unipolar signal on the dB scale
    sc_uni = abs(sc[n])
    sc_dB = 20 * np.log10(sc_uni/1)

    # Ensure there are no values of negative infinity
    if sc_dB < -96:
        sc_dB = -96

    # Static characteristics
    if sc_dB > T:
        gainSC = T + (sc_dB - T)/R  # Perform downwards compression
    else:
        gainSC = sc_dB  # Do not perform compression

    gainChange_dB = gainSC - sc_dB

    # Smooth over gainChange
    if gainChange_dB < gainSmoothPrev:
        # attack mode
        gainSmooth = -np.sqrt(((1-alphaA) * pow(gainChange_dB, 2)) + pow(alphaA * gainSmoothPrev, 2))

    else:
        # release
        gainSmooth = -np.sqrt(((1-alphaR) * pow(gainChange_dB, 2)) + pow(alphaR * gainSmoothPrev, 2))

    # Convert to linear amplitude scalar
    lin_A[n] = pow(10, (gainSmooth/20))

    # Apply linear amplitude to input sample
    y[n] = lin_A[n] * x[n]

    # Update gainSmoothPrev used in the next sample of the loop
    gainSmoothPrev = gainSmooth

t = np.arange(0, N)/Fs

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Input Signal - Synth')
plt.axis([0, t[-1], -1.1, 1.1])
plt.subplot(3, 1, 2)
plt.plot(t, sc)
plt.title('Sidechain - Kick')
plt.axis([0, t[-1], -1.1, 1.1])
plt.subplot(3, 1, 3)
plt.plot(t, y, t, lin_A)
plt.title('Output')
plt.axis([0, t[-1], -1.1, 1.1])
plt.legend(['Output Signal', 'Gain Reduction'])
plt.show()

Audio(y, rate=Fs)

# RMSCOMP2
# This script creates a compressor with approximated RMS detection. The RMS value is
# estimated by using feedback. Separate attack and release times can be achieved.
#
# See also RMSCOMP

import numpy as np
import matplotlib.pyplot as plt
import soundfile

# Acoustic guitar 'audio' sound file
x, Fs = soundfile.read('AcGtr.wav')

# Parameters for compressor
T = -12  # Threshold = -12 dBFS
R = 4  # Ratio = 4:1

# Initialize separate attack and release times
attackTime = 0.1  # time in seconds
alphaA = np.exp(-np.log(9)/(Fs * attackTime))
releaseTime = 0.1  # time in seconds
alphaR = np.exp(-np.log(9)/(Fs * releaseTime))

gainSmoothPrev = 0  # Initialize smoothing variable

N = len(x)
y = np.zeros(N)
lin_A = np.zeros(N)

# Loop over each sample to see if it is above threshold
for n in range(N):
    # Turn the input signal into a unipolar signal on the dB scale
    x_dB = 20 * np.log10(abs(x[n]))

    # Ensure there are no values of negative infinity
    if x_dB < -96:
        x_dB = -96

    # Static characteristics
    if x_dB > T:
        gainSC = T + (x_dB - T)/R  # Perform downwards compression
    else:
        gainSC = x_dB  # Do not perform compression

    gainChange_dB = gainSC - x_dB

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

plt.subplot(2, 1, 1)
plt.plot(t,x)
plt.title('Input Signal')
plt.axis([0, t[-1], -1.1, 1.1])
plt.subplot(2, 1, 2)
plt.plot(t, y, t, lin_A)
plt.title('Output')
plt.axis([0, t[-1], -1.1, 1.1])
plt.legend(['Output Signal', 'Gain Reduction'])
plt.show()

# RMSCOMP
# This script creates a compressor with conventional RMS detection. The RMS value is
# calculated over a range of 'M' samples. Note: attack and release are linked
#
# See also COMPRESSOR, RMSCOMP2

import numpy as np
import matplotlib.pyplot as plt
import soundfile

# Acoustic guitar 'audio' sound file
x, Fs = soundfile.read('AcGtr.wav')

# Parameters for compressor
T = -20  # Threshold = -20 dBFS
R = 4  # Ratio = 4:1

# Initialize separate attack and release times
attackTime = 0.1  # time in seconds
alphaA = np.exp(-np.log(9)/(Fs * attackTime))
releaseTime = 0.25  # time in seconds
alphaR = np.exp(-np.log(9)/(Fs * releaseTime))

gainSmoothPrev = 0  # Initialize smoothing variable

M = 2048 # length of RMS calculation

# Initialize the first time window in a buffer
x_win = np.append(np.zeros(int(M/2)), x[0:int(M/2)])

N = len(x)
y = np.zeros(N)
lin_A = np.zeros(N)

# Loop over each sample to see if it is above threshold
for n in range(N):
    # Calculate the RMS for the current window
    x_rms = np.sqrt(np.mean(np.square(x_win)))

    # Turn the input signal into a unipolar signal on the dB scale
    x_dB = 20 * np.log10(x_rms)

    # Ensure there are no values of negative infinity
    if x_dB < -96:
        x_dB = -96

    # Static characteristics
    if x_dB > T:
        gainSC = T + (x_dB - T)/R  # Perform compression
    else:
        gainSC = x_dB  # Do not perform compression

    gainChange_dB = gainSC - x_dB

    # Convert to linear amplitude scalar
    lin_A[n] = pow(10, (gainChange_dB/20))

    # Apply linear amplitude to input sample
    y[n] = lin_A[n] * x[n]

    # Update the current time window
    if n + int(M/2) < N:
        x_win = x_win[1:]
        x_win = np.append(x_win, x[n+(int(M/2))])

    else:
        x_win = np.append(x_win[1:], 0)


t = np.arange(0, N)/Fs

plt.subplot(2,1,1)
plt.plot(t,x)
plt.title('Input Signal')
plt.axis([0, t[-1], -1.1, 1.1])
plt.subplot(2,1,2)
plt.plot(t, y, t, lin_A)
plt.title('Output')
plt.axis([0, t[-1], -1.1, 1.1])
plt.legend(['Output Signal', 'Gain Reduction'])
plt.show()
# FEEDBACKCOMP
# This script creates a feedback compressor. The processing of the detection path is
# similar to the feedforward compressor. The main difference is the output 'y' is
# analyzed in the detection path, not the input 'x'. A plot is produced at the end
# of the script to visualize the result.
#
# See also COMPRESSOR, BASICCOMP

import numpy as np
import matplotlib.pyplot as plt
import soundfile

# Acoustic guitar 'audio' sound file
x, Fs = soundfile.read('AcGtr.wav')

# Parameters for compressor
T = -15 # Threshold = -15 dBFS
R = 10 # Ratio = 10:1

# Initialize separate attack and release times
attackTime = 0.05 # time in seconds
alphaA = np.exp(-np.log(9)/(Fs * attackTime))
releaseTime = 0.25 # time in seconds
alphaR = np.exp(-np.log(9)/(Fs * releaseTime))

N = len(x)
y = np.zeros(N)
lin_A = np.zeros(N)

gainSmoothPrev = 0 # Initialize smoothing variable

y_prev = 0 # Initialize ouptut for feedback detection

# Loop over each sample to see if it is above threshold
for n in range(N):
    ###### Detection path based on the ouput signal, not 'x'
    # Turn the input signal into a unipolar signal on the dB scale
    y_uni = abs(y_prev)
    y_dB = 20 * np.log10(y_uni/1)

    # Ensure there are no values of negative infinity
    if y_dB < -96:
        y_dB = -96

    # Static characteristics
    if y_dB > T:
        gainSC = T + (y_dB - T)/R

    else:
        gainSC = y_dB # Do not perform compression

    gainChange_dB = gainSC - y_dB

    # smooth over the gainChange
    if gainChange_dB < gainSmoothPrev:
        # attack mode
        gainSmooth = ((1-alphaA) * gainChange_dB) + (alphaA * gainSmoothPrev)

    else:
        # release mode
        gainSmooth = ((1-alphaR) * gainChange_dB) + (alphaR * gainSmoothPrev)

    # Convert to linear amplitude scalar
    lin_A[n] = pow(10, gainSmooth/20)

    # Apply linear amplitude scalar
    y[n] = lin_A[n] * x[n]
    y_prev = y[n] # Update the next cycle

    # Update gainSmoothPrev used in the next sample of the loop
    gainSmoothPrev = gainSmooth

t = np.arange(0, N)/Fs

plt.subplot(2,1,1)
plt.plot(t,x)
plt.title('Input Signal')
plt.axis([0, 7, -1.1, 1.1])
plt.subplot(2,1,2)
plt.plot(t, y, t, lin_A)
plt.title('Output')
plt.axis([0, 7, -1.1, 1.1])
plt.legend(['Output Signal', 'Gain Reduction'])
plt.show()
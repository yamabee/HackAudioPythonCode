# BASICCOMP
# This script creates a dynamic range compressor with attack and release times
# linked together. A step input signal is synthesized for testing. A plot is produced
# at the end of the script to show a comparison of the input step signal, the output
# response, and the gain reduction curve.
#
# See also COMPRESSOR, COMPRESSOREXAMPLE

import numpy as np
import matplotlib.pyplot as plt

# Step input signal
Fs = 48000
Ts = 1/Fs
x = np.append(np.zeros(Fs), np.ones(Fs))
x = np.append(x, np.zeros(Fs))

N = len(x)
# Parameters for compressor
T = -12 # Threshold = -12 dBFS
R = 3 # Ratio = 3:1
responseTime = 0.25 # time in seconds
alpha = np.exp(-np.log(9)/(Fs * responseTime))
gainSmoothPrev = 0 # Initialize smoothing variable

y = np.zeros(N)
lin_A = np.zeros(N)

# Loop over each sample to see if it is above threshold
for n in range(N):
    ###### Calculations of the detection path
    # Turn the input signal into a unipolar signal on the dB scale
    x_uni = abs(x[n])
    x_dB = 20 * np.log10(x_uni/1)
    # Ensure there are no values of negative infinity
    if x_dB < - 96:
        x_dB = -96

    # Static characteristics
    if x_dB > T:
        gainSC = T + (x_dB - T)/R # Perform downwards compression

    else:
        gainSC = x_dB # Do not perform compression

    gainChange_dB = gainSC - x_dB

    # Smooth over the gainChange_dB to alter response time
    gainSmooth = ((1-alpha) * gainChange_dB) + (alpha * gainSmoothPrev)

    # Convert to linear amplitude scalar
    lin_A[n] = pow(10, gainSmooth/20)

    ###### Apply linear amplitude from detection path
    ###### to input sample.
    y[n] = lin_A[n] * x[n]

    # Update gainSmoothPrev used in the next sample of the loop
    gainSmoothPrev = gainSmooth

t = np.arange(0, N) * Ts

plt.subplot(3,1,1)
plt.plot(t, x)
plt.title('Step Input')
plt.axis([0, 3, -0.1, 1.1])

plt.subplot(3,1,2)
plt.plot(t, y)
plt.title('Comp Out')
plt.axis([0, 3, -0.1, 1.1])

plt.subplot(3,1,3)
plt.plot(t, lin_A)
plt.title('Gain Reduction')
plt.axis([0, 3, -0.1, 1.1])
plt.show()

# The 'gain reduction' line shows the amount of compression applied at each sample
# of the signal. When the value is '1', there is no compression. When the value is
# less than '1', gain reduction is happening.
# DISTORTIONEXAMPLE
# This script is used to test various distortion functions. Each algorithm
# can be analyzed by 'uncommenting' the code under each section. The waveform
# and characteristic curve is plotted for each function.

import numpy as np
import matplotlib.pyplot as plt

from infiniteClip import infiniteClip
from halfWaveRectification import halfWaveRectification
from fullWaveRectification import fullWaveRectification
from hardClipping import hardClipping
from cubicDistortion import cubicDistortion
from arctanDistortion import arctanDistortion
from exponential import exponential
from piecewise import piecewise
from diode import diode
from asymmetrical import asymmetrical
from bitReduction import bitReduction

Fs = 48000
Ts = 1/Fs
f = 2
t = np.arange(0, Fs * 1) * Ts

x = np.sin(2 * np.pi * f * t)  # used as input signal for each distortion

# # Infinite clipping
# y = infiniteClip(x)

# # Half-wave rectification
# y = halfWaveRectification(x)

# # Full-wave Rectification
# y = fullWaveRectification(x)

# # Hard-clipping
# thresh = 0.5
# y = hardClipping(x, thresh)

# # Cubic soft-clipping
# a = 1
# y = cubicDistortion(x, alpha)

# # Arctangent distortion
# alpha = 5
# y = arctanDistortion(x, alpha)

# # Sine distortion
# y = np.sin((np.pi/2) * x)

# # Exponential soft-clipping
# drive = 4
# y = exponential(x, drive)

# # Piece-wise overdrive
# y = piecewise(x)

# # Diode clipping
# y = diode(x)

# # Asymmetrical distortion
# dc = -0.25
# y = asymmetrical(x, dc)

# # Bit crushing
# nBits = 8
# y = bitReduction(x, nBits)

# Dither Noise
dither = 0.003 * np.random.randn(np.size(x))
nBits = 4
y = bitReduction(x + dither, nBits)

# Plotting
plt.figure(1)
plt.subplot(1, 2, 1)  # Waveform
plt.plot(t, x, t, y)
plt.axis([0, 1, -1.1, 1.1])
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.title('Waveform')

plt.subplot(1, 2, 2)  # Characteristic Curve
plt.plot(x, x, x, y)
plt.axis([-1, 1, -1.1, 1.1])
plt.xlabel('Input Amplitude')
plt.ylabel('Output Amplitude')
plt.legend(['Legend', 'Distortion'])
plt.title('Characteristic Curve')
plt.show()

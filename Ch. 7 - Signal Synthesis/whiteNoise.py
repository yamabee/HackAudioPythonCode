# WHITENOISE
# This script synthesizes a white noise signal by using a
# Gaussian random number generator. Gaussian random numbers are
# also described as normally distributed random numbers. The
# function 'np.random.normal' creates random numbers based on a
# normal distribution.

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
from plottf import plottf

Fs = 44100  # Sampling rate
sec = 5  # Desired length in seconds
samples = Fs * sec  # Convert length to samples

# Next, synthesize noise. The scalar (0.2) is to reduce the
# amplitude of the signal to within the full-scale range. An
# additional option would be to perform peak normalization to
# ensure the amplitude is always between -1 and 1.
noise = 0.2 * np.random.normal(size=[samples])
plt.plot(noise)
plt.show()

plottf(noise, Fs)

Audio(noise, rate=Fs)
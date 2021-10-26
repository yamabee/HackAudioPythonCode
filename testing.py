
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import audiofile
import pandas as pd
from scipy import signal
from scipy.io import wavfile
import IPython.display as ipd
from pydub import AudioSegment
from scipy.fftpack import fft, fftfreq, ifft


def crossfades(Fs, len, Hz, fade):
    period = Fs/Hz
    win = signal.windows.hann(fade*2)

    n = 0
    g1 = np.zeros(len)
    g2 = np.zeros(len)
    while n < len:
        # Position of 'n' relative to a cycle
        t = np.mod(n, period)
        if t < period/2 - fade:  #fade/2
            g1[n] = 1
            g2[n] = 0
            c = 0
        elif t < period/2: #+ fade/2 # first fade
            g1[n] = 0
            g2[n] = 1
            c = c + 1
        elif t < period - fade:
            g1[n] = 0
            g2[n] = 1
            c = 0
        else: # 2nd fade
            g1[n] = pow(win[c], 0.5)
            g2[n] = pow(win[fade+c], 0.5)
            c = c + 1

        n = n + 1

    return g1, g2

# # BASICPITCH
# # This script demonstrates a basic example of pitch shifting created by using
# # a modulated time delay.
#
# Fs = 48000
# Ts = 1/Fs
# t = np.arange(0, Fs) * Ts
# f = 110 # Musical note A2 = 110 Hz
# x = np.sin(2 * np.pi * f * t)
#
# # Pitch shift amount
# semitones = -12
# tr = pow(2, (semitones/12))
# dRate = 1 - tr # Delay rate of change
#
# # Conditional to handle pitch up or pitch down
# if dRate > 0: # Pitch decrease
#     d = 0
#     x = np.pad(x, (0, Fs), 'constant') # Prepare for signal to be elongated
#
# else: # Pitch increase
#     # Initialize delay so it is always positive
#     d = len(x) * -dRate
#
# N = len(x)
# y = np.zeros(N)
# buffer = np.zeros(Fs*2)
# M = len(buffer) - 1
# wIndex = (Fs * 2) - 1
#
# for n in range(N):
#     intDelay = int(np.floor(d)) # round down to get previous sample
#     frac = d - intDelay # find fractional amount
#
#     rIndex = wIndex - intDelay  # set location of read index
#
#     # Ensure read index is not exceeding the length of the buffer
#     if rIndex < 0:
#         rIndex += M
#
#     # Ensure read index does not go out of bounds of the buffer
#     if rIndex == 0:
#         y[n] = (1-frac) * buffer[rIndex] + frac * buffer[M]
#     else:
#         y[n] = (1-frac) * buffer[rIndex] + frac * buffer[rIndex - 1]
#
#     # Store the current output in circular buffer
#     buffer[wIndex] = x[n]
#     wIndex += 1
#     if wIndex > M:
#         wIndex = 1
#
#     d += dRate


def pitchShifter(x, Fs, semitones):
    Ts = 1 / Fs
    N = len(x)  # Total number of samples
    out = np.zeros(N)
    y1 = np.zeros(N)
    y2 = np.zeros(N)
    lfo1 = np.zeros(N)  # for visualizing LFOs
    lfo2 = np.zeros(N)

    maxDelay = int(Fs * .05)  # Maximum delay is 50ms
    buffer1 = np.zeros(maxDelay + 1)
    buffer2 = np.zeros(maxDelay + 1)
    wIndex1 = maxDelay
    wIndex2 = maxDelay

    tr = pow(2, semitones / 12)  # Convert semitones
    dRate = 1 - tr  # Delay rate of change

    tau = (maxDelay / abs(dRate)) * Ts  # Period of sawtooth LFO
    freq = 1 / tau  # Frequency of LFO

    fade = round((tau * Fs) / 8)  # Fade length is 1/8 of a cycle
    Hz = (freq / 2) * (8 / 7)  # Frequency crossfade due to overlap
    g1, g2 = crossfades(Fs, N, Hz, fade)  # Crossfade gains

    if dRate > 0:  # Pitch decrease
        # Initialize delay so LFO cycles line up with crossfade
        d1 = dRate * fade
        d2 = maxDelay
        d1Temp = d1  # These variables are used to control the length of
        d2Temp = d2  # each cycle of the LFO for the proper amount of overlap

    else:  # Pitch increase
        # Initialize delay so LFO cycles line up with crossfade
        d1 = maxDelay - (maxDelay / 8)
        d2 = 0
        d1Temp = d1
        d2Temp = d2

    # Loop to process input signal
    for n in range(N):
        # Parallel delay processing of the input signal
        intDelay1 = int(np.floor(d1))  # round down to get previous sample
        intDelay2 = int(np.floor(d2))

        frac1 = d1 - intDelay1  # find fractional amount
        frac2 = d2 - intDelay2

        rIndex1 = wIndex1 - intDelay1  # set location of read index
        rIndex2 = wIndex2 - intDelay2

        # Ensure read index is not exceeding the length of the buffer
        if rIndex1 < 0:
            rIndex1 += maxDelay

        if rIndex2 < 0:
            rIndex2 += maxDelay

        # Ensure read index does not go out of bounds of the buffer
        if rIndex1 == 0:
            y1 = (1 - frac1) * buffer1[rIndex1] + frac1 * buffer1[maxDelay]
        else:
            y1 = (1 - frac1) * buffer1[rIndex1] + frac1 * buffer1[rIndex1 - 1]

        if rIndex2 == 0:
            y2 = (1 - frac2) * buffer2[rIndex2] + frac2 * buffer2[maxDelay]
        else:
            y2 = (1 - frac2) * buffer2[rIndex2] + frac2 * buffer2[rIndex2 - 1]

        # Store the current output in circular buffer
        buffer1[wIndex1] = x[n]
        buffer2[wIndex2] = x[n]

        wIndex1 += 1
        if wIndex1 > maxDelay:
            wIndex1 = 1

        wIndex2 += 1
        if wIndex2 > maxDelay:
            wIndex2 = 1

        # Use crossfade gains to combine the output of each delay
        out[n] = g1[n] * y1 + g2[n] * y2

        lfo1[n] = d1  # Save the current delay times for plotting
        lfo2[n] = d2

        # The following conditions are set up to control the
        # overlap of the sawtooth LFOs
        if dRate < 0:  # Slope of LFO is negative (pitch up)
            d1 += dRate
            d1Temp += dRate
            if d1 < 0:
                d1 = 0  # Portion of LFO where delay time = 0

            if d1Temp < -maxDelay * (6 / 8):  # Start next cycle
                d1 = maxDelay
                d1Temp = maxDelay

            d2 += dRate
            d2Temp += dRate
            if d2 < 0:
                d2 = 0  # Portion of LFO where delay time = 0

            if d2Temp < -maxDelay * (6 / 8):  # Start next cycle
                d2 = maxDelay
                d2Temp = maxDelay

        else:  # Slope of LFO is positive (pitch down)
            d1Temp += dRate
            if d1Temp > maxDelay:  # Start next cycle
                d1 = 0
                d1Temp = -maxDelay * (6 / 8)

            elif d1Temp < 0:
                d1 = 0  # Portion where delay time = 0

            else:
                d1 += dRate

            d2Temp += dRate
            if d2Temp > maxDelay:  # Start next cycle
                d2 = 0
                d2Temp = -maxDelay * (6 / 8)

            elif d2Temp < 0:
                d2 = 0  # Portion where delay time = 0

            else:
                d2 += dRate

    # Plotting
    t = np.arange(0, N) * Ts
    plt.subplot(4, 1, 1)  # Waveform
    plt.plot(t, lfo1, t, lfo2)
    plt.axis([0, t[-1], -100, maxDelay])
    plt.ylabel('Delay')

    plt.subplot(4, 1, 2)
    plt.plot(t, g1, t, g2)  # Crossfade gains
    plt.axis([0, t[-1], -0.1, 1.1])
    plt.ylabel('Amplitude')

    plt.figure()
    nfft = 2048  # Length of each time frame
    window = signal.windows.hann(nfft)  # Calculated window function
    overlap = 128  # Number of samples for frame overlap
    spec, f, tSpec, imAxis = plt.specgram(out)
    plt.show()

    return out

# FIX THIS SCRIPT!!!!

# PITCHSHIFTEREXAMPLE
# This script is an example to demonstrate the pitchShifter function
# for processing an audio signal. The desired number of semitones
# can be set from within this script.

# Import acoustic guitar recording for processing
x, Fs = sf.read('AcGtr.wav')

# Experiment with different values
semitones = 1

out = pitchShifter(x, Fs, semitones=semitones)
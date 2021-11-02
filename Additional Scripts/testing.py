
import matplotlib.pyplot as plt
import numpy as np
import soundfile
import audiofile
import pandas as pd
from scipy import signal
from scipy.io import wavfile
from IPython.display import Audio
from pydub import AudioSegment
from scipy.fftpack import fft, fftfreq, ifft

def apf(x, buffer, Fs, n, delay, gain, amp, rate):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = amp * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(np.mod(n, M)) # Current index
    indexD = int(np.mod((n-delay+intDelay), M)) # Delay index
    indexF = int(np.mod((n-delay+intDelay+1), M)) # Fractional index

    # Temp variable for output of delay buffer
    w = (1 - frac) * buffer[indexD] + frac * buffer[indexF]

    # Temp variable used for the node after the input sum
    v = x + (-gain * w)

    # Summation at output
    out = (gain * v) + w

    # Store the current input to delay buffer
    buffer[indexC] = v

    return out, buffer

# EARLYREFLECTIONS
# This function creates a tapped delay line to be used for the early
# reflections of a reverb algorithm. THe delays and gains of the taps
# are included in this function and were based on an IR measurement from a
# recording studio in Nashville, TN.
#
# Also see MOORERREVERB

def earlyReflections(x, buffer, Fs, n):

    # Delay times converted from milliseconds
    delayTimes = [np.fix(0*Fs), np.fix(0.01277*Fs), np.fix(0.01283*Fs), np.fix(0.01293*Fs), np.fix(0.01333*Fs),
                              np.fix(0.01566*Fs), np.fix(0.02404*Fs), np.fix(0.02679*Fs), np.fix(0.02731*Fs), np.fix(0.02737*Fs), np.fix(0.02914*Fs),
                              np.fix(0.02920*Fs), np.fix(0.02981*Fs), np.fix(0.03389*Fs), np.fix(0.04518*Fs), np.fix(0.04522*Fs), np.fix(0.04527*Fs),
                              np.fix(0.05452*Fs), np.fix(0.06958*Fs)]

    numDelays = len(delayTimes)
    for delay in range(numDelays):
        delayTimes[delay] = int(delayTimes[delay])

    # There must be a 'gain' for each of the 'delayTimes'
    gains = [1, 0.1526, -0.4097, 0.2984, 0.1553, 0.1442,
             -0.3124, -0.4176, -0.9391, 0.6926, -0.5787, 0.5782,
             0.4206, 0.3958, 0.3450, -0.5361, 0.417, 0.1948, 0.1548]

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = np.mod(n, M) # current index
    buffer[indexC] = x

    out = 0 # initialize the output to be used in loop

    # Loop through all the taps
    for tap in range(len(delayTimes)):
        # Find the circular buffer index for the current tap
        indexTDL = np.mod(n-delayTimes[tap], M)

        if indexTDL == 3088:
            out = out

        # 'Tap' the delay line and add current tap with output
        out = out + gains[tap] * buffer[indexTDL]

    return out, buffer

#%%

# LPCF
# This function creates a feedback comb filter with a LPF in the feedback
# path.
#
# Input Variables
#   n: current sample number of the input signal
#   delay: samples of delay
#   fbGain: feedback gain (linear scale)
#   amp: amplitude of LFO modulation
#   rate: frequency of LFO modulation
#   fbLPF: output delayed one sample to create basic LPF
#
# See also MOORERREVERB

def lpcf(x, buffer, Fs, n, delay, fbGain, amp, rate, fbLPF):
    # Calculate time in seconds for the current sample
    t = n/Fs
    fracDelay = amp * np.sin(2 * np.pi * rate * t)
    intDelay = int(np.floor(fracDelay))
    frac = fracDelay - intDelay

    # Determine indexes for circular buffer
    M = len(buffer)
    indexC = int(np.mod(n, M))  # Current index
    indexD = int(np.mod((n - delay + intDelay), M))  # Delay index
    indexF = int(np.mod((n - delay + intDelay + 1), M))  # Fractional index

    out = (1 - frac) * buffer[indexD] + frac * buffer[indexF]

    # Store the current output in appropriate index. The LPF is created
    # by adding the current output with the previous sample, both are
    # weighted 0.5.
    buffer[indexC] = x + fbGain * (0.5 * out + 0.5 * fbLPF)

    # Store the current output for the feedback LPF to be used with the
    # next sample.
    fbLPF = out

    return out, buffer, fbLPF


#%%

# MOORERREVERB
# This script implements the Moorer reverb algorithm by modifying the
# Schroeder reverb script. First, an additional step to add early reflections
# is included. Second, a simple low-pass filter is included in the feedback
# path of the comb filters.
#
# See also EARLYREFLECTIONS, LPCF

x, Fs = soundfile.read('AcGtr.wav')
x = np.append(x, np.zeros(Fs*3)) # Add zero-padding for reverb tail

# Max delay of 70ms
maxDelay = int(np.ceil(0.07 * Fs))
# Initialize all buffers
buffer1 = np.zeros(maxDelay)
buffer2 = np.zeros(maxDelay)
buffer3 = np.zeros(maxDelay)
buffer4 = np.zeros(maxDelay)
buffer5 = np.zeros(maxDelay)
buffer6 = np.zeros(maxDelay)

# Early reflections tapped delay line
bufferER = np.zeros(maxDelay)

# Delay and gain parameters
d1 = np.fix(0.0297 * Fs)
g1 = 0.9
d2 = np.fix(0.0371 * Fs)
g2 = -0.9
d3 = np.fix(0.0411 * Fs)
g3 = 0.9
d4 = np.fix(0.0437 * Fs)
g4 = -0.9
d5 = np.fix(0.005 * Fs)
g5 = 0.7
d6 = np.fix(0.0017 * Fs)
g6 = 0.7

# LFO parameters
rate1 = 0.6
amp1 = 8
rate2 = 0.71
amp2 = 8
rate3 = 0.83
amp3 = 8
rate4 = 0.95
amp4 = 8
rate5 = 1.07
amp5 = 8
rate6 = 1.19
amp6 = 8

# Variables used as delay for a simple LPF in each comb filter function
fbLPF1 = 0
fbLPF2 = 0
fbLPF3 = 0
fbLPF4 = 0

# Initialize output signal
N = len(x)
out = np.zeros(N)

for n in range(N):
    # Early reflections TDL
    w0, bufferER = earlyReflections(x[n], bufferER, Fs, n)

    # Four parallel LPCFs
    w1, buffer1, fbLPF1 = lpcf(w0, buffer1, Fs, n, d1, g1, amp1, rate1, fbLPF1)
    w2, buffer2, fbLPF2 = lpcf(w0, buffer2, Fs, n, d2, g2, amp2, rate2, fbLPF2)
    w3, buffer3, fbLPF3 = lpcf(w0, buffer3, Fs, n, d3, g3, amp3, rate3, fbLPF3)
    w4, buffer4, fbLPF4 = lpcf(w0, buffer4, Fs, n, d4, g4, amp4, rate4, fbLPF4)

    # Combine parallel paths
    combPar = 0.25 * (w1 + w2 + w3 + w4)

    # Two series all-pass filters
    w5, buffer5 = apf(combPar, buffer5, Fs, n, d5, g5, amp5, rate5)
    out[n], buffer6 = apf(w5, buffer6, Fs, n, d6, g6, amp6, rate6)

Audio(out, rate=Fs)
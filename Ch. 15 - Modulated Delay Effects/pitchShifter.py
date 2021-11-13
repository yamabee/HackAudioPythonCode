# PITCHSHIFTER
# This function implements the pitch shifter audio effect by using two parallel
# delay lines. The delay time for each line is modulated by a sawtooth LFO. The
# frequency of the LFO is based on the desired number of semitones for the
# pitch shifter. Both increases and decreases in pitch are possible with this
# function.
#
# Both LFOs repeat a cycle such that the delay time stays within a range of 0ms
# to 50ms. This way the processed signal is not significantly shorter or longer
# than the original signal.
#
# The cycles of the two LFOs are intentionally offset to have an overlap. An
# amplitude crossfade is applied to the delay lines to switch between the two
# during the overlap. The crossfade reduces the audibility of the relatively
# large discontinuity in the delay time at the start of the LFO cycle.
#
# See also PITCHSHIFTEREXAMPLE, CROSSFADES, LFOPITCH

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from crossfades import crossfades


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

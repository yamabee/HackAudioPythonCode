# BIQUADFILTER
# This function implements a bi-quad filter based on the Audio EQ Cookbook
# Coefficients. All filter types can be specified (LPF, HPF, BPF, etc.) and
# three different topologies are included.
#
# Input Variables
#   f0: filter frequency
#   Q: bandwidth parameter
#   dBGain: gain value on the decibel scale
#   type: 'lpf', 'hpf', 'pkf', 'bp1', 'bp2', 'apf', 'lsf', 'hsf'
#   form: 1 (Direct Form I), 2 (DFII), 3 (Transposed DFII)

import numpy as np


def biquadFilter(x, Fs, f0, Q, dBGain, type, form):
    N = len(x)
    out = np.zeros(N)

    w0 = 2 * np.pi * f0/Fs  # Angular freq. (radians/sample)
    alpha = np.sin(w0)/(2 * Q)  # Filter Width
    A = np.sqrt(pow(10, dBGain/20))

    if type == 'lpf':
        b0 = (1 - np.cos(w0))/2
        b1 = 1 - np.cos(w0)
        b2 = (1 - np.cos(w0))/2
        a0 = 1 + alpha
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha

    elif type == 'hpf':
        b0 = (1 + np.cos(w0))/2
        b1 = -(1 + np.cos(w0))
        b2 = (1 + np.cos(w0))/2
        a0 = 1 + alpha
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha

    elif type == 'pkf':
        b0 = 1 + alpha * A
        b1 = -2 * np.cos(w0)
        b2 = 1 - alpha * A
        a0 = 1 + alpha/A
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha/A

    elif type == 'bp1':
        b0 = np.sin(w0)/2
        b1 = 0
        b2 = -np.sin(w0)/2
        a0 = 1 + alpha
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha

    elif type == 'bp2':
        b0 = alpha
        b1 = 0
        b2 = -alpha
        a0 = 1 + alpha
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha

    elif type == 'nch':
        b0 = 1
        b1 = -2 * np.cos(w0)
        b2 = 1
        a0 = 1 + alpha
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha

    elif type == 'apf':
        b0 = 1 - alpha
        b1 = -2 * np.cos(w0)
        b2 = 1 + alpha
        a0 = 1 + alpha
        a1 = -2 * np.cos(w0)
        a2 = 1 - alpha

    elif type == 'lsf':
        b0 = A * ((A + 1) - (A-1) * np.cos(w0) + 2 * np.sqrt(A) * alpha)
        b1 = 2 * A * ((A-1) - (A+1)*np.cos(w0))
        b2 = A * ((A+1) - (A-1) * np.cos(w0) + 2 * np.sqrt(A) * alpha)
        a0 = (A+1) + (A-1)*np.cos(w0) + 2 * np.sqrt(A) * alpha
        a1 = -2 * ((A-1) + (A+1) * np.cos(w0))
        a2 = (A+1) + (A-1) * np.cos(w0) - 2 * np.sqrt(A) * alpha

    elif type == 'hsf':
        b0 = A * ((A + 1) + (A-1) * np.cos(w0) + 2 * np.sqrt(A) * alpha)
        b1 = -2 * A * ((A-1) + (A+1)*np.cos(w0))
        b2 = A * ((A+1) + (A-1) * np.cos(w0) - 2 * np.sqrt(A) * alpha)
        a0 = (A+1) - (A-1)*np.cos(w0) + 2 * np.sqrt(A) * alpha
        a1 = 2 * ((A-1) - (A+1) * np.cos(w0))
        a2 = (A+1) - (A-1) * np.cos(w0) - 2 * np.sqrt(A) * alpha

    else:
        b0 = 1
        b1 = 0
        b2 = 0
        a0 = 1
        a1 = 0
        a2 = 0

    if form == 1:
        x2 = 0
        x1 = 0
        y2 = 0
        y1 = 0

        for n in range(N):
            out[n] = (b0/a0) * x[n] + (b1/a0) * x1 + (b2/a0) * x2 + (-a1/a0) * y1 + (-a2/a0) * y2
            x2 = x1
            x1 = x[n]
            y2 = y1
            y1 = out[n]

    elif form == 2:
        w1 = 0
        w2 = 0
        for n in range(N):
            w = x[n] + (-a1/a0) * w1 + (-a2/a0) * w2
            out[n] = (b0/a0) * w + (b1/a0) * w1 + (b2/a0) * w2
            w2 = w1
            w1 = w

    elif form == 3:
        d1 = 0
        d2 = 0
        for n in range(N):
            out[n] = (b0/a0) * x[n] + d1
            d1 = (b1/a0) * x[n] + (-a1/a0) * out[n] + d2
            d2 = (b2/a0) * x[n] + (-a2/a0) * out[n]

    else:
        out = x

    return out

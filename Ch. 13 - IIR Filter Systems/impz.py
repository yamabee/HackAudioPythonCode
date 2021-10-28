# IMPZ

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def impz(b,a):
    impulse = np.repeat(0., 60)
    impulse[0] = 1.
    x = np.arange(0, 60)

    response = signal.lfilter(b, a, impulse)

    plt.figure(figsize=(10,6))
    plt.subplot(2,2,1)
    plt.stem(x, response, 'm', use_line_collection=True)
    plt.xlabel(r'n (samples)', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.title(r'Impulse Response', fontsize=15)

    plt.show()

    return response
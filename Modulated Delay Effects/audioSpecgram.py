# AUDIOSPECGRAM
# This script displays a spectrogram of an audio signal using the
# Mat Plot Library.
#
# See also SPECTROGRAM

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

x, Fs = sf.read('AcGtr.wav')
N = len(x)
# Waveform
t = np.arange(0, N) / Fs
plt.subplot(311)
plt.plot(t,x)
plt.axis([0, N / Fs, -1, 1])

# Spectrogram
nfft = 2048 # Length of each time frame
window = np.hanning(nfft) # Calculated windowing function
overlap = 128 # Number of samples for frame overlap

plt.subplot(312)
spec, f, t, imAxis = plt.specgram(x,nfft, Fs, window=window, noverlap=overlap)
# f, t, Sxx = signal.spectrogram(x,fs=Fs, window=window, noverlap=overlap, nfft=nfft)
plt.axis('tight')
plt.axis('auto')
plt.xlabel('Time (sec.)')
plt.ylabel('Freq. (Hz)')
plt.show()
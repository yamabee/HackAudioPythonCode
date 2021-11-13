# IMPIIR
# This script demonstrates one example to approximate the impulse response
# of an IIR system.
#
# See also IMPFIR

import numpy as np
import matplotlib.pyplot as plt
import soundfile

Fs = 48000
Ts = 1/Fs
N = Fs * 2 # Number of samples
# Synthesize impulse signal
imp = np.zeros([N, 1])
imp[1] = 1 # Change the first sample = 1

out = np.zeros([N * 5, 1])

d1 = int(0.5 * Fs) # 1/2 second delay
a1 = -0.7 # Gain of feedback delay line

# Index each element of our signal to create the output
for n in range(d1):
    out[n] = imp[n] # Initially there is no delay

for n in np.arange(d1+1, Fs*2): # Then there is signal + delay
    out[n] = imp[n] + a1 * out[n - d1]

for n in np.arange(Fs*2+1, Fs*10): # Finally, there is only delay
    out[n] = a1 * out[n - d1] # After input finished


t = np.arange(0, N) / Fs
plt.subplot(1,2,1)
plt.stem(t, imp) # Plot the impulse response
plt.axis([-0.1, 2, -0.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Input Impulse')
plt.show()

t = np.arange(0, Fs * 10) * Ts
plt.subplot(1,2,2)
plt.stem(t, out) # Plot the impulse response
plt.axis([-0.1, 10, -1.1, 1.1])
plt.xlabel('Time (sec.)')
plt.title('Output Impulse Response')
plt.show()

# soundfile.write('impResp.wav', imp, Fs)
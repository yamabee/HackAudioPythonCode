# ADSREXAMPLE
# This script creates a linear ADSR amplitude envelope.
#
# See also ADSR

import numpy as np
import matplotlib.pyplot as plt

# Number of samples per fade
a = 20
d = 20
s = 70
r = 40

sustainAmplitude = 0.75

# create each segment A, D, S, R
aFade = np.linspace(0, 1, a)
dFade = np.linspace(1, sustainAmplitude, d)
sFade = sustainAmplitude * np.ones(s)
rFade = np.linspace(sustainAmplitude, 0, r)

# Concatenates total ADSR envelope
env = np.append(aFade, dFade)
env = np.append(env, sFade)
env = np.append(env, rFade)

plt.plot(env)
plt.show()
import numpy as np

def fractionalDelay(x, buffer, delay):
    intDelay = int(np.floor(delay))
    frac = delay - intDelay
    if intDelay == 0:
        out = (1-frac) * x + frac * buffer(0)

    else:
        out = (1-frac) * buffer(intDelay - 1) + frac * buffer(intDelay)

    # Store the current output in appropriate index
    buffer = np.append(x, buffer[1:-1])

    return out, buffer
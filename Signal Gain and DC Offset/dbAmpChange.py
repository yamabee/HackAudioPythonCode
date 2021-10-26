# DBAMPCHANGE This function changes the amplitude of a signal.
# This function changes the amplitude of a input signal based on
# a desired change relative to a decibel scale.

def db_amp_change(x, db_change):
    scale = pow(10, db_change/20) # Convert from decibel to linear
    return scale * x # Apply linear amplitude to signal
# LUFSEXAMPLE
# This script demonstrates the use of the lufs function
# for calculating loudness based on the LUFS/LKFS standard.
# Four examples are shown. First, a mono recording of a
# guitar is analyzed. Second, a stereo recording of
# drums is analyzed.
#
# Then, two more examples are demonstrated using test signals
# provided by the European Broadcast Union (EBU) for the sake
# of verifying proper measurement. A filtered pink noise signal
# is measured with a loudness of -23 LUFS. Finally, a sine wave
# signal is measured with a loudness of -40 LUFS.
#
# See also LUFS

import soundfile
from lufs import lufs

# Example 1 - Guitar
sig_1, Fs = soundfile.read('AcGtr.wav')
loudnessGuit = lufs(sig_1)
print('LUFS of Example 1: ' + str(loudnessGuit))

# Example 2 - Stereo drums
sig_2, Fs = soundfile.read('distDrums.wav')
loudnessDrums = lufs(sig_2)
print('LUFS of Example 2: ' + str(loudnessDrums))

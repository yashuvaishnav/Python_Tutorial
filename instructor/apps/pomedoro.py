import time
import os
import sys

minutes = 0.2 # default keep 20 mins
interval = minutes * 60  # in seconds
duration = 1  # seconds
freq = 440  # Hz

while True:
    time.sleep(2)
    # Print message
    print("Look away for 20 seconds!")
    # Optional beep sound on Linux/macOS
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    os.system('spd-say "Time for a break"')

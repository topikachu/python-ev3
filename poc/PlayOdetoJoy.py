import wave
import struct
from ev3.rawdevice import Sound
import time

frequency=[ 523, 578, 659, 698, 784, 880, 988 ]




notes=[ 3, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 3, 2, 2, 3, 3,
                4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 2, 1, 1 ]
beats=[ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 4, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 4 ]
Sound.init()

for (note,beat) in zip(notes, beats):
    print frequency[note],beat
    Sound.playTone(frequency[note],beat*100*2)
    time.sleep(beat/10.0*2)

Sound.close()

    
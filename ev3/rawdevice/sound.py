import os
import struct
from . import lms2012

_initialized = False
_soundfile = None


def open_device():
    global _initialized
    if not _initialized:
        global _soundfile
        _soundfile = os.open(lms2012.SOUND_DEVICE_NAME, os.O_RDWR)
        _initialized = True


def play_tone(frequency, duration, volume=100):
    os.write(_soundfile, struct.pack('B' * 6, lms2012.TONE, volume * 13 / 100,
             frequency & 0xff, frequency >> 8, duration & 0xff, duration >> 8))


def close_device():
    global _initialized
    if _initialized:
        os.close(_soundfile)
        _initialized = False

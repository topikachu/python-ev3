import os
import time
from mmap import *
from . import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime
import struct

isInitialized=False
soundfile=None

def init():
    global isInitialized    
    if not isInitialized:
        global soundfile
        soundfile=os.open(lms2012.SOUND_DEVICE_NAME,os.O_RDWR)
        isInitialized=True


def playTone(frequency, duration, volume=100):
    os.write(soundfile,struct.pack('B'*6,lms2012.TONE,volume*13/100,frequency & 0xff,frequency >> 8,duration & 0xff,duration >> 8))
    

def close():
    global isInitialized    
    if isInitialized:
        os.close(soundfile)
        isInitialized=False
    



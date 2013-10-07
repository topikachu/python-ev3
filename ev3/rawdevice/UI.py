import os
import time
from mmap import *
from . import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime
import struct
import array

isInitialized=False
uifile=None
uimm=None
ui=None

def init():
    global isInitialized
    if not isInitialized:
        global uifile
        uifile=os.open(lms2012.UI_DEVICE_NAME,os.O_RDWR | os.O_SYNC)
        global uimm
        uimm=mmap(fileno=uifile, length=sizeof(lms2012.UI),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global ui
        ui=lms2012.UI.from_buffer(uimm)
        isInitialized=True

def setLed(light):
    os.write(uifile,struct.pack('BB',ord('0')+light,0))

def isPressed(key):
    return ui.Pressed[key]

def close():
    global isInitialized
    if isInitialized:
        uimm.close()
        os.close(uifile)
        isInitialized=False







    











import os
import time
from mmap import *
from . import lms2012
from . import lms2012extra
from fcntl import ioctl
from ctypes import sizeof

isInitialized=False
dcmfile=None

def init():
    global isInitialized
    if not isInitialized:        
        global dcmfile        
        dcmfile=os.open(lms2012.DCM_DEVICE_NAME,os.O_RDWR)
        isInitialized=True

def setPinMode(port, pin):
    buf = bytearray('-'*4)
    buf[port]=pin
    os.write(dcmfile,buf);

def close():
    global isInitialized
    if isInitialized:
        os.close(dcmfile)
        isInitialized=False
        

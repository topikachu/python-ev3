from ctypes import sizeof
from fcntl import ioctl
from mmap import *
import os
import time

from . import lms2012, lms2012extra


isInitialized=False
dcmfile=None

def open():
    global isInitialized
    if not isInitialized:        
        global dcmfile        
        dcmfile=os.open(lms2012.DCM_DEVICE_NAME,os.O_RDWR)
        isInitialized=True

def set_pin_mode(port, pin):
    buf = bytearray('-'*4)
    buf[port]=pin
    os.write(dcmfile,buf);

def close():
    global isInitialized
    if isInitialized:
        os.close(dcmfile)
        isInitialized=False
        

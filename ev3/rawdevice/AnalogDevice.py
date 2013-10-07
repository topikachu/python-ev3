import os
import time
from mmap import *
from . import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime


isInitialized=False
analogfile=None
analogmm=None
analog=None
def init():
    global isInitialized    
    if not isInitialized:
        analogfile=os.open(lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)
        global analogmm
        analogmm=mmap(fileno=analogfile, length=sizeof(lms2012.ANALOG),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global analog
        analog=lms2012.ANALOG.from_buffer(analogmm)
        isInitialized=True
def getPin6(port):
    return analog.InPin6[port]
def getPin1(port):
    return analog.InPin1[port]

def close():
    global isInitialized    
    if isInitialized:
        analogmm.close()
        os.close(analogfile)
        isInitialized=False
    



from ctypes import sizeof
import datetime
from fcntl import ioctl
from mmap import *
import os
import time

from . import lms2012


isInitialized=False
analogfile=None
analogmm=None
analog=None
def open():
    global isInitialized    
    if not isInitialized:
        global analogfile
        analogfile=os.open(lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)
        global analogmm
        analogmm=mmap(fileno=analogfile, length=sizeof(lms2012.ANALOG),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global analog
        analog=lms2012.ANALOG.from_buffer(analogmm)
        isInitialized=True
def get_pin6(port):
    return analog.InPin6[port]
def get_pin1(port):
    return analog.InPin1[port]

def get_connection_type(port):
    print lms2012.CtoV(analog.InPin1[port])
    return analog.InConn[port]


def clear_change(port):
    analog.Updated[port] =  0


def close():
    global isInitialized    
    if isInitialized:
        analogmm.close()
        os.close(analogfile)
        isInitialized=False
    



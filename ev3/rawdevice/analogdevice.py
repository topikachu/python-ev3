from ctypes import sizeof
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os

from . import lms2012


_initialized=False
_analogfile=None
_analogmm=None
_analog=None
def open_device():
    global _initialized    
    if not _initialized:
        global _analogfile
        _analogfile=os.open(lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)
        global _analogmm
        _analogmm=mmap(fileno=_analogfile, length=sizeof(lms2012.ANALOG),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global _analog
        _analog=lms2012.ANALOG.from_buffer(_analogmm)
        _initialized=True
def get_pin6(port):
    return _analog.InPin6[port]
def get_pin1(port):
    return _analog.InPin1[port]

def get_connection_type(port):
    print lms2012.CtoV(_analog.InPin1[port])
    return _analog.InConn[port]


def clear_change(port):
    _analog.Updated[port] =  0


def close_device():
    global _initialized    
    if _initialized:
        _analogmm.close()
        os.close(_analogfile)
        _initialized=False
    



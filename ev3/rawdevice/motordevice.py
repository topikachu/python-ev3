from ctypes import sizeof
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os
import struct

from . import lms2012


_initialized=False
_pwmfile=None
_motorfile=None
_motormm=None
_motodata=None


def open_device():
    global _initialized
    if not _initialized:
        global _pwmfile
        _pwmfile=os.open(lms2012.PWM_DEVICE_NAME,os.O_RDWR)
        global _motorfile
        _motorfile=os.open(lms2012.MOTOR_DEVICE_NAME,os.O_RDWR)
        MOTORDATAArrray=lms2012.MOTORDATA * 4
        global _motormm
        _motormm=mmap(fileno=_motorfile, length=sizeof(MOTORDATAArrray),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)    
        global _motodata
        _motodata=MOTORDATAArrray.from_buffer(_motormm)
        _initialized=True

def start(port):
    os.write(_pwmfile, struct.pack('BB',lms2012.opOUTPUT_START,1<<port))
def stop(port):
    os.write(_pwmfile, struct.pack('BBB',lms2012.opOUTPUT_STOP,1<<port,0))
def power(port,power):
    os.write(_pwmfile, struct.pack('BBB',lms2012.opOUTPUT_POWER,1<<port,power))
def get_speed(port):
    return _motodata[port].Speed
def get_tacho(port):
    return _motodata[port].TachoCounts

def close_device():
    global _initialized
    if _initialized:
        _motormm.close()
        os.close(_motorfile)
        os.close(_pwmfile)
        _initialized=False













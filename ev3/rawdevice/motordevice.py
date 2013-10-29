from ctypes import sizeof
import datetime
from fcntl import ioctl
from mmap import *
import os
import struct
import time

from . import lms2012


isInitialized=False
pwmfile=None
motorfile=None
motormm=None
motodata=None


def open():
    global isInitialized
    if not isInitialized:
        global pwmfile
        pwmfile=os.open(lms2012.PWM_DEVICE_NAME,os.O_RDWR)
        global motorfile
        motorfile=os.open(lms2012.MOTOR_DEVICE_NAME,os.O_RDWR)
        MOTORDATAArrray=lms2012.MOTORDATA * 4
        global motormm
        motormm=mmap(fileno=motorfile, length=sizeof(MOTORDATAArrray),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)    
        global motodata
        motodata=MOTORDATAArrray.from_buffer(motormm)
        isInitialized=True

def start(port):
    os.write(pwmfile, struct.pack('BB',lms2012.opOUTPUT_START,1<<port))
def stop(port):
    os.write(pwmfile, struct.pack('BBB',lms2012.opOUTPUT_STOP,1<<port,0))
def power(port,power):
    os.write(pwmfile, struct.pack('BBB',lms2012.opOUTPUT_POWER,1<<port,power))
def get_speed(port):
    return motodata[port].Speed
def get_tacho(port):
    return motodata[port].TachoCounts

def close():
    global isInitialized
    if isInitialized:
        motormm.close()
        os.close(motorfile)
        os.close(pwmfile)
        isInitialized=False













import os
import time
from mmap import *
from . import lms2012
from . import lms2012extra
from fcntl import ioctl
from ctypes import sizeof
import datetime


from . import devcon
from . import Dcm

INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;




isInitialized=False
iicfile=None
iicmm=None
iic=None

def init():
    global isInitialized
    if not isInitialized:        
        global iicfile        
        iicfile=os.open(lms2012.IIC_DEVICE_NAME,os.O_RDWR)
        global iicmm        
        iicmm=mmap(fileno=iicfile, length=sizeof(lms2012.IIC),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global iic
        iic=lms2012.IIC.from_buffer(iicmm)
        isInitialized=True



def setOperatingMode(port, typ, mode):
    devcon.Connection[port]=lms2012.CONN_NXT_IIC
    devcon.Type[port]=typ
    devcon.Mode[port]=mode
    ioctl(iicfile, lms2012extra.IIC_SET_CONN, devcon);        
    

def reset(port):
    Dcm.setPinMode(port,'f')
    time.sleep(0.1)
    devcon.Connection[port]=lms2012.CONN_NONE
    devcon.Type[port]=0
    devcon.Mode[port]=0
    ioctl(iicfile,lms2012extra.IIC_SET_CONN, devcon)
    time.sleep(0.1)
    setOperatingMode(port,lms2012.TYPE_IIC_UNKNOWN, 255);
    time.sleep(0.1)
    setOperatingMode(port,lms2012.TYPE_IIC_UNKNOWN, 255);
    
def i2cTransaction(port,deviceAddress, writeBuf, readLen):    
        iicdata=lms2012.IICDAT()
        iicdata.Port = port
        iicdata.Result = -1
        iicdata.Repeat = 1
        iicdata.Time = 0
        iicdata.WrLng = len(writeBuf)+ 1
        iicdata.WrData[1:len(writeBuf)+1]=writeBuf[:]
        iicdata.WrData[0] = deviceAddress >> 1
        iicdata.RdLng = -readLen
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
        while True:
            ioctl(iicfile, lms2012extra.IIC_SETUP, iicdata)            
            status = iicdata.Result
            if (iicdata.Result == 0):
                return iicdata.RdData[:readLen]
            if datetime.datetime.now()>timeout:
                break
            time.sleep(0.01)
                  
            
    

def close():
    global isInitialized
    if isInitialized:
        iicmm.close()
        os.close(iicfile)
        isInitialized=False


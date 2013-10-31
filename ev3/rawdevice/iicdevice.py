from ctypes import sizeof
import datetime
from fcntl import ioctl
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os
import time

from . import dcm, lms2012, lms2012extra


INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;




_initialized=False
_iicfile=None
_iicmm=None
_iic=None
_devcon=None
def open_device():
    global _initialized
    if not _initialized:        
        global _devcon
        from . import devcon as _devcon
        global _iicfile        
        _iicfile=os.open(lms2012.IIC_DEVICE_NAME,os.O_RDWR)
        global _iicmm        
        _iicmm=mmap(fileno=_iicfile, length=sizeof(lms2012.IIC),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global _iic
        _iic=lms2012.IIC.from_buffer(_iicmm)
        _initialized=True



def set_operating_mode(port, typ, mode):
    _devcon.Connection[port]=lms2012.CONN_NXT_IIC
    _devcon.Type[port]=typ
    _devcon.Mode[port]=mode
    ioctl(_iicfile, lms2012extra.IIC_SET_CONN, _devcon);        
    

def reset(port):
    dcm.set_pin_mode(port,'f')
    time.sleep(0.1)
    _devcon.Connection[port]=lms2012.CONN_NONE
    _devcon.Type[port]=0
    _devcon.Mode[port]=0
    ioctl(_iicfile,lms2012extra.IIC_SET_CONN, _devcon)
    time.sleep(0.1)
    set_operating_mode(port,lms2012.TYPE_IIC_UNKNOWN, 255);
    time.sleep(0.1)
    set_operating_mode(port,lms2012.TYPE_IIC_UNKNOWN, 255);
    
    
def i2c_transaction(port,deviceAddress, writeBuf, readLen):    
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
            ioctl(_iicfile, lms2012extra.IIC_SETUP, iicdata)            
            #status = iicdata.Result
            if (iicdata.Result == 0):
                return iicdata.RdData[:readLen]
            if datetime.datetime.now()>timeout:
                break
            time.sleep(0.01)
                  
            
    

def close_device():
    global _initialized
    if _initialized:
        _iicmm.close()
        os.close(_iicfile)
        _initialized=False


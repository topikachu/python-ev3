from ctypes import sizeof
import datetime
from fcntl import ioctl
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os
import time

from . import  lms2012, lms2012extra


INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;




_initialized=False
_uartfile=None
_uarmm=None
_uart=None
_devcon=None
def open_device():
    global _initialized
    if not _initialized: 
        global _devcon
        from . import devcon as _devcon
        global _uartfile        
        _uartfile=os.open(lms2012.UART_DEVICE_NAME,os.O_RDWR)
        print _uartfile
        global uartmm        
        uartmm=mmap(fileno=_uartfile, length=sizeof(lms2012.UART),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global _uart
        _uart=lms2012.UART.from_buffer(uartmm)
        _initialized=True

def wait_no_zero_status(port):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
    while True:
        status = _uart.Status[port]    
        if status!=0:
            break
        if datetime.datetime.now()>timeout:
            break
        time.sleep(0.025)
    return status




def clear_change(port):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
    while True:

        status = _uart.Status[port]
        if (status & lms2012.UART_DATA_READY) != 0 and (status & lms2012.UART_PORT_CHANGED) == 0:
            break
        if datetime.datetime.now()>timeout:
            break
        _devcon.Connection[port]=lms2012.CONN_INPUT_UART
        _devcon.Type[port]=0
        _devcon.Mode[port]=0
        ioctl(_uartfile,lms2012extra.UART_CLEAR_CHANGED, _devcon)
        _uart.Status[port] = _uart.Status[port] & ~ lms2012.UART_PORT_CHANGED
        time.sleep(0.01)

def set_mode(port,mode):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=5)
    while (True):
        _devcon.Connection[port]=lms2012.CONN_INPUT_UART
        _devcon.Type[port]=0
        _devcon.Mode[port]=mode
        ioctl(_uartfile,lms2012extra.UART_SET_CONN,_devcon)
        status = wait_no_zero_status(port)
        if status & lms2012.UART_PORT_CHANGED:
            clear_change(port)
        else:
            break
        if datetime.datetime.now()>timeout:
            break
        time.sleep(0.01)

def get_value_bytes(port):
    index = _uart.Actual[port]
    return _uart.Raw[port][index]

def get_value_byte(port):
    return get_value_bytes(port)[0]

def reset(port):
    _devcon.Connection[port]=lms2012.CONN_NONE
    _devcon.Type[port]=0
    _devcon.Mode[port]=0
    ioctl(_uartfile,lms2012extra.UART_SET_CONN, _devcon)

def get_mode_info(port,mode):
    uartCtl=lms2012.UARTCTL()
    uartCtl.Port  =  port
    uartCtl.Mode = mode
    ioctl(_uartfile,lms2012extra.UART_READ_MODE_INFO,uartCtl);
    return uartCtl.TypeData


def close_device():
    global _initialized
    if _initialized:
        uartmm.close()
        os.close(_uartfile)
        _initialized=False


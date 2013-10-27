import os
import time
from mmap import *
from . import lms2012
from . import lms2012extra

from fcntl import ioctl
from ctypes import sizeof
import datetime

from . import devcon


INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;




isInitialized=False
uartfile=None
uarmm=None
uart=None

def init():
    global isInitialized
    if not isInitialized:        
        global uartfile        
        uartfile=os.open(lms2012.UART_DEVICE_NAME,os.O_RDWR)
        print uartfile
        global uartmm        
        uartmm=mmap(fileno=uartfile, length=sizeof(lms2012.UART),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global uart
        uart=lms2012.UART.from_buffer(uartmm)
        isInitialized=True

def waitNoZeroStatus(port):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
    while True:
        status = uart.Status[port]    
        if status!=0:
            break
        if datetime.datetime.now()>timeout:
            break
        time.sleep(0.025)
    return status




def clearChange(port):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
    while True:
        status = uart.Status[port]
        if (status & lms2012.UART_DATA_READY) != 0 and (status & lms2012.UART_PORT_CHANGED) == 0:
            break
        if datetime.datetime.now()>timeout:
            break
        devcon.Connection[port]=lms2012.CONN_INPUT_UART
        devcon.Type[port]=0
        devcon.Mode[port]=0
        ioctl(uartfile,lms2012extra.UART_CLEAR_CHANGED, devcon)
        uart.Status[port] = uart.Status[port] & ~ lms2012.UART_PORT_CHANGED
        time.sleep(0.01)

def setMode(port,mode):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=5)
    while (True):
        devcon.Connection[port]=lms2012.CONN_INPUT_UART
        devcon.Type[port]=0
        devcon.Mode[port]=mode
        ioctl(uartfile,lms2012extra.UART_SET_CONN,devcon)
        status = waitNoZeroStatus(port)
        if status & lms2012.UART_PORT_CHANGED:
            clearChange(port)
        else:
            break

def getValueBytes(port):
    index = uart.Actual[port]
    return uart.Raw[port][index]

def getValueByte(port):
    return getValueBytes(port)[0]

def reset(port):
    devcon.Connection[port]=lms2012.CONN_NONE
    devcon.Type[port]=0
    devcon.Mode[port]=0
    ioctl(uartfile,lms2012extra.UART_SET_CONN, devcon)

def getModeInfo(port,mode):
    uartCtl=lms2012.UARTCTL()
    uartCtl.Port  =  port
    uartCtl.Mode = mode
    ioctl(uartfile,lms2012extra.UART_READ_MODE_INFO,uartCtl);
    return uartCtl.TypeData


def close():
    global isInitialized
    if isInitialized:
        uartmm.close()
        os.close(uartfile)
        isInitialized=False


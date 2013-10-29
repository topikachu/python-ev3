from ctypes import sizeof
import datetime
from fcntl import ioctl
from mmap import *
import os
import time

from . import devcon, lms2012, lms2012extra


INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;




isInitialized=False
uartfile=None
uarmm=None
uart=None

def open():
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

def wait_no_zero_status(port):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
    while True:
        status = uart.Status[port]    
        if status!=0:
            break
        if datetime.datetime.now()>timeout:
            break
        time.sleep(0.025)
    return status




def clear_change(port):
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

def set_mode(port,mode):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=5)
    while (True):
        devcon.Connection[port]=lms2012.CONN_INPUT_UART
        devcon.Type[port]=0
        devcon.Mode[port]=mode
        ioctl(uartfile,lms2012extra.UART_SET_CONN,devcon)
        status = wait_no_zero_status(port)
        if status & lms2012.UART_PORT_CHANGED:
            clear_change(port)
        else:
            break

def get_value_bytes(port):
    index = uart.Actual[port]
    return uart.Raw[port][index]

def get_value_byte(port):
    return get_value_bytes(port)[0]

def reset(port):
    devcon.Connection[port]=lms2012.CONN_NONE
    devcon.Type[port]=0
    devcon.Mode[port]=0
    ioctl(uartfile,lms2012extra.UART_SET_CONN, devcon)

def get_mode_info(port,mode):
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


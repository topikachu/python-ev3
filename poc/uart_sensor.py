from ctypes import *
import datetime
from fcntl import ioctl
from mmap import *
import os
import struct
import time

import ev3
from ev3.rawdevice import lms2012
from ev3.rawdevice.lms2012 import UART, UART_DEVICE_NAME


UART_SET_CONN = 0xc00c7500;
UART_READ_MODE_INFO = 0xc03c7501;
UART_NACK_MODE_INFO = 0xc03c7502;
UART_CLEAR_CHANGED = 0xc03c7503;


def resetAll():
    for i in range (0,4):
        devcon.Connection[i]=lms2012.CONN_NONE
        devcon.Type[i]=0
        devcon.Mode[i]=0
        ioctl(uartfile,UART_SET_CONN, devcon)   


def wait_no_zero_status():
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=10)
    while True:
        status = uart.Status[port]    
        if status!=0 or datetime.datetime.now()>timeout:
            break 
        time.sleep(0.025)
    return status



def resetDevice():
    INIT_RETRY=100    
    retryCnt = 0
    while True:
        status = uart.Status[port]
        if (status & lms2012.UART_DATA_READY) != 0 and (status & lms2012.UART_PORT_CHANGED) == 0:
            break
        if retryCnt > INIT_RETRY:
            break
        devcon.Connection[port]=lms2012.CONN_INPUT_UART
        devcon.Type[port]=0
        devcon.Mode[port]=0
        ioctl(uartfile,UART_CLEAR_CHANGED, devcon)
        uart.Status[port] = uart.Status[port] & ~ lms2012.UART_PORT_CHANGED
        retryCnt = retryCnt +1
        time.sleep(0.01)

def setUartMode(mode):
    while (True):
        devcon.Connection[port]=lms2012.CONN_INPUT_UART
        devcon.Type[port]=0
        devcon.Mode[port]=mode
        ioctl(uartfile,UART_SET_CONN,devcon)
        status = wait_no_zero_status()
        if status & lms2012.UART_PORT_CHANGED:
            resetDevice()
        else:
            break

    


def main():

    global uartfile
    uartfile=os.open(UART_DEVICE_NAME,os.O_RDWR)

    mm=mmap(fileno=uartfile, length=sizeof(UART),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)

    global devcon
    devcon=lms2012.DEVCON()
    global uart
    uart=UART.from_buffer(mm)


    resetAll()
    print "reset all"
    time.sleep(2)
    global port

    port=3
    
    setUartMode(2)
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=10)
    while (datetime.datetime.now()<timeout):
        index = uart.Actual[port]
        print index
        print [str(b) for b in uart.Raw[port][index]]
        time.sleep(1)
    mm.close()
    os.close(uartfile)


if __name__ == '__main__':
    main()
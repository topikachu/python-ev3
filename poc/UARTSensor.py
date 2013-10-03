import os
import time
import struct
import ev3
from mmap import *
from ctypes import *
from ev3.cdriver.lms2012 import UART,UART_DEVICE_NAME
from ev3.cdriver import lms2012
from fcntl import ioctl
import datetime

UART_SET_CONN = 0xc00c7500;
UART_READ_MODE_INFO = 0xc03c7501;
UART_NACK_MODE_INFO = 0xc03c7502;
UART_CLEAR_CHANGED = 0xc03c7503;

uartfile=os.open(UART_DEVICE_NAME,os.O_RDWR)

mm=mmap(fileno=uartfile, length=sizeof(UART),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)
uart=UART.from_buffer(mm)
devcon=lms2012.DEVCON()

#connect the color sensor to the 3rd sensor port
port=2 #index from 0
devcon.Connection[port]=lms2012.CONN_NONE
devcon.Type[port]=0
devcon.Mode[port]=0
ioctl(uartfile,UART_SET_CONN,devcon)

COL_AMBIENT = 1
devcon.Connection[port]=lms2012.CONN_INPUT_UART
devcon.Type[port]=0
devcon.Mode[port]=COL_AMBIENT

ioctl(uartfile,UART_SET_CONN,devcon)
   

mm.close()
os.close(uartfile)
import os
import time
from mmap import *
from ev3.cdriver import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime



devcon=lms2012.DEVCON()




UART_SET_CONN = 0xc00c7500;
UART_READ_MODE_INFO = 0xc03c7501;
UART_NACK_MODE_INFO = 0xc03c7502;
UART_CLEAR_CHANGED = 0xc03c7503;

class UARTDevice():
    
    global uartfile
    uartfile=os.open(lms2012.UART_DEVICE_NAME,os.O_RDWR)
    mm=mmap(fileno=uartfile, length=sizeof(lms2012.UART),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)    
    global uart
    uart=lms2012.UART.from_buffer(mm)
    def __init__(self,port):
        self.port=port

    def waitNoZeroStatus(self):
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
        while True:
            status = uart.Status[self.port]    
            if status!=0:
                break
            if datetime.datetime.now()>timeout:
                break
            time.sleep(0.025)
        return status



    def resetDevice(self):
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
        while True:
            status = uart.Status[self.port]
            if (status & lms2012.UART_DATA_READY) != 0 and (status & lms2012.UART_PORT_CHANGED) == 0:
                break
            if datetime.datetime.now()>timeout:
                break
            devcon.Connection[self.port]=lms2012.CONN_INPUT_UART
            devcon.Type[self.port]=0
            devcon.Mode[self.port]=0
            ioctl(uartfile,UART_CLEAR_CHANGED, devcon)
            uart.Status[self.port] = uart.Status[self.port] & ~ lms2012.UART_PORT_CHANGED
            time.sleep(0.01)

    def setMode(self,mode):
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=5)
        while (True):
            devcon.Connection[self.port]=lms2012.CONN_INPUT_UART
            devcon.Type[self.port]=0
            devcon.Mode[self.port]=mode
            ioctl(uartfile,UART_SET_CONN,devcon)
            status = self.waitNoZeroStatus()
            if status & lms2012.UART_PORT_CHANGED:
                self.resetDevice()
            else:
                break

    def getValueBytes(self):
        index = uart.Actual[self.port]
        return uart.Raw[self.port][index]

    def getValueByte(self):
        return self.getValueBytes()[0]

class AnalogDevice():
    global analogfile
    analogfile=os.open(lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)
    mm=mmap(fileno=analogfile, length=sizeof(lms2012.ANALOG),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)
    global analog
    analog=ANALOG.from_buffer(mm)
    def __init__(self,port):
        self.port=port
    def getPin6(self):
        return analog.InPin6[self.port]
    def getPin1(self):
        return analog.InPin1[self.port]


import os
import time
from mmap import *
from ev3.cdriver import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime
import struct


devcon=lms2012.DEVCON()




UART_SET_CONN = 0xc00c7500;
UART_READ_MODE_INFO = 0xc03c7501;
UART_NACK_MODE_INFO = 0xc03c7502;
UART_CLEAR_CHANGED = 0xc03c7503;

INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;

class UARTDevice():
    
   
    uartfile=os.open(lms2012.UART_DEVICE_NAME,os.O_RDWR)   
    uartmm=mmap(fileno=uartfile, length=sizeof(lms2012.UART),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)       
    uart=lms2012.UART.from_buffer(uartmm)
    def __init__(self,port):
        self.port=port

    def waitNoZeroStatus(self):
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
        while True:
            status = UARTDevice.uart.Status[self.port]    
            if status!=0:
                break
            if datetime.datetime.now()>timeout:
                break
            time.sleep(0.025)
        return status




    def clearChange(self):
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=1)
        while True:
            status = UARTDevice.uart.Status[self.port]
            if (status & lms2012.UART_DATA_READY) != 0 and (status & lms2012.UART_PORT_CHANGED) == 0:
                break
            if datetime.datetime.now()>timeout:
                break
            devcon.Connection[self.port]=lms2012.CONN_INPUT_UART
            devcon.Type[self.port]=0
            devcon.Mode[self.port]=0
            ioctl(UARTDevice.uartfile,UART_CLEAR_CHANGED, devcon)
            UARTDevice.uart.Status[self.port] = UARTDevice.uart.Status[self.port] & ~ lms2012.UART_PORT_CHANGED
            time.sleep(0.01)

    def setMode(self,mode):
        timeout=datetime.datetime.now()+datetime.timedelta(seconds=5)
        while (True):
            devcon.Connection[self.port]=lms2012.CONN_INPUT_UART
            devcon.Type[self.port]=0
            devcon.Mode[self.port]=mode
            ioctl(UARTDevice.uartfile,UART_SET_CONN,devcon)
            status = self.waitNoZeroStatus()
            if status & lms2012.UART_PORT_CHANGED:
                self.clearChange()
            else:
                break

    def getValueBytes(self):
        index = UARTDevice.uart.Actual[self.port]
        return UARTDevice.uart.Raw[self.port][index]

    def getValueByte(self):
        return self.getValueBytes()[0]

    def reset(self):
        devcon.Connection[self.port]=lms2012.CONN_NONE
        devcon.Type[self.port]=0
        devcon.Mode[self.port]=0
        ioctl(UARTDevice.uartfile,UART_CLEAR_CHANGED, devcon)
        

    @staticmethod
    def close():
        UARTDevice.uartmm.close()
        os.close(UARTDevice.uartfile)


class AnalogDevice():
    analogfile=os.open(lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)
    analogmm=mmap(fileno=analogfile, length=sizeof(lms2012.ANALOG),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)
    analog=lms2012.ANALOG.from_buffer(analogmm)
    def __init__(self,port):
        self.port=port
    def getPin6(self):
        return AnalogDevice.analog.InPin6[self.port]
    def getPin1(self):
        return AnalogDevice.analog.InPin1[self.port]
    @staticmethod
    def close():
        AnalogDevice.analogmm.close()
        os.close(AnalogDevice.analogfile)
        


class MotorDevice():
    
    pwmfile=os.open(lms2012.PWM_DEVICE_NAME,os.O_RDWR)
    
    
    motorfile=os.open(lms2012.MOTOR_DEVICE_NAME,os.O_RDWR)
    MOTORDATAArrray=lms2012.MOTORDATA * 4
    motormm=mmap(fileno=motorfile, length=sizeof(MOTORDATAArrray),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)    
    motodata=MOTORDATAArrray.from_buffer(motormm)

    def __init__(self,port):
        self.port=port
    def start(self):
        os.write(MotorDevice.pwmfile, struct.pack('BB',lms2012.opOUTPUT_START,1<<self.port))
    def stop(self):
        os.write(MotorDevice.pwmfile, struct.pack('BBB',lms2012.opOUTPUT_STOP,1<<self.port,0))
    def power(self,power):
        os.write(MotorDevice.pwmfile, struct.pack('BBB',lms2012.opOUTPUT_POWER,1<<self.port,power))
    def getSpeed(self):
        return MotorDevice.motodata[self.port].Speed
    def getTacho(self):
        return MotorDevice.motodata[self.port].TachoCounts
    @staticmethod
    def close():
        MotorDevice.motormm.close()
        os.close(MotorDevice.motorfile)
        os.close(MotorDevice.pwmfile)

    











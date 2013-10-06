import os
import time
from mmap import *
from . import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime
import struct
import array
devcon=lms2012.DEVCON()




UART_SET_CONN = 0xc00c7500;
UART_READ_MODE_INFO = 0xc03c7501;
UART_NACK_MODE_INFO = 0xc03c7502;
UART_CLEAR_CHANGED = 0xc03c7503;

INPUT_DEVICE_NUMBER=4;
OUTPUT_DEVICE_NUMBER=4;



class UARTDevice():
    isInitialized=False
    def __init__(self,port):
        self.port=port
        if not UARTDevice.isInitialized:
            UARTDevice.uartfile=os.open(lms2012.UART_DEVICE_NAME,os.O_RDWR)        
            UARTDevice.uartmm=mmap(fileno=UARTDevice.uartfile, length=sizeof(lms2012.UART),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
            UARTDevice.uart=lms2012.UART.from_buffer(UARTDevice.uartmm)
            UARTDevice.isInitialized=True

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
        if UARTDevice.isInitialized:
            UARTDevice.uartmm.close()
            os.close(UARTDevice.uartfile)
            UARTDevice.isInitialized=False


class AnalogDevice():
    isInitialized=False
    def __init__(self,port):
        self.port=port
        if not AnalogDevice.isInitialized:
            AnalogDevice.analogfile=os.open(lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)
            AnalogDevice.analogmm=mmap(fileno=AnalogDevice.analogfile, length=sizeof(lms2012.ANALOG),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
            AnalogDevice.analog=lms2012.ANALOG.from_buffer(AnalogDevice.analogmm)
            AnalogDevice.isInitialized=True
    def getPin6(self):
        return AnalogDevice.analog.InPin6[self.port]
    def getPin1(self):
        return AnalogDevice.analog.InPin1[self.port]
    @staticmethod
    def close():
        if AnalogDevice.isInitialized:
            AnalogDevice.analogmm.close()
            os.close(AnalogDevice.analogfile)
            AnalogDevice.isInitialized=False
        


class MotorDevice():
    isInitialized=False

    
    def __init__(self,port):
        self.port=port
        if not MotorDevice.isInitialized:
            MotorDevice.pwmfile=os.open(lms2012.PWM_DEVICE_NAME,os.O_RDWR)
            MotorDevice.motorfile=os.open(lms2012.MOTOR_DEVICE_NAME,os.O_RDWR)
            MOTORDATAArrray=lms2012.MOTORDATA * 4
            MotorDevice.motormm=mmap(fileno=MotorDevice.motorfile, length=sizeof(MOTORDATAArrray),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)    
            MotorDevice.motodata=MOTORDATAArrray.from_buffer(MotorDevice.motormm)
            MotorDevice.isInitialized=True

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
        if MotorDevice.isInitialized:
            MotorDevice.motormm.close()
            os.close(MotorDevice.motorfile)
            os.close(MotorDevice.pwmfile)
            MotorDevice.isInitialized=False



class UI():
    isInitialized=False
    @staticmethod
    def init():
        if not UI.isInitialized:
            UI.uifile=os.open(lms2012.UI_DEVICE_NAME,os.O_RDWR | os.O_SYNC)
            UI.uimm=mmap(fileno=UI.uifile, length=sizeof(lms2012.UI),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
            UI.ui=lms2012.UI.from_buffer(UI.uimm)
            UI.isInitialized=True
    @staticmethod
    def setLed(light):
        if not UI.isInitialized:
            init()
        os.write(UI.uifile,struct.pack('BB',ord('0')+light,0))
    @staticmethod
    def isPressed(key):
        if not UI.isInitialized:
            init()
        return UI.ui.Pressed[key]
    @staticmethod
    def close():
        if UI.isInitialized:
            UI.uimm.close()
            os.close(UI.uifile)
            UI.isInitialized=False



PixelTab=[
        chr(0x00), # 000 00000000
        chr(0xE0), # 001 11100000
        chr(0x1C), # 010 00011100
        chr(0xFC), # 011 11111100
        chr(0x03), # 100 00000011
        chr(0xE3), # 101 11100011
        chr(0x1F), # 110 00011111
        chr(0xFF)  # 111 11111111
        ]
class LCD():
    isInitialized=False
    MEM_WIDTH=60 #bytes
    SCREEN_WIDTH=178 #pix
    SCREEN_HEIGHT=128
    @staticmethod
    def init():
        if not LCD.isInitialized:
            LCD.lcdfile=os.open(lms2012.LCD_DEVICE_NAME,os.O_RDWR)
            LCD.lcdmm=mmap(fileno=LCD.lcdfile, length=LCD.MEM_WIDTH * LCD.SCREEN_HEIGHT,flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0) 
            LCD.membuffer=array.array('c',['\0']*(LCD.MEM_WIDTH * LCD.SCREEN_HEIGHT))
            LCD.imgbuffer=array.array('B',[0]*((LCD.SCREEN_WIDTH+7)/8 * LCD.SCREEN_HEIGHT))
        LCD.isInitialized=True



    @staticmethod
    def drawImage(src, srcX, srcY, srcWidth, srcHegiht, destX, destY, width, height):
        """ drawImage(src, srcX, srcY, srcWidth, srcHegiht, destX, destY, width, height):

            srcX, destX and width must be multiples of 8
            
        """
        if width > srcWidth:
            width = srcWidth
        if destX+width>LCD.SCREEN_WIDTH:
            width = LCD.SCREEN_WIDTH - destX
        if height > srcHegiht:
            height = srcHegiht
        if destY+height > LCD.SCREEN_HEIGHT:
            height =  LCD.SCREEN_HEIGHT- destY

 
        srcStart=srcX/8
        
        destStart=destX/8
        
        for i in range(0,height):
            LCD.imgbuffer[destStart:destStart+width/8] = src[srcStart:srcStart+width/8]            
            srcStart+=srcWidth/8
            destStart+=(LCD.SCREEN_WIDTH+7)/8
        LCD.update()

    @staticmethod
    def black():
        LCD.membuffer=array.array('c',[chr(0xff)]*(LCD.MEM_WIDTH * LCD.SCREEN_HEIGHT))
        LCD.imgbuffer=array.array('B',[0xff]*((LCD.SCREEN_WIDTH+7)/8 * LCD.SCREEN_HEIGHT))
        LCD.update()

    @staticmethod
    def white():
        LCD.membuffer=array.array('c',[chr(0x00)]*(LCD.MEM_WIDTH * LCD.SCREEN_HEIGHT))
        LCD.imgbuffer=array.array('B',[0x00]*((LCD.SCREEN_WIDTH+7)/8 * LCD.SCREEN_HEIGHT))
        LCD.update()

    @staticmethod
    def update():
        destindex=0
        srcindex=0
        for y in range (0,LCD.SCREEN_HEIGHT):
            for x in range (0,7):
                pixels  = LCD.imgbuffer[srcindex]
                srcindex+=1
                pixels |=(LCD.imgbuffer[srcindex]<<8)
                srcindex+=1
                pixels |=(LCD.imgbuffer[srcindex] <<16)
                srcindex+=1
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
                pixels >>= 3;
                LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
                destindex+=1
            pixels  = LCD.imgbuffer[srcindex]
            srcindex+=1
            pixels |= (LCD.imgbuffer[srcindex] <<8)
            srcindex+=1
            LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            LCD.membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1

        LCD.lcdmm.seek(0)
        LCD.lcdmm.write(LCD.membuffer)
        LCD.lcdmm.flush()

        
    @staticmethod
    def close():
        if LCD.isInitialized:
            LCD.lcdmm.close()
            os.close(LCD.lcdfile)
            




    











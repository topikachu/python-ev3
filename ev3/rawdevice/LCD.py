import os
import time
from mmap import *
from . import lms2012
from fcntl import ioctl
from ctypes import sizeof
import datetime
import struct
import array




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


isInitialized=False
MEM_WIDTH=60 #bytes
SCREEN_WIDTH=178 #pix
SCREEN_HEIGHT=128
lcdfile=None
membuffer=None
imgbuffer=None

def init():
    global isInitialized
    if not isInitialized:
        global lcdfile
        lcdfile=os.open(lms2012.LCD_DEVICE_NAME,os.O_RDWR)
        global lcdmm
        lcdmm=mmap(fileno=lcdfile, length=MEM_WIDTH * SCREEN_HEIGHT,flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0) 
        global membuffer
        membuffer=array.array('c',['\0']*(MEM_WIDTH * SCREEN_HEIGHT))
        global imgbuffer
        imgbuffer=array.array('B',[0]*((SCREEN_WIDTH+7)/8 * SCREEN_HEIGHT))
    isInitialized=True




def drawImage(src, srcX, srcY, srcWidth, srcHegiht, destX, destY, width, height):
    """ drawImage(src, srcX, srcY, srcWidth, srcHegiht, destX, destY, width, height):

        srcX, destX and width must be multiples of 8
        
    """
    if width > srcWidth:
        width = srcWidth
    if destX+width>SCREEN_WIDTH:
        width = SCREEN_WIDTH - destX
    if height > srcHegiht:
        height = srcHegiht
    if destY+height > SCREEN_HEIGHT:
        height =  SCREEN_HEIGHT- destY


    srcStart=srcX/8
    
    destStart=destX/8
    
    for i in range(0,height):
        imgbuffer[destStart:destStart+width/8] = src[srcStart:srcStart+width/8]            
        srcStart+=srcWidth/8
        destStart+=(SCREEN_WIDTH+7)/8
    redraw()


def black():
    membuffer=array.array('c',[chr(0xff)]*(MEM_WIDTH * SCREEN_HEIGHT))
    imgbuffer=array.array('B',[0xff]*((SCREEN_WIDTH+7)/8 * SCREEN_HEIGHT))
    redraw()


def white():
    membuffer=array.array('c',[chr(0x00)]*(MEM_WIDTH * SCREEN_HEIGHT))
    imgbuffer=array.array('B',[0x00]*((SCREEN_WIDTH+7)/8 * SCREEN_HEIGHT))
    redraw()


def redraw():
    destindex=0
    srcindex=0
    for y in range (0,SCREEN_HEIGHT):
        for x in range (0,7):
            pixels  = imgbuffer[srcindex]
            srcindex+=1
            pixels |=(imgbuffer[srcindex]<<8)
            srcindex+=1
            pixels |=(imgbuffer[srcindex] <<16)
            srcindex+=1
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
            pixels >>= 3;
            membuffer[destindex]=PixelTab[pixels & 0x07]
            destindex+=1
        pixels  = imgbuffer[srcindex]
        srcindex+=1
        pixels |= (imgbuffer[srcindex] <<8)
        srcindex+=1
        membuffer[destindex]=PixelTab[pixels & 0x07]
        destindex+=1
        pixels >>= 3;
        membuffer[destindex]=PixelTab[pixels & 0x07]
        destindex+=1
        pixels >>= 3;
        membuffer[destindex]=PixelTab[pixels & 0x07]
        destindex+=1
        pixels >>= 3;
        membuffer[destindex]=PixelTab[pixels & 0x07]
        destindex+=1

    lcdmm.seek(0)
    lcdmm.write(membuffer)
    lcdmm.flush()

    

def close():
    global isInitialized
    if isInitialized:
        lcdmm.close()
        os.close(lcdfile)
        isInitialized=False
        




    











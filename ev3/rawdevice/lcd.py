import os
import array
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
from . import lms2012

PIXEL_TAB = [
    chr(0x00),  # 000 00000000
    chr(0xE0),  # 001 11100000
    chr(0x1C),  # 010 00011100
    chr(0xFC),  # 011 11111100
    chr(0x03),  # 100 00000011
    chr(0xE3),  # 101 11100011
    chr(0x1F),  # 110 00011111
    chr(0xFF)  # 111 11111111
]
_initialized = False
MEM_WIDTH = 60  # bytes
SCREEN_WIDTH = 178  # pix
SCREEN_HEIGHT = 128
_lcdfile = None
_membuffer = array.array('c', ['\0'] * (MEM_WIDTH * SCREEN_HEIGHT))
_imgbuffer = array.array('B', [0] * ((SCREEN_WIDTH + 7) / 8 * SCREEN_HEIGHT))


def open_device():
    global _initialized
    if not _initialized:
        global _lcdfile
        _lcdfile = os.open(lms2012.LCD_DEVICE_NAME, os.O_RDWR)
        global lcdmm
        lcdmm = mmap(fileno=_lcdfile, length=MEM_WIDTH * SCREEN_HEIGHT,
                     flags=MAP_SHARED, prot=PROT_READ | PROT_WRITE, offset=0)
    _initialized = True


def draw_image(src, srcX, srcY, srcWidth, srcHegiht, destX, destY, width, height):
    """ draw_image(src, srcX, srcY, srcWidth, srcHegiht, destX, destY, width, height):

        srcX, destX and width must be multiples of 8
        
    """
    if width > srcWidth:
        width = srcWidth
    if destX + width > SCREEN_WIDTH:
        width = SCREEN_WIDTH - destX
    if height > srcHegiht:
        height = srcHegiht
    if destY + height > SCREEN_HEIGHT:
        height = SCREEN_HEIGHT - destY

    srcStart = srcX / 8

    destStart = destX / 8
    i = 0
    while i < height:
        _imgbuffer[destStart:destStart + width /
                   8] = src[srcStart:srcStart + width / 8]
        srcStart += srcWidth / 8
        destStart += (SCREEN_WIDTH + 7) / 8
        i += 1
    redraw()


def black():
    _membuffer = array.array('c', [chr(0xff)] * (MEM_WIDTH * SCREEN_HEIGHT))
    _imgbuffer = array.array(
        'B', [0xff] * ((SCREEN_WIDTH + 7) / 8 * SCREEN_HEIGHT))
    redraw()


def white():
    _membuffer = array.array('c', [chr(0x00)] * (MEM_WIDTH * SCREEN_HEIGHT))
    _imgbuffer = array.array(
        'B', [0x00] * ((SCREEN_WIDTH + 7) / 8 * SCREEN_HEIGHT))
    redraw()


def redraw():
    destindex = 0
    srcindex = 0
    y = 0
    while y < SCREEN_HEIGHT:
        x = 0
        while x < 7:
            pixels = _imgbuffer[srcindex]
            srcindex += 1
            pixels |= (_imgbuffer[srcindex] << 8)
            srcindex += 1
            pixels |= (_imgbuffer[srcindex] << 16)
            srcindex += 1
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            pixels >>= 3
            _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
            destindex += 1
            x += 1
        pixels = _imgbuffer[srcindex]
        srcindex += 1
        pixels |= (_imgbuffer[srcindex] << 8)
        srcindex += 1
        _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
        destindex += 1
        pixels >>= 3
        _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
        destindex += 1
        pixels >>= 3
        _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
        destindex += 1
        pixels >>= 3
        _membuffer[destindex] = PIXEL_TAB[pixels & 0x07]
        destindex += 1
        y += 1

    lcdmm.seek(0)
    lcdmm.write(_membuffer)
    lcdmm.flush()


def close_device():
    global _initialized
    if _initialized:
        lcdmm.close()
        os.close(_lcdfile)
        _initialized = False

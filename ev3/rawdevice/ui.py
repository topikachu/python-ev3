from ctypes import sizeof
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os
import struct

from . import lms2012


_initialized=False
_uifile=None
_uimm=None
_ui=None

def open_device():
    global _initialized
    if not _initialized:
        global _uifile
        _uifile=os.open(lms2012.UI_DEVICE_NAME,os.O_RDWR | os.O_SYNC)
        global _uimm
        _uimm=mmap(fileno=_uifile, length=sizeof(lms2012.UI),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
        global _ui
        _ui=lms2012.UI.from_buffer(_uimm)
        _initialized=True

def set_led(light):
    os.write(_uifile,struct.pack('BB',ord('0')+light,0))

def is_pressed(key):
    return _ui.Pressed[key]

def close_device():
    global _initialized
    if _initialized:
        _uimm.close()
        os.close(_uifile)
        _initialized=False







    











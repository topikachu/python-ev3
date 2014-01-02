import os
from . import lms2012

_initialized = False
_dcmfile = None


def open_device():
    global _initialized
    if not _initialized:
        global _dcmfile
        _dcmfile = os.open(lms2012.DCM_DEVICE_NAME, os.O_RDWR)
        _initialized = True


def set_pin_mode(port, pin):
    buf = bytearray('-' * 4)
    buf[port] = pin
    os.write(_dcmfile, buf)


def close_device():
    global _initialized
    if _initialized:
        os.close(_dcmfile)
        _initialized = False

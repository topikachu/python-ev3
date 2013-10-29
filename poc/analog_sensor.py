from ctypes import *
import datetime
from mmap import *
import os
import struct
import time

import ev3
from ev3.rawdevice.lms2012 import ANALOG


analogfile=os.open(ev3.rawdevice.lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)

mm=mmap(fileno=analogfile, length=sizeof(ANALOG),flags=MAP_PRIVATE,prot=PROT_READ | PROT_WRITE, offset=0)
analog=ANALOG.from_buffer(mm)
timeout=datetime.datetime.now()+datetime.timedelta(seconds=10)
while (datetime.datetime.now()<timeout):
    print analog.InPin6[0]
    time.sleep(1)
os.close(analogfile)
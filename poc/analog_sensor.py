from ctypes import sizeof
import datetime
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os
import time

import ev3
from ev3.rawdevice.lms2012 import ANALOG


analogfile=os.open(ev3.rawdevice.lms2012.ANALOG_DEVICE_NAME,os.O_RDWR)

mm=mmap(fileno=analogfile, length=sizeof(ANALOG),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)
_analog=ANALOG.from_buffer(mm)
timeout=datetime.datetime.now()+datetime.timedelta(seconds=10)
while (datetime.datetime.now()<timeout):
    print _analog.InPin6[0]
    time.sleep(1)
os.close(analogfile)
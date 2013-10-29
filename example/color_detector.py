from __future__ import print_function

import time

from ev3 import brick
from ev3.lego import EV3ColorSensor


brick.open()
colorSensor = EV3ColorSensor(3)
colorSensor.setColorMode()
brick.registerEvent(lambda: colorSensor.getValue()==7,lambda:print("hello"))
brick.start()
while True:
    time.sleep(0)



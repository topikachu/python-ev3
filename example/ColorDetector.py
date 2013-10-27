from __future__ import print_function
from ev3 import Brick
from ev3.lego import EV3ColorSensor
import time
Brick.init()
colorSensor = EV3ColorSensor(3)
colorSensor.setColorMode()
Brick.registerEvent(lambda: colorSensor.getValue()==7,lambda:print("hello"))
Brick.start()
while True:
    time.sleep(0)



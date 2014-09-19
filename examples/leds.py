"""
Cycles through the LED combinations.

HARDWARE:
    Brick-face LEDs.
"""
#XXX: This doesn't work yet. Why?
from time import sleep
from ev3.ev3dev import LED

lights = LED()
lights.left.on()
sleep(0.5)
lights.right.on()
sleep(0.5)
lights.left.off()
sleep(0.5)
lights.right.off()
sleep(0.5)

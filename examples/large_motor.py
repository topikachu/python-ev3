"""
Runs an attached Large Motor for 5 seconds.

HARDWARE:
    Large Motor plugged into any motor port.
"""
import time
from ev3.lego import LargeMotor
d = LargeMotor()
d.reset()
d.run_forever(50, regulation_mode=False)
time.sleep(5)
d.stop()

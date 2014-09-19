"""
Runs an attached Medium Motor for 5 seconds.

This is the example used on the site README.

HARDWARE:
    Medium Motor plugged into any motor port.
"""
import time
from ev3.lego import MediumMotor
d = MediumMotor()
d.reset()
d.run_forever(50, regulation_mode=False)
time.sleep(5)
d.stop()

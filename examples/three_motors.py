"""
Runs an attached Medium and Large Motors for 5 seconds.

HARDWARE:
    Medium Motor plugged into port A.
    Large Motors plugged into ports B and C.
"""
import time
from ev3.lego import LargeMotor, MediumMotor

# Initialize the motors.
a = MediumMotor(port='a')
a.reset()
b = LargeMotor(port='b')
b.reset()
c = LargeMotor(port='c')
c.reset()

# Start them all.
a.run_forever(50, regulation_mode=False)
b.run_forever(50, regulation_mode=False)
c.run_forever(50, regulation_mode=False)

time.sleep(5)

# Stop them all.
a.stop()
b.stop()
c.stop()

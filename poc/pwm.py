import os
import struct
import time


pwmfile=os.open("/dev/lms_pwm",os.O_RDWR)
os.write(pwmfile, struct.pack('BB',0xa6,1<<0))
os.write(pwmfile, struct.pack('BBB',0xa4,1<<0,50))
time.sleep(5)
os.write(pwmfile, struct.pack('BBB',0xa3,1<<0,0))
os.close(pwmfile)

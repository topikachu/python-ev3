from ev3.ev3dev import Motor
import unittest
import time
from util import get_input

class TestMotor(unittest.TestCase):
    get_input('Attach a motor on port A then continue')
    def __init__(self,*args, **kwargs):
        super(TestMotor, self).__init__(*args, **kwargs)        
        self.d=Motor(port=Motor.PORT.A)

    def setUp(self):
        self.d.reset()

    def test_run(self):
        self.d.run_mode = 'forever'
        self.d.regulation_mode = True
        self.d.pulses_per_second_sp = 200
        self.d.start()
        time.sleep(5)
        self.d.stop()

    def test_run_forever(self):
        self.d.run_forever(50, regulation_mode=False)
        time.sleep(5)
        self.d.stop()
        self.d.run_forever(200, regulation_mode=True)
        time.sleep(5)
        self.d.stop()

    def test_run_time_limited(self):
        self.d.run_time_limited(time_sp=10000, speed_sp=80, regulation_mode=False,
                           stop_mode=Motor.STOP_MODE.COAST, ramp_up_sp=1000, ramp_down_sp=1000)
        time.sleep(12)
    def test_run_position_limited(self):
        self.d.position=0
        self.d.run_position_limited(position_sp=360, speed_sp=800,
                           stop_mode=Motor.STOP_MODE.BRAKE , ramp_up_sp=1000, ramp_down_sp=1000)
        time.sleep(5)

    def test_run_position_limited_relative (self):        
        self.d.position_mode=Motor.POSITION_MODE.RELATIVE
        self.d.run_position_limited(position_sp=160, speed_sp=800,
                           stop_mode=Motor.STOP_MODE.BRAKE , ramp_up_sp=1000, ramp_down_sp=1000)
        time.sleep(5) 

if __name__ == '__main__':
    unittest.main()

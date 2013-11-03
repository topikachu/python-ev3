import time
import unittest
from ev3.rawdevice.lms2012 import TYPE_TACHO, TYPE_NONE
from ev3.rawdevice import motordevice

PORTS=0X06 # (0X02+0X06 ) B,C

class TestMotorDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        motordevice.open_device()
        #motordevice.set_types([TYPE_NONE, TYPE_TACHO,TYPE_TACHO ,TYPE_NONE ])
    def setUp(self):
        motordevice.reset(PORTS)
        
        
        
    def test_motor(self):
        # make sure the shuffled sequence does not lose any elements
        #motordevice.polarity(PORTS,1) 
        motordevice.power(PORTS,50)
        
        i=0
        while i<10:
            print "moter B step %d ,speed %d" %  (motordevice.get_steps(1),motordevice.get_speed(1))
            print "moter C step %d ,speed %d" %  (motordevice.get_steps(2),motordevice.get_speed(2))
            time.sleep(1)
            i+=3
        motordevice.stop(PORTS,brake=1)
#     def test_step_power(self):        
#         motordevice.step_power(PORTS, 50, 3, 10, 5, 1)
#         time.sleep(5)
        
    def test_time_power(self):
        motordevice.time_power(PORTS, 50, 2000,5000 , 2000, 1)
    def test_time_sync(self):
        motordevice.time_sync(PORTS, 50, 50, 5000, 1)
        motordevice.start(PORTS)
    def tearDown(self):
        motordevice.stop(PORTS,brake=1)
    @classmethod   
    def tearDownClass(cls):
        
        motordevice.close_device()


if __name__ == '__main__':
    unittest.main()
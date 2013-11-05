from __future__ import print_function
import unittest
from ev3.rawdevice.lms2012 import TYPE_TACHO, TYPE_NONE
from ev3.rawdevice import motordevice
from test import test_util

PORTS=0X06 # (0X02+0X06 ) B,C

def print_motor_info():
    print("moter B count %d, speed %d\nmoter C count %d, speed %d" % \
                                               (motordevice.get_sensor(1),motordevice.get_speed(1),\
                                                motordevice.get_sensor(2),motordevice.get_speed(2)))

class TestMotorDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        motordevice.open_device()
        motordevice.set_types([TYPE_NONE, TYPE_TACHO,TYPE_TACHO ,TYPE_NONE ])
        
    def setUp(self):
        print ("In method", self._testMethodName)
        motordevice.reset(PORTS)        
        
          
    def test_power(self):
        motordevice.power(PORTS,20)
        test_util.wait(5, print_motor_info )
        
    def test_speed(self):
        motordevice.speed(PORTS,20)        
        test_util.wait(5, print_motor_info )
        
     

    def test_step_power(self):        
        motordevice.step_power(PORTS, 20, 180, 720, 180, 1)        
        test_util.wait(6, print_motor_info)
         
    def test_time_power(self):        
        motordevice.time_power(PORTS, 20, 2000,5000 , 2000, 1)
        test_util.wait(6, print_motor_info)
        
    def test_step_speed(self):
        motordevice.step_speed(PORTS, 20, 180, 720, 180, 1)
        test_util.wait(10, print_motor_info)
        
    def test_time_speed(self):
        motordevice.time_speed(PORTS, 20, 2000,5000 , 2000, 1)
        test_util.wait(10, print_motor_info)
    
    
    def test_step_sync(self):
        motordevice.step_sync(PORTS, 20, 50, 1000, 1)        
        test_util.wait(10, print_motor_info)   
        
        
        
    def test_time_sync(self):
        motordevice.time_sync(PORTS, 20, 50, 5000, 1)
        
        test_util.wait(5, print_motor_info)
        
    def tearDown(self):
        motordevice.stop(PORTS,brake=1)
        pass
    @classmethod   
    def tearDownClass(cls):
        
        motordevice.close_device()


if __name__ == '__main__':
    unittest.main()
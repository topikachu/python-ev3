from __future__ import print_function
import unittest
from test import test_util
from ev3 import ev3
from ev3.rawdevice import motordevice
from ev3.rawdevice.lms2012 import TYPE_TACHO, TYPE_NONE
def setUpModule():
    ev3.open_all_device()
    
def tearDownModule():
    ev3.close_all_device()
class TestEv3Motor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    
    def test_motor(self):
        motordevice.set_types([TYPE_NONE, TYPE_TACHO,TYPE_TACHO ,TYPE_NONE ])
        motordevice.step_speed(ev3.MOTOR_C_BIT, 20, 10, 10, 10)
         
        test_util.wait(5, lambda:print("moter B sensor %d, speed %d, count %d\nmoter C sensor %d, speed %d count %d" % \
                                               (motordevice.get_sensor(1),motordevice.get_speed(1),motordevice.get_tacho(1), \
                                                motordevice.get_sensor(2),motordevice.get_speed(2),motordevice.get_tacho(2))))
        motordevice.stop(ev3.MOTOR_C_BIT, 1)
        motordevice.reset(ev3.MOTOR_B_BIT|ev3.MOTOR_C_BIT)
        motordevice.clear_steps(ev3.MOTOR_B_BIT|ev3.MOTOR_C_BIT)
        
        print("moter B sensor %d, speed %d, count %d\nmoter C sensor %d, speed %d count %d" % \
                                               (motordevice.get_sensor(1),motordevice.get_speed(1),motordevice.get_tacho(1), \
                                                motordevice.get_sensor(2),motordevice.get_speed(2),motordevice.get_tacho(2)))
        print (bytearray(motordevice._motormm.read(motordevice._motormm.size())))
#         #motordevice.step_speed(ev3.MOTOR_C_BIT, 20, 10, 10, 10)
#         test_util.wait(5, lambda:print("moter B sensor %d, speed %d, count %d\nmoter C sensor %d, speed %d count %d" % \
#                                                (motordevice.get_sensor(1),motordevice.get_speed(1),motordevice.get_tacho(1), \
#                                                 motordevice.get_sensor(2),motordevice.get_speed(2),motordevice.get_tacho(2))))
       

        
    @classmethod
    def tearDownClass(cls):
        pass
        


if __name__ == '__main__':
    unittest.main()
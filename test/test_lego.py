from __future__ import print_function
import unittest

from ev3 import ev3
from test import test_util
def setUpModule():
    ev3.open_all_device()
    
def tearDownModule():
    ev3.close_all_device()
class TestEv3Sensors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    def setUp(self):
        print ("In method", self._testMethodName)
        
    def test_ev3_color_sensor(self):
        from ev3.lego import EV3ColorSensor

        colorSensor = EV3ColorSensor(ev3.SENSOR_3)
        print( "start reflect mode")
        colorSensor.set_reflect_mode()
        test_util.count_down(10, lambda:print( colorSensor.get_value()))
        
        print ("start ambient mode")
        colorSensor.set_ambient_mode()
        test_util.count_down(10, lambda:print( colorSensor.get_value()))
        
        print( "start color mode")
        colorSensor.set_color_mode()        
        test_util.count_down(10, lambda:print( colorSensor.color_to_string()))
            

        colorSensor.reset()
    
    def test_ev3_ir_sensor(self):
        from ev3.lego import EV3IRSensor
        irSensor=EV3IRSensor(ev3.SENSOR_4)
        print("IR prox mode")
        irSensor.set_prox_mode()
        test_util.count_down(10, lambda:print(irSensor.get_distance()))
        irSensor.set_seek_mode()
        print("IR seek mode. open beacon!!")        
        test_util.count_down(10, lambda:print(irSensor.get_direction_and_distance(EV3IRSensor.CHANNEL_1)))
        print("IR remote mode. press beacon buttone!!")        
        irSensor.set_remote_mode()
        test_util.count_down(10, lambda:print(irSensor.get_remote_command(EV3IRSensor.CHANNEL_1)))        
        irSensor.reset()
    
    def test_ev3_touch_sensor(self):
        from ev3.lego import EV3TouchSensor
        touchSensor = EV3TouchSensor(ev3.SENSOR_2)
        test_util.count_down(10, lambda:print(touchSensor.is_pressed()))
    
    @classmethod
    def tearDownClass(cls):
        pass
        


if __name__ == '__main__':
    unittest.main()
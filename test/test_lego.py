import time
import unittest

from ev3 import ev3

def setUpModule():
    ev3.open_all_device()
    
def tearDownModule():
    ev3.close_all_device()
class TestAnalogDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    
    def test_ev3_color_sensor(self):
        from ev3.lego import EV3ColorSensor

        colorSensor = EV3ColorSensor(2)
        colorSensor.set_color_mode()
        print "start color test"
        i=0
        while (i<10):
            print colorSensor.color_to_string()
            time.sleep(1)
            i+=1

        colorSensor.reset()
    def tearDownClass(self):
        pass
        


if __name__ == '__main__':
    unittest.main()
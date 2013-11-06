import time
import unittest

from ev3 import robot

def setUpModule():
    robot.open_all_devices()
    
def tearDownModule():
    robot.close_all_devices()
class TestBattery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    
    def test_battery(self):
        print robot.get_battery();
        

        
    @classmethod
    def tearDownClass(cls):
        pass
        


if __name__ == '__main__':
    unittest.main()
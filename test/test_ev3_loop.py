import time
import unittest

from ev3 import robot
import ev3.lego
def setUpModule():
    robot.open_all_devices()
    
def tearDownModule():
    robot.close_all_devices()
class TestEv3Loop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    
    def test_loop(self):
        robot.open_all_devices()
        
        print robot.get_battery();
        

        
    @classmethod
    def tearDownClass(cls):
        pass
        


if __name__ == '__main__':
    unittest.main()
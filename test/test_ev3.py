import time
import unittest

from ev3 import ev3

def setUpModule():
    ev3.open_all_device()
    
def tearDownModule():
    ev3.close_all_device()
class TestBattery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        

    
    def test_battery(self):
        print ev3.get_battery();
        

        
    @classmethod
    def tearDownClass(cls):
        pass
        


if __name__ == '__main__':
    unittest.main()
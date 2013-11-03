import time
import unittest

from ev3.rawdevice import analogdevice


class TestEv3Sensors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        analogdevice.open_device()

    
    def test_getValue(self):
        
        for i in range(0,4):
            print analogdevice.get_connection_type(i)            
            time.sleep(1)
    @classmethod
    def tearDownClass(cls):
        analogdevice.close_device()


if __name__ == '__main__':
    unittest.main()
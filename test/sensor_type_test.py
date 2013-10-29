import time
import unittest

from ev3.rawdevice import analogdevice


class TestAnalogDevice(unittest.TestCase):

    def setUp(self):
        analogdevice.open_device()

    
    def test_getValue(self):
        
        for i in range(0,4):
            print analogdevice.get_connection_type(i)            
            time.sleep(1)

    def tearDown(self):
        analogdevice.close_device()


if __name__ == '__main__':
    unittest.main()
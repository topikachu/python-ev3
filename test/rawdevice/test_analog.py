import time
import unittest

from ev3.rawdevice import analogdevice


class TestEv3Sensors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        analogdevice.open_device()

    
    def test_getValue(self):
        print "Touch Sensor test. Press the button"
        i=0
        while i<10:
            print analogdevice.get_pin6(1)            
            time.sleep(1)
            i+=1
    @classmethod
    def tearDownClass(cls):
        analogdevice.close_device()


if __name__ == '__main__':
    unittest.main()
import time
import unittest

from ev3.rawdevice import analogdevice


class TestAnalogDevice(unittest.TestCase):

    def setUp(self):
        analogdevice.open()

    
    def test_getValue(self):
        print "Touch Sensor test. Press the button"
        for i in range(0,10):
            print analogdevice.get_pin6(0)            
            time.sleep(1)

    def tearDown(self):
        analogdevice.close()


if __name__ == '__main__':
    unittest.main()
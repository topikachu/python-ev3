from ev3.rawdevice import AnalogDevice
import unittest
import time
class TestAnalogDevice(unittest.TestCase):

    def setUp(self):
        AnalogDevice.init()

    
    def test_getValue(self):
        print "Touch Sensor test. Press the button"
        for i in range(0,10):
            print AnalogDevice.getPin6(0)            
            time.sleep(1)

    def tearDown(self):
        AnalogDevice.close()


if __name__ == '__main__':
    unittest.main()
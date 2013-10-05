from ev3.cdriver.rawdevice import AnalogDevice
import unittest
import time
class TestAnalogDevice(unittest.TestCase):

    def setUp(self):
        self.analogDevice = AnalogDevice(0)

    
    def test_getValue(self):
        for i in range(0,10):
            print self.analogDevice.getPin6()            
            time.sleep(1)

    def tearDown(self):
        self.analogDevice.close()


if __name__ == '__main__':
    unittest.main()
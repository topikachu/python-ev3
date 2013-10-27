from ev3.rawdevice import AnalogDevice
import unittest
import time
class TestAnalogDevice(unittest.TestCase):

    def setUp(self):
        AnalogDevice.init()

    
    def test_getValue(self):
        
        for i in range(0,4):
            print AnalogDevice.getConnectionType(i)            
            time.sleep(1)

    def tearDown(self):
        AnalogDevice.close()


if __name__ == '__main__':
    unittest.main()
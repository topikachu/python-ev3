from ev3.rawdevice import UARTDevice
import unittest
import time
class TestUARTDevice(unittest.TestCase):

    def setUp(self):
        UARTDevice.init()

    def test_setMode(self):
        
        UARTDevice.setMode(2,0)
        time.sleep(1)
        UARTDevice.setMode(2,1)
        time.sleep(1)
        UARTDevice.setMode(2,2)
        deviceType = UARTDevice.getModeInfo(2,0)
        print deviceType.Name
        print deviceType.Type
        print "Color Sensor test!"
        for i in range(0,10):
            print UARTDevice.getValueByte(2)
            time.sleep(1)

        UARTDevice.reset(2)

    def tearDown(self):
        UARTDevice.close()

    

if __name__ == '__main__':
    unittest.main()
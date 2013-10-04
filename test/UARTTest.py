from ev3.cdriver.rawdevice import UARTDevice
import unittest
import time
class TestUARTDevice(unittest.TestCase):

    def setUp(self):
        self.UARTDevice = UARTDevice(2)

    def test_setMode(self):
        # make sure the shuffled sequence does not lose any elements
        self.UARTDevice.setMode(0)
        self.UARTDevice.setMode(1)
        self.UARTDevice.setMode(2)

    def test_getValueByte(self):
        for i in range(0,10):
            print self.UARTDevice.getValueByte()
            time.sleep(1)

    

if __name__ == '__main__':
    unittest.main()
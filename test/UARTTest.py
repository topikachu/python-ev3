from ev3.rawdevice import UARTDevice
import unittest
import time
class TestUARTDevice(unittest.TestCase):

    def setUp(self):
        self.uartDevice = UARTDevice(2)

    def test_setMode(self):
        # make sure the shuffled sequence does not lose any elements
        self.uartDevice.setMode(0)
        time.sleep(1)
        self.uartDevice.setMode(1)
        time.sleep(1)
        self.uartDevice.setMode(2)
        for i in range(0,10):
            print self.uartDevice.getValueByte()
            time.sleep(1)
        self.uartDevice.reset()

    def tearDown(self):
        self.uartDevice.close()

    

if __name__ == '__main__':
    unittest.main()
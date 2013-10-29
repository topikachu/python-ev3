import time
import unittest

from ev3.rawdevice import uartdevice


class TestUARTDevice(unittest.TestCase):

    def setUp(self):
        uartdevice.open()

    def test_setMode(self):
        
        uartdevice.set_mode(2,0)
        time.sleep(1)
        uartdevice.set_mode(2,1)
        time.sleep(1)
        uartdevice.set_mode(2,2)
        deviceType = uartdevice.get_mode_info(2,0)
        print deviceType.Name
        print deviceType.Type
        print "Color Sensor test!"
        for i in range(0,10):
            print uartdevice.get_value_byte(2)
            time.sleep(1)

        uartdevice.reset(2)

    def tearDown(self):
        uartdevice.close()

    

if __name__ == '__main__':
    unittest.main()
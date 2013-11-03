from __future__ import print_function
import unittest
from test import test_util
from ev3.rawdevice import uartdevice


class TestUARTDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        uartdevice.open_device()

    def test_setMode(self):
        
        uartdevice.set_mode(2,0)
        test_util.count_down(5)
        uartdevice.set_mode(2,1)
        test_util.count_down(5)
        print( "Color Sensor test!")
        uartdevice.set_mode(2,2)
        test_util.count_down(10,lambda : print(uartdevice.get_value_byte(2)))
        
        
        
    @classmethod
    def tearDownClass(cls):
        uartdevice.reset(2)
        uartdevice.close_device()

    

if __name__ == '__main__':
    unittest.main()
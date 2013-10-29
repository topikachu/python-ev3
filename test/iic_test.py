import time
import unittest

from ev3.rawdevice import dcm, iicdevice


class TestUARTDevice(unittest.TestCase):

    def setUp(self):
        dcm.open()
        iicdevice.open()

    def test_setMode(self):
        iicdevice.reset(0)
        dcm.set_pin_mode(0,ord('F'));
        
        #iicdevice.i2c_transaction(0,0x02,buf,0)
        
        
        value = iicdevice.i2c_transaction(0,0x02,bytearray([0x00]),8)
        print bytearray(value).decode()
        value = iicdevice.i2c_transaction(0,0x02,bytearray([0x08]),8)
        print bytearray(value).decode()
        value = iicdevice.i2c_transaction(0,0x02,bytearray([0x10]),8)
        print bytearray(value).decode()
        buf=bytearray([0x41,ord('I')])
        iicdevice.i2c_transaction(0,0x02,buf,0)
        for i in range(0,100):
            value = iicdevice.i2c_transaction(0,0x02,bytearray([0x42]),1)
            time.sleep(0)
            print value[0]
        

    def tearDown(self):
        iicdevice.close()
        dcm.close()

    

if __name__ == '__main__':
    unittest.main()
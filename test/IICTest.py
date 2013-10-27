from ev3.rawdevice import IICDevice
from ev3.rawdevice import Dcm
import unittest
import time
class TestUARTDevice(unittest.TestCase):

    def setUp(self):
        Dcm.init()
        IICDevice.init()

    def test_setMode(self):
        IICDevice.reset(0)
        Dcm.setPinMode(0,ord('0'));
        buf=bytearray([0x41,ord('I')])
        #IICDevice.i2cTransaction(0,0x02,buf,0)
        
        buf=bytearray([0x10])
        value = IICDevice.i2cTransaction(0,0x02,buf,8)
        if value:
                for v in  value:
                    print chr(v)
        
        

    def tearDown(self):
        IICDevice.close()
        Dcm.close()

    

if __name__ == '__main__':
    unittest.main()
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
        Dcm.setPinMode(0,ord('F'));
        
        #IICDevice.i2cTransaction(0,0x02,buf,0)
        
        
        value = IICDevice.i2cTransaction(0,0x02,bytearray([0x00]),8)
        print bytearray(value).decode()
        value = IICDevice.i2cTransaction(0,0x02,bytearray([0x08]),8)
        print bytearray(value).decode()
        value = IICDevice.i2cTransaction(0,0x02,bytearray([0x10]),8)
        print bytearray(value).decode()
        buf=bytearray([0x41,ord('I')])
        IICDevice.i2cTransaction(0,0x02,buf,0)
        for i in range(0,100):
            value = IICDevice.i2cTransaction(0,0x02,bytearray([0x42]),1)
            time.sleep(0)
            print value[0]
        

    def tearDown(self):
        IICDevice.close()
        Dcm.close()

    

if __name__ == '__main__':
    unittest.main()
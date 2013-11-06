import time
import unittest

from ev3.rawdevice import dcm, iicdevice


class TestIICDevice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dcm.open_device()
        iicdevice.open_device()

    def test_setMode(self):
        iicdevice.reset(0)
        #dcm.set_pin_mode(0,ord('F'));
        
        #iicdevice.i2c_transaction(0,0x02,buf,0)
        
        
        value = iicdevice.i2c_transaction(0,0x02,bytearray([0x00]),8)
        print bytearray(value).decode()
        value = iicdevice.i2c_transaction(0,0x02,bytearray([0x08]),8)
        print bytearray(value).decode()
        value = iicdevice.i2c_transaction(0,0x02,bytearray([0x10]),8)
        print bytearray(value).decode()
        buf=bytearray([0x41,ord('I')])
        iicdevice.i2c_transaction(0,0x02,buf,0)
        print "test iic psp control. press button!"
        round=0
        while round<5:
            print "round %d" % round
            time.sleep(3)
            round+=1
            i=0        
            while i<30:
                value = iicdevice.i2c_transaction(0,0x02,bytearray([0x42]),1)
                time.sleep(0)
                print hex(value[0] & 0xff)
                i+=1
        
    @classmethod
    def tearDownClass(cls):
        iicdevice.close_device()
        dcm.close_device()

    

if __name__ == '__main__':
    unittest.main()
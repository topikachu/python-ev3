from ev3.ev3dev import  I2CS
import unittest



class TestI2CS(unittest.TestCase):

    def test_i2cs(self):
    	raw_input('Attach an I2CS sensor on port 3 then continue')
        d = I2CS(port=3,addr=0x01)
        print(d.read_byte())
        print(d.read_byte_data(0x00))
if __name__ == '__main__':
    unittest.main()

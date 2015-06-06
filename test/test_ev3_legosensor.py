from ev3.ev3dev import  LegoSensor
import unittest
from util import get_input
import glob

class TestLegoSensor(unittest.TestCase):

    def test_LegoSensor(self):
        get_input('Attach a Lego on port 1 then continue')
        d = LegoSensor(port=1)
        print(d.mode)
        print(d.port)
        if (len(glob.glob('/sys/class/lego-sensor/sensor*/name')) >0):
            name = d.name
            print(name)
            d = LegoSensor(name=name)
        print(d.mode)
        print(d.port)

if __name__ == '__main__':
    unittest.main()

from ev3.ev3dev import  Msensor
import unittest
from util import get_input
import glob

class TestMsensor(unittest.TestCase):

    def test_msensor(self):
        get_input('Attach a Msensor on port 1 then continue')
        d = Msensor(port=1)
        print(d.mode)
        print(d.port)
        if (len(glob.glob('/sys/class/msensor/sensor*/type_id')) >0):
            type_id = d.type_id
            print(type_id)
            d = Msensor(type_id=type_id)
        if (len(glob.glob('/sys/class/msensor/sensor*/name')) >0):
            name = d.name
            print(name)
            d = Msensor(name=name)
        print(d.mode)
        print(d.port)

if __name__ == '__main__':
    unittest.main()

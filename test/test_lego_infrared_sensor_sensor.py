from ev3.lego import InfraredSensor
import unittest
from util import get_input

class TestInfraredSensor(unittest.TestCase):
    def test_infrared_sensor(self):
        get_input('Attach a InfraredSensor then continue')
        d= InfraredSensor()
        print(d.mode)
        get_input('test proximity')
        print(d.prox)
        print(d.mode)
        get_input('test remote')
        print(d.remote)
        print(d.mode)
        get_input('test remote_bin')
        print(d.remote_bin)
        print(d.mode)
        get_input('test seek')
        print(d.seek)
        print(d.mode)


if __name__ == '__main__':
    unittest.main()    

from ev3.lego import InfraredSensor
import unittest


class TestColorSensor(unittest.TestCase):
    d= InfraredSensor()
    print(d.mode)
    raw_input('test proxy')
    print(d.prox)
    print(d.mode)
    raw_input('test remote')
    print(d.remote)
    print(d.mode)
    raw_input('test remote_bin')
    print(d.remote_bin)
    print(d.mode)
    raw_input('test seek')
    print(d.seek)
    print(d.mode)


if __name__ == '__main__':
    unittest.main()    
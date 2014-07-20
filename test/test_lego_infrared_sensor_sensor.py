from ev3.lego import InfraredSensor
import unittest


class TestInfraredSensor(unittest.TestCase):
    def test_infrared_sensor(self):
        raw_input('Attach a InfraredSensor then continue')
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
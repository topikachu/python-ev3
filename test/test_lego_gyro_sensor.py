from ev3.lego import GyroSensor
import unittest
from util import get_input

class TestGyroSensor(unittest.TestCase):
    def test_gyro_sensor(self):
        get_input('Attach a GyroSensor then continue')
        d = GyroSensor()
        get_input('test ang')
        print(d.ang)
        print(d.mode)
        get_input('test rate')
        print(d.rate)
        print(d.mode)
        get_input('test ang_and_rate')
        print(d.ang_and_rate)
        print(d.mode)


if __name__ == '__main__':
    unittest.main()

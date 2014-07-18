from ev3.lego import GyroSensor
import unittest


class TestColorSensor(unittest.TestCase):
    d = GyroSensor()
    raw_input('test ang')
    print(d.ang)
    print(d.mode)
    raw_input('test rate')
    print(d.rate)
    print(d.mode)
    raw_input('test ang_and_rate')
    print(d.ang_and_rate)
    print(d.mode)


if __name__ == '__main__':
    unittest.main()

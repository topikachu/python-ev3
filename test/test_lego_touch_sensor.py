from ev3.lego import TouchSensor
import unittest


class TestTouchSensor(unittest.TestCase):
    d = TouchSensor()
    raw_input('test pushed')
    print(d.is_pushed)
    print(d.mode)


if __name__ == '__main__':
    unittest.main()

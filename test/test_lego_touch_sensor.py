from ev3.lego import TouchSensor
import unittest


class TestTouchSensor(unittest.TestCase):
    def test_TouchSensor(self):
        d = TouchSensor()
        raw_input('test pushed')
        print(d.is_pushed)
        print(d.mode)


if __name__ == '__main__':
    unittest.main()

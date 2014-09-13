import ev3.ev3dev
import unittest
from util import get_input


class TestI2CS(unittest.TestCase):

    def test_battery(self):
        print(ev3.ev3dev.get_battery_percentage())
if __name__ == '__main__':
    unittest.main()

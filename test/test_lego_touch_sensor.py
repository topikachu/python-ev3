from ev3.lego import TouchSensor
import unittest
from util import get_input

class TestTouchSensor(unittest.TestCase):
    def test_touch_sensor(self):
        get_input('Attach a TouchSensor then continue')    	
        d = TouchSensor()
        get_input('test pushed')
        print(d.is_pushed)
        print(d.mode)


if __name__ == '__main__':
    unittest.main()

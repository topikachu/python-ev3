from ev3.lego import ColorSensor
import unittest
from util import get_input

class TestColorSensor(unittest.TestCase):
    def test_color_sensor(self):
        get_input('Attach a ColorSensor then continue')
        d = ColorSensor()
        get_input('test rgb')
        print(d.rgb)
        print(d.mode)
        get_input('test color')
        print(d.color)
        print(d.mode)
        get_input('test reflect')
        print(d.reflect)
        print(d.mode)
        get_input('test ambient')
        print(d.ambient)
        print(d.mode)


if __name__ == '__main__':
    unittest.main()

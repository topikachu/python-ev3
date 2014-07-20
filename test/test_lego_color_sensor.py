from ev3.lego import ColorSensor
import unittest


class TestColorSensor(unittest.TestCase):
    def test_color_sensor(self):
        raw_input('Attach a ColorSensor then continue')
        d = ColorSensor()
        raw_input('test rgb')
        print(d.rgb)
        print(d.mode)
        raw_input('test color')
        print(d.color)
        print(d.mode)
        raw_input('test reflect')
        print(d.reflect)
        print(d.mode)
        raw_input('test ambient')
        print(d.ambient)
        print(d.mode)


if __name__ == '__main__':
    unittest.main()

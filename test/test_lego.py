import time
import unittest

from ev3 import brick


class TestAnalogDevice(unittest.TestCase):

    def setUp(self):
        brick.open_all_device()

    
    def test_ev3_color_sensor(self):
        from ev3.lego import EV3ColorSensor

        colorSensor = EV3ColorSensor(2)
        colorSensor.set_color_mode()
        print "start color test"
        i=0
        while (i<10):
            print colorSensor.color_to_string()
            time.sleep(1)
            i+=1

        colorSensor.reset()
    def tearDown(self):
        brick.close_all_device()


if __name__ == '__main__':
    unittest.main()
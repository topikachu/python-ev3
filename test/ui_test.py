import time
import unittest

from ev3.rawdevice import lms2012, ui


class TestUIDevice(unittest.TestCase):

    def setUp(self):
        ui.open()

    
    def test_setLed(self):
        for i in range(1,10):
            ui.set_led(i)
            time.sleep(1)
        ui.set_led(0)

    def test_key(self):
        print "Button test. Press the 'up' key!"
        for i in range(0,10):
            print ui.is_pressed(0)
            time.sleep(1)

    def tearDown(self):
        ui.close()


if __name__ == '__main__':
    unittest.main()
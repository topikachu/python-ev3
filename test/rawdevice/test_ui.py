import time
import unittest

from ev3.rawdevice import ui


class TestUIDevice(unittest.TestCase):

    def setUp(self):
        ui.open_device()

    
    def test_setLed(self):
        i=0
        while i < 10:            
            ui.set_led(i)
            time.sleep(1)
            i+=1
        ui.set_led(0)

    def test_key(self):
        print "Button test. Press the 'up' key!"
        i=0
        while i<10:
            print ui.is_pressed(0)
            time.sleep(1)
            i+=1

    def tearDown(self):
        ui.close_device()


if __name__ == '__main__':
    unittest.main()
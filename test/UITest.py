from ev3.rawdevice import UI
from ev3.rawdevice import lms2012
import unittest
import time
class TestUIDevice(unittest.TestCase):

    def setUp(self):
        UI.init()

    
    def test_setLed(self):
        for i in range(1,10):
            UI.setLed(i)
            time.sleep(1)
        UI.setLed(0)

    def test_key(self):
        print "Button test. Press the 'up' key!"
        for i in range(0,10):
            print UI.isPressed(0)
            time.sleep(1)

    def tearDown(self):
        UI.close()


if __name__ == '__main__':
    unittest.main()
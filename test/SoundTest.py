# -*- coding: utf8
from ev3.rawdevice import Sound
import unittest
import time
import array


class TestSound(unittest.TestCase):

    def setUp(self):
        Sound.init()

    
    def test_lcd(self):
        Sound.playTone(697, 200)
        

    def tearDown(self):
        Sound.close()


if __name__ == '__main__':
    unittest.main()
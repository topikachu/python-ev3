# -*- coding: utf8

import unittest

from ev3.rawdevice import sound


class TestSound(unittest.TestCase):

    def setUp(self):
        sound.open_device()

    
    def test_lcd(self):
        sound.play_tone(697, 200)
        

    def tearDown(self):
        sound.close_device()


if __name__ == '__main__':
    unittest.main()
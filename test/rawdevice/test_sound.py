# -*- coding: utf8

import unittest

from ev3.rawdevice import sound


class TestSound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sound.open_device()

    
    def test_lcd(self):
        sound.play_tone(697, 200)
        
    @classmethod
    def tearDownClass(cls):
        sound.close_device()


if __name__ == '__main__':
    unittest.main()
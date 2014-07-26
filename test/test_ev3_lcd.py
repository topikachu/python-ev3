from ev3.ev3dev import Lcd
# -*- coding: utf-8 -*-
import unittest
from util import get_input
import time
from PIL import Image,ImageDraw,ImageFont
class TestLcd(unittest.TestCase):

    def test_lcd(self):
        get_input('Test lcd')
        d= Lcd()        
        d.draw.ellipse((20, 20, 60, 60))
        d.update()
        time.sleep(2)
        d.reset()
        font = ImageFont.load_default() 
        d.draw.text((10, 10), "hello", font=font)
        d.update()
        time.sleep(2)
        d.reset()
        font = ImageFont.truetype('/usr/share/fonts/truetype/arphic/uming.ttc',15)
        d.draw.text((20, 20), u'你好,世界', font=font)
        d.update()



        
if __name__ == '__main__':
    unittest.main()

from ev3.ev3dev import  Tone
import unittest
from util import get_input
import time

class TestTone(unittest.TestCase):

    def test_tone(self):
        get_input('Test beep')
        d= Tone()
        d.play(1000, 3000)
        time.sleep(3)
        d.play(1000)
        time.sleep(3)
        d.stop()
        
if __name__ == '__main__':
    unittest.main()

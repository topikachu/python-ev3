from ev3.ev3dev import Key
import unittest
from util import get_input
import time


class TestTone(unittest.TestCase):

    def test_tone(self):
        d = Key()
        get_input('Test keyboard. Hold Up key')
        print(d.up)
        get_input('Test keyboard. Release Up key')
        print(d.up)
        get_input('Test keyboard. Hold Down key')
        print(d.down)
        get_input('Test keyboard. Release Down key')
        print(d.down)
        get_input('Test keyboard. Hold Left key')
        print(d.left)
        get_input('Test keyboard. Release Left key')
        print(d.left)
        get_input('Test keyboard. Hold Right key')
        print(d.right)
        get_input('Test keyboard. Release Right key')
        print(d.right)
        get_input('Test keyboard. Hold Backspace key')
        print(d.backspace)
        get_input('Test keyboard. Release Backspace key')
        print(d.backspace)
        get_input('Test keyboard. Hold Enter key')
        print(d.enter)
        get_input('Test keyboard. Release Enter key')
        print(d.enter)

if __name__ == '__main__':
    unittest.main()

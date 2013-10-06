# -*- coding: utf8
from ev3.font import getFont
import unittest
import time
import array


class TestFont(unittest.TestCase):



    
    def test_getFont(self):
        print getFont('c')
        print getFont(u'如')
        



if __name__ == '__main__':
    unittest.main()
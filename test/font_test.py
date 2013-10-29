# -*- coding: utf8

import unittest

from ev3.font import get_font


class TestFont(unittest.TestCase):



    
    def test_getFont(self):
        print get_font('c')
        print get_font(u'如')
        



if __name__ == '__main__':
    unittest.main()
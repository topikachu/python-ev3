from ev3.lego import LargeMotor
import unittest
import time
from util import get_input


class TestLargeMotor(unittest.TestCase):
    def test_large_motor(self):
        get_input('Attach a LargeMotor then continue')
        d = LargeMotor()
        print(d.type)
        d.run_forever(100, regulation_mode=False)
        print(d.run)
        time.sleep(5)
        d.stop()
if __name__ == '__main__':
    unittest.main()

from ev3.lego import LargeMotor
import unittest
import time
from util import get_input


class TestLargeMotor(unittest.TestCase):
    def test_large_motor(self):
        get_input('Attach a LargeMotor then continue')
        d = LargeMotor()
        print(d.driver_name)
        d.run_forever(100, speed_regulation=False)
        print(d.state)
        time.sleep(5)
        d.stop()
if __name__ == '__main__':
    unittest.main()

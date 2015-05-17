from ev3.lego import MediumMotor
import unittest
import time
from util import get_input


class TesMediumMotor(unittest.TestCase):
    def test_medium_motor(self):
        get_input('Attach a MediumMotor then continue')
        d = MediumMotor()
        print(d.driver_name)
        d.run_forever(100, speed_regulation=False)
        print(d.state)
        time.sleep(5)
        d.stop()
if __name__ == '__main__':
    unittest.main()

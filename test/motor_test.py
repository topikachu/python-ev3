import time
import unittest

from ev3.rawdevice import motordevice


class TestMotorDevice(unittest.TestCase):

    def setUp(self):
        motordevice.open()

    def test_motor(self):
        # make sure the shuffled sequence does not lose any elements
        motordevice.start(0)
        motordevice.power(0,50)
        for i in range(0,10):
            print motordevice.get_tacho(0)
            print motordevice.get_speed(0)
            time.sleep(1)
        motordevice.stop(0)
    def tearDown(self):
        motordevice.close()


if __name__ == '__main__':
    unittest.main()
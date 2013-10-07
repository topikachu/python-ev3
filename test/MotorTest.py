from ev3.rawdevice import MotorDevice
import unittest
import time
class TestMotorDevice(unittest.TestCase):

    def setUp(self):
        MotorDevice.init()

    def test_motor(self):
        # make sure the shuffled sequence does not lose any elements
        MotorDevice.start(0)
        MotorDevice.power(0,50)
        for i in range(0,10):
            print MotorDevice.getTacho(0)
            print MotorDevice.getSpeed(0)
            time.sleep(1)
        MotorDevice.stop(0)
    def tearDown(self):
        MotorDevice.close()


if __name__ == '__main__':
    unittest.main()
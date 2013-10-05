from ev3.cdriver.rawdevice import MotorDevice
import unittest
import time
class TestMotorDevice(unittest.TestCase):

    def setUp(self):
        self.motorDevice = MotorDevice(0)

    def test_motor(self):
        # make sure the shuffled sequence does not lose any elements
        self.motorDevice.start()
        self.motorDevice.power(50)
        for i in range(0,10):
            print self.motorDevice.getTacho()
            print self.motorDevice.getSpeed()
            time.sleep(1)
        self.motorDevice.stop()
    def tearDown(self):
        self.motorDevice.close()


if __name__ == '__main__':
    unittest.main()
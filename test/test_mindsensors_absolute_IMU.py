from ev3.mindsensors import AbsoluteIMU
import unittest


class TestAbsoluteIMU(unittest.TestCase):

    def test_absolute_IMU(self):
        d = AbsoluteIMU(2)
        print(d.version)
        print(d.vendor_id)
        print(d.device_id)
        raw_input('test compass')
        print(d.compass)
        raw_input('test x_gyro')
        print(d.x_gyro)

if __name__ == '__main__':
    unittest.main()

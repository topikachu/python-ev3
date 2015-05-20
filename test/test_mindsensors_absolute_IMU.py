from ev3.mindsensors import AbsoluteIMU
import unittest
from util import get_input

class TestAbsoluteIMU(unittest.TestCase):

    def test_absolute_IMU(self):
        get_input('Attach a AbsoluteIMU at port 2 then continue')
        d = AbsoluteIMU(2)
        print(d.version)
        get_input('test compass')
        print(d.compass)
        get_input('test x_gyro')
        print(d.x_gyro)

if __name__ == '__main__':
    unittest.main()

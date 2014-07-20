from ev3.lego import UltrasonicSensor
import unittest


class TestUltrasonicSensor(unittest.TestCase):
    def test_ultrasonic_sensor(self):
        raw_input('Attach a UltrasonicSensor then continue')        
        d = UltrasonicSensor()        
        raw_input('test dist_cm')
        print(d.dist_cm)
        print(d.mode)
        raw_input('test dist_in')
        print(d.dist_in)
        print(d.mode)
        raw_input('test listen')
        print(d.listen)
        print(d.mode)
        raw_input('test si_cm')
        print(d.si_cm)
        print(d.mode)
        raw_input('test si_in')
        print(d.si_in)
        print(d.mode)



if __name__ == '__main__':
    unittest.main()

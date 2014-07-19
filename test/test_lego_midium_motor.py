from ev3.lego import MidiumMotor
import unittest
import time



class TesMidiumMotor(unittest.TestCase):
    def test_midium_motor(self):
        d = MidiumMotor()
        print(d.type)
        d.run_mode='forever'
        d.regulation_mode=True
        d.pulses_per_second_sp=200
        d.start()
        print(d.run)
        time.sleep(5)
        d.stop()
if __name__ == '__main__':
    unittest.main()

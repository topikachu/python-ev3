from ev3.lego import MediumMotor
import unittest
import time



class TesMediumMotor(unittest.TestCase):
    def test_medium_motor(self):
        raw_input('Attach a MediumMotor then continue')
        d = MediumMotor()
        print(d.type)
        d.run_forever(100, regulation_mode=False)
        print(d.run)
        time.sleep(5)
        d.stop()
if __name__ == '__main__':
    unittest.main()

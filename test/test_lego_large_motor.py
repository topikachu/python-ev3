from ev3.lego import LargeMotor
import unittest
import time



class TestLargeMotor(unittest.TestCase):
    def test_large_motor(self):
        raw_input('Attach a LargeMotor then continue')
        d = LargeMotor()
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

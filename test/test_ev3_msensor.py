from ev3.ev3dev import  Msensor
import unittest



class TestMsensor(unittest.TestCase):

    def test_msensor(self):
        raw_input('Attach a Msensor on port 1 then continue')
        d = Msensor(port=1)
        print(d.mode)
        type_id = d.type_id
        print(type_id)
        print(d.port)
        d = Msensor(type_id=type_id)
        print(d.mode)
        print(d.type_id)
        print(d.port)

if __name__ == '__main__':
    unittest.main()

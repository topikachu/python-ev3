from ev3.ev3dev import Ev3Dev, Msensor
import unittest



class TestEv3Dev(unittest.TestCase):
    d = Ev3Dev()
    d.dev_path = 'somepath'    
    print(d.dev_path)


class TestMsensor(unittest.TestCase):
    d = Msensor(port=1)
    print(d.mode)
    type_id = d.type_id_as_int
    print(type_id)
    print(d.port)
    d = Msensor(type_id=type_id)
    print(d.mode)
    print(d.type_id)
    print(d.port)

if __name__ == '__main__':
    unittest.main()

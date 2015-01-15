from ev3dev import LegoSensor, Motor


class TouchSensor(LegoSensor):

    def __init__(self, port=-1):
#Both lego-nxt-touch and lego-ev3-touch support auto
        LegoSensor.__init__(self, port, type_id=16, name='auto')

    @property
    def is_pushed(self):
        self.mode = 'TOUCH'
        return bool(self.value0)

class LightSensor(LegoSensor):
    
    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, type_id=1, name='lego-nxt-light')
    
    @property
    def reflect(self):
        self.mode = 'REFLECT'
        #Reflected light intensity (0 to 100)
        return self.value0/(int(self.decimals)*10)

    @property
    def ambient(self):
        self.mode = 'AMBIENT'
        #Ambient light intensity (0 to 100)
        return self.value0/(int(self.decimals)*10)

class SoundSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, type_id=1, name='nxt-analog')

    @property
    def db(self):
        self.mode = 'ANALOG-0'
        # Sound pressure level (0 to 1000)
        return "%.2f" % (self.value0/(int(self.decimals)*10))

    @property
    def dba(self):
        self.mode = 'ANALOG-1'
        # Sound pressure level (0 to 1000)
        return "%.2f" % (self.value0/(int(self.decimals)*10))

class ColorSensor(LegoSensor):
    colors = (None, 'black', 'blue', 'green',
              'yellow', 'red', 'white', 'brown')

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, type_id=29, name='ev3-uart-29')

    @property
    def rgb(self):
        self.mode = 'RGB-RAW'
        return self.value0, self.value1, self.value2

    @property
    def color(self):
        self.mode = 'COL-COLOR'
        return self.value0

    @property
    def reflect(self):
        self.mode = 'COL-REFLECT'
        return self.value0

    @property
    def ambient(self):
        self.mode = 'COL-AMBIENT'
        return self.value0

    @property
    def ref_raw(self):
        self.mode = 'REF-RAW'
        return self.value0, self.value1


class InfraredSensor(LegoSensor):

    def __init__(self, port=-1):
       LegoSensor.__init__(self, port, type_id=33, name='ev3-uart-33')

    @property
    def remote(self):
        self.mode = 'IR-REMOTE'
        return self.value0, self.value1, self.value2, self.value3

    @property
    def remote_bin(self):
        self.mode = 'IR-REM-A'
        return self.value0

    @property
    def prox(self):
        self.mode = 'IR-PROX'
        return self.value0

    @property
    def seek(self):
        self.mode = 'IR-SEEK'
        return [(self.value0, self.value1),
                (self.value2, self.value3),
                (self.value4, self.value5),
                (self.value6, self.value7)]


class GyroSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, type_id=32, name='ev3-uart-32')

    @property
    def ang(self):
        self.mode = 'GYRO-ANG'
        return self.value0

    @property
    def rate(self):
        self.mode = 'GYRO-RATE'
        return self.value0

    @property
    def ang_and_rate(self):
        self.mode = 'GYRO-G&A'
        return self.value0, self.value1


class UltrasonicSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, type_id=30, name='ev3-uart-30')

    @property
    def dist_cm(self):
        self.mode = 'US-DIST-CM'
        return self.value0

    @property
    def dist_in(self):
        self.mode = 'US-DIST-IN'
        return self.value0

    @property
    def listen(self):
        self.mode = 'US-LISTEN'
        return bool(self.value0)

    @property
    def si_cm(self):
        self.mode_force_flush('US-SI-CM')
        return self.value0

    @property
    def si_in(self):
        self.mode_force_flush('US-SI-IN')
        return self.value0


class LargeMotor(Motor):

    def __init__(self, port=''):
        Motor.__init__(self, port, _type='tacho')


class MediumMotor(Motor):

    def __init__(self, port=''):
        Motor.__init__(self, port, _type='minitacho')

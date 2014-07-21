from .ev3dev import Msensor, Motor


class TouchSensor(Msensor):

    def __init__(self, port=-1):
        Msensor.__init__(self, port, type_id=16)

    @property
    def is_pushed(self):
        self.mode = 'TOUCH'
        return bool(self.value0)


class ColorSensor(Msensor):
    colors = (None, 'black', 'blue', 'green',
              'yellow', 'red', 'white', 'brown')

    def __init__(self, port=-1):
        Msensor.__init__(self, port, type_id=29)

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


class InfraredSensor(Msensor):

    def __init__(self, port=-1):
        Msensor.__init__(self, port, type_id=33)

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


class GyroSensor(Msensor):

    def __init__(self, port=-1):
        Msensor.__init__(self, port, type_id=32)

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


class UltrasonicSensor(Msensor):

    def __init__(self, port=-1):
        Msensor.__init__(self, port, type_id=30)

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

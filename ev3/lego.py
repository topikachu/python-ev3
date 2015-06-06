from .ev3dev import LegoSensor, Motor


class TouchSensor(LegoSensor):

    def __init__(self, port=-1):
        # Both lego-nxt-touch and lego-ev3-touch support auto
        LegoSensor.__init__(self, port, name='lego-ev3-touch')

    @property
    def is_pushed(self):
        self.mode = 'TOUCH'
        return bool(self.value0)


class LightSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, name='lego-nxt-light')

    @property
    def reflect(self):
        self.mode = 'REFLECT'
        # Reflected light intensity (0 to 100)
        return self.value0/10.0

    @property
    def ambient(self):
        self.mode = 'AMBIENT'
        # Ambient light intensity (0 to 100)
        return self.value0/10.0


class SoundSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, name='lego-nxt-sound')

    @property
    def db(self):
        self.mode = 'DB'
        # Sound pressure level (0 to 1000)
        return self.value0/10.0

    @property
    def dba(self):
        self.mode = 'DBA'
        # Sound pressure level (0 to 1000)
        return self.value0/10.0


class ColorSensor(LegoSensor):
    colors = (None, 'black', 'blue', 'green',
              'yellow', 'red', 'white', 'brown')

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, name='lego-ev3-color')

    @property
    def rgb(self):
        """Raw color components; (`r`, `g`, `b`). Values between 0 and 1020(??).

        All leds rapidly cycle, appears white."""
        self.mode = 'RGB-RAW'
        return self.value0, self.value1, self.value2

    @property
    def color(self):
        """Integer between 0 and 7 indicating the color. See the `colors`
        attribute for color names.

        All leds rapidly cycle, appears white."""
        self.mode = 'COL-COLOR'
        return self.value0

    @property
    def reflect(self):
        """Reflected intensity in percent (int). Red led is on."""
        self.mode = 'COL-REFLECT'
        return self.value0

    @property
    def ambient(self):
        """Ambient intensity in percent (int). Red led is off."""
        self.mode = 'COL-AMBIENT'
        return self.value0

    @property
    def ref_raw(self):
        """Raw reflected intensity; (`r`, `b`). Values between 0 and 1020(??).

        Red led is on."""
        self.mode = 'REF-RAW'
        return self.value0, self.value1


class InfraredSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, name='lego-ev3-ir')

    class REMOTE:

        """Button values for the `remote` property."""
        NONE = 0
        RED_UP = 1
        RED_DOWN = 2
        BLUE_UP = 3
        BLUE_DOWN = 4
        RED_UP_AND_BLUE_UP = 5
        RED_UP_AND_BLUE_DOWN = 6
        RED_DOWN_AND_BLUE_UP = 7
        RED_DOWN_AND_BLUE_DOWN = 8
        BAECON_MODE_ON = 9
        RED_UP_AND_RED_DOWN = 10
        BLUE_UP_AND_BLUE_DOWN = 11

    @property
    def remote(self):
        """IR remote control mode. A tuple of recieved value for each of the 4
        channels.
        """
        self.mode = 'IR-REMOTE'
        return self.value0, self.value1, self.value2, self.value3

    @property
    def remote_bin(self):
        self.mode = 'IR-REM-A'
        return self.value0

    @property
    def prox(self):
        """Proximity mode. Distance in percent (100% is about 70cm)."""
        self.mode = 'IR-PROX'
        return self.value0

    @property
    def seek(self):
        """IR Seeker mode. A list of (`heading`, `distance`) pairs for each of
        the 4 channels.

        When looking in the same direction as the sensor, `heading` =
        -25 is far left and `heading` = +25 is far right.

        `distance` is the distance in percent (100% is about 70cm).

        Channels with no baecon returns (0, 128).
        """
        self.mode = 'IR-SEEK'
        return [(self.value0, self.value1),
                (self.value2, self.value3),
                (self.value4, self.value5),
                (self.value6, self.value7)]


class GyroSensor(LegoSensor):

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, name='lego-ev3-gyro')

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
        LegoSensor.__init__(self, port, name='lego-ev3-us')

    @property
    def dist_cm(self):
        self.mode = 'US-DIST-CM'
        return self.value0/10.0

    @property
    def dist_in(self):
        self.mode = 'US-DIST-IN'
        return self.value0/10.0

    @property
    def listen(self):
        self.mode = 'US-LISTEN'
        return bool(self.value0)

    @property
    def si_cm(self):
        self.mode_force_flush('US-SI-CM')
        return self.value0/10.0

    @property
    def si_in(self):
        self.mode_force_flush('US-SI-IN')
        return self.value0/10.0


class LargeMotor(Motor):

    def __init__(self, port=''):
        Motor.__init__(self, port, _type='lego-ev3-l-motor')


class MediumMotor(Motor):

    def __init__(self, port=''):
        Motor.__init__(self, port, _type='lego-ev3-m-motor')

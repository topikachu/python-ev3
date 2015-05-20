from .ev3dev import I2CS
from .ev3dev import LegoSensor


class MindSensorI2CS(I2CS):

    @property
    def version(self):
        return self.read_byte_array_as_string(0x00, 8)

    @property
    def vendor_id(self):
        return self.read_byte_array_as_string(0x08, 8)

    @property
    def device_id(self):
        return self.read_byte_array_as_string(0x10, 8)


@I2CS.create_i2c_property(
    command=(0x41, {'read_only': False}),
    button_set_1 = 0x42,
    button_set_2= 0x43,
    x_left= 0x44,
    y_left= 0x45,
    x_right= 0x46,
    y_right= 0x47,
    up= 0x4A,
    right= 0x4B,
    down= 0x4C,
    left= 0x4D,
    l2= 0x4E,
    r2= 0x4F,
    l1= 0x50,
    r1= 0x51,
    triangle= 0x52,
    circle= 0x53,
    cross= 0x54,
    square= 0x55)
class PSPNxV4(MindSensorI2CS):

    def __init__(self, port, addr=0x01):
        I2CS.__init__(self, port, addr)
        self.command = 0x49


class AbsoluteIMU(LegoSensor):
    # Is this too tricky to create property?

    def __init__(self, port=-1):
        LegoSensor.__init__(self, port, name='ms-absolute-imu')
        self._mode = ''

    @property
    def version(self):
        return self.fw_version

    @property
    def compass_cal_start(self):
        self.write_value('command', 'BEGIN-COMP-CAL')

    @property
    def compass_cal_end(self):
        self.write_value('command', 'END-COMP-CAL')

    @property
    def acc_2g(self):
        self.write_value('command', 'ACCEL-2G')

    @property
    def acc_4g(self):
        self.write_value('command', 'ACCEL-4G')

    @property
    def acc_8g(self):
        self.write_value('command', 'ACCEL-8G')

    @property
    def acc_16g(self):
        self.write_value('command', 'ACCEL-16G')

    @property
    def x_acc(self):
        self.mode = 'ACCEL'
        return self.value0

    @property
    def y_acc(self):
        self.mode = 'ACCEL'
        return self.value1

    @property
    def z_acc(self):
        self.mode = 'ACCEL'
        return self.value2

    @property
    def x_tilt(self):
        self.mode = 'TILT'
        return self.value0

    @property
    def y_tilt(self):
        self.mode = 'TILT'
        return self.value1

    @property
    def z_tilt(self):
        self.mode = 'TILT'
        return self.value2

    @property
    def x_raw_magnetic(self):
        self.mode = 'MAG'
        return self.value0

    @property
    def y_raw_magnetic(self):
        self.mode = 'MAG'
        return self.value1

    @property
    def z_raw_magnetic(self):
        self.mode = 'MAG'
        return self.value2

    @property
    def x_gyro(self):
        self.mode = 'GYRO'
        return self.value0

    @property
    def y_gyro(self):
        self.mode = 'GYRO'
        return self.value1

    @property
    def z_gyro(self):
        self.mode = 'COMPASS'
        return self.value0

    @property
    def compass(self):
        self.mode = 'GYRO'
        return self.value2


class MagicWand(MindSensorI2CS):

    val = 0xff

    # port = 1..4 , matching the EV3 input port where the magic wand is
    # connected
    def __init__(self, port, addr=0x38):
        MindSensorI2CS.__init__(self, port, addr)

    def put_data(self, v):
        self.val = v
        MindSensorI2CS.write_byte(self, v)

    # turns all leds on
    def led_all_on(self):
        self.put_data(0x00)

    # turns all leds off
    def led_all_off(self):
        self.put_data(0xff)

    # turns a specific led on. leds are indexed 1..8
    def led_on(self, num):
        self.put_data(self.val & (0xff - (1 << (num - 1))))

    # turns a specific led off. leds are indexed 1..8
    def led_off(self, num):
        self.put_data(self.val | (1 << (num - 1)))

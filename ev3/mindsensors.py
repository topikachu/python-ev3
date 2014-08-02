from .ev3dev import I2CS


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


def absoluteIMU_property(cls):
    for prop in ['x_acc', 'y_acc', 'z_acc',
                             'x_raw_magnetic', 'y_raw_magnetic', 'z_raw_magnetic',
                             'x_gyro', 'y_gyro', 'z_gyro',
                             'compass']:
        def fget(self):
            return (getattr(self, prop + '_msb') << 8) + getattr(self, prop + '_lsb')
        setattr(cls, prop, property(fget))
    return cls

@I2CS.create_i2c_property(
    command=(0x41, {'read_only':False}),
    x_tilt= 0x42,
    y_tilt= 0x43,
    z_tilt= 0x44,
    x_acc_lsb= 0x45,
    x_acc_msb= 0x46,
    y_acc_lsb= 0x47,
    y_acc_msb= 0x48,
    z_acc_lsb= 0x49,
    z_acc_msb= 0x4A,
    compass_lsb= 0x4B,
    compass_msb= 0x4C,
    x_raw_magnetic_lsb= 0x4D,
    x_raw_magnetic_msb= 0x4E,
    y_raw_magnetic_lsb= 0x4F,
    y_raw_magnetic_msb= 0x50,
    z_raw_magnetic_lsb= 0x51,
    z_raw_magnetic_msb= 0x52,
    x_gyro_lsb= 0x53,
    x_gyro_msb= 0x54,
    y_gyro_lsb= 0x55,
    y_gyro_msb= 0x56,
    z_gyro_lsb= 0x57,
    z_gyro_msb= 0x58,
    gyro_filter= 0x5A)
@absoluteIMU_property
class AbsoluteIMU(MindSensorI2CS):
# Is this too tricky to create property?

    def __init__(self, port, addr=0x11):
        I2CS.__init__(self, port, addr)

    def compass_cal_start(self):
        self.command = 0x43

    def compass_cal_end(self):
        self.command = 0x63

    def acc_2g(self):
        self.command = 0x31

    def acc_4g(self):
        self.command = 0x32

    def acc_8g(self):
        self.command = 0x33

    def acc_16g(self):
        self.command = 0x34

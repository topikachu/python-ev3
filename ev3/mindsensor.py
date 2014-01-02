import sensor
import functools


class PSPNxV4(sensor.IICSensor):

    __command_map = {"button_set_1": 0x42,
                     "button_set_2": 0x43,
                     "x_left": 0x44,
                     "y_left": 0x45,
                     "x_right": 0x46,
                     "y_right": 0x47,
                     "up": 0x4A,
                     "right": 0x4B,
                     "down": 0x4C,
                     "left": 0x4D,
                     "l2": 0x4E,
                     "r2": 0x4F,
                     "l1": 0x50,
                     "r1": 0x51,
                     "triangle": 0x52,
                     "circle": 0x52,
                     "cross": 0x53,
                     "square": 0x54,

                     }

    def __init__(self, port, address=0x02):
        self.port = port
        super(PSPNxV4, self).__init__(port, address)
        # Initialize the Playstation 2 Wireless Receiver dongle (attached to
        # PSPNxV4-Nx)
        self.command(0x41, 0x49)

    def read_value(self, button):
        register = PSPNxV4.__command_map[button]
        return self.read_single_byte(register) & 0xff

    def __getattr__(self, attrName):
        return functools.partial(self.read_value, attrName[len("get_"):])


class DistNxV3(sensor.IICSensor):

    def __init__(self, port, address=0x02):
        super(DistNxV3, self).__init__(port, address)

    def get_distance(self):
        data = self.read(0x42, 2)
        distance = (0x00FF & data[0])
        distance += ((0x00FF & data[1]) << 8)
        return distance

    def get_voltage(self):
        data = self.read(0x44, 2)
        voltage = (0x00FF & data[0])
        voltage += ((0x00FF & data[1]) << 8)
        return voltage

    def energize(self):
        self.command(0x41, 0x45)

    def de_energize(self):
        self.command(0x41, 0x44)

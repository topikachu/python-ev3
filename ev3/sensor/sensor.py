import time
from ..rawdevice import uartdevice
from ..rawdevice import analogdevice
from ..rawdevice import iicdevice


class UartSensor(object):

    def __init__(self, port):
        self.port = port
        uartdevice.reset(port)

    def set_mode(self, mode, delay=0):
        time.sleep(delay)
        self.mode = mode
        uartdevice.set_mode(self.port, mode)

    def get_value(self):
        return uartdevice.get_value_byte(self.port)

    def get_value_bytes(self):
        return uartdevice.get_value_bytes(self.port)

    def reset(self):
        uartdevice.reset(self.port)


class AnalogSensor(object):

    def __init__(self, port):
        self.port = port
        analogdevice.clear_change(port)

    def get_pin1_value(self):
        return analogdevice.get_pin1(self.port)

    def get_pin6_value(self):
        return analogdevice.get_pin6(self.port)


class IICSensor(object):

    def __init__(self, port, address):
        self.port = port
        iicdevice.reset(port)
        self.address = address

    def transaction(self, send_buf, read_length):
        values = iicdevice.i2c_transaction(
            self.port, self.address, send_buf, read_length)
        return values[:read_length]

    def read(self, register, read_length=32):
        values = iicdevice.i2c_transaction(
            self.port, self.address, [register], read_length)
        return values[:read_length]

    def read_single_byte(self, register):
        values = iicdevice.i2c_transaction(
            self.port, self.address, [register], 1)
        return values[0]

    def command(self, register, cmd):
        iicdevice.i2c_transaction(self.port, self.address, [register, cmd], 0)

    def version(self):
        return bytearray(self.read(0x00, 8)).decode()

    def vendor(self):
        return bytearray(self.read(0x08, 8)).decode()

    def device(self):
        return bytearray(self.read(0x10, 8)).decode()


__all__ = ['IICSensor', 'UartSensor', 'AnalogSensor']

import struct
import sensor
from ..rawdevice import lms2012


class HiTechncCompass(sensor.IICSensor):

    def __init__(self, port, address):
        super(HiTechncCompass, self).__init__(port, address)

    def get_angle(self):
        sensor_data = self.read(0x44, 2)
        angle = (0x00FF & sensor_data[0])
        angle += ((0x00FF & sensor_data[1]) << 8)
        return (angle)


class HiTechncPIRSensor(sensor.IICSensor):

    def __init__(self, port, address):
        super(HiTechncPIRSensor, self).__init__(port, address)

    def get_measurement(self):
        sensor_data = self.read(0x42, 1)
        return sensor_data[0]

    def set_deadband(self, db):
        self.command(0x41, db)

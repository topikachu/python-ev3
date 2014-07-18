import os
import glob


class NoSuchSensorError(Exception):

    def __init__(self, port, type_id):
        self.port = port
        self.type_id = type_id

    def __str__(self):
        return "No such sensor port=%d type_id=%d" % (self.port, self.type_id)


class NoSuchMotorError(Exception):

    def __init__(self, port, _type):
        self.port = port
        self._type = _type

    def __str__(self):
        return "No such sensor port=%s type=%s" % (self.port, self._type)


class Ev3StringType(object):

    @staticmethod
    def post_read(value):
        return value

    @staticmethod
    def pre_write(value):
        return value


class Ev3IntType(object):

    @staticmethod
    def post_read(value):
        return int(value)

    @staticmethod
    def pre_write(value):
        return str(value)


class Ev3BoolType(object):

    @staticmethod
    def post_read(value):
        return bool(value)

    @staticmethod
    def pre_write(value):
        return '1' if value else '0'


class Ev3OnOffType(object):

    @staticmethod
    def post_read(value):
        return True if value == 'on' else False

    @staticmethod
    def pre_write(value):
        if (value == 'on' or value == 'off'):
            return value
        else:
            return 'on' if bool(value) else 'off'


def create_ev3_property(name, readonly=False, property_type=Ev3StringType):
    def fget(self):
        return property_type.post_read(self.read_value(name))

    def fset(self, value):
        self.write_value(name, property_type.pre_write(value))

    return property(fget, fset if not readonly else None)


class Ev3Dev(object):

    def __init__(self):
        self._sys_path = ""
        pass

    def read_value(self, name):
        attr_file = os.path.join(self.sys_path, name)
        if os.path.isfile(attr_file):
            f = open(attr_file)
            value = f.read().strip()
            f.close()
            return value
        else:
            return None

    @property
    def sys_path(self):
        return self._sys_path

    @sys_path.setter
    def sys_path(self, path):
        self._sys_path = path

    def write_value(self, name, value):
        attr_file = os.path.join(self.sys_path, name)       
        if os.path.isfile(attr_file):
            f = open(attr_file, 'w')
            f.write(str(value))
            f.close()
        else:
            return


class Msensor(Ev3Dev):
    property_list = [
        {'name': 'bin_data', 'readonly': True},
        {'name': 'bin_data_format', 'readonly': True},
        {'name': 'dp', 'readonly': True},
        {'name': 'mode', 'readonly': False},
        {'name': 'modes', 'readonly': True},
        {'name': 'port_name', 'readonly': True},
        {'name': 'type_id', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'uevent', 'readonly': True},
        {'name': 'units', 'readonly': True},
        {'name': 'value0', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value1', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value2', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value3', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value4', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value5', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value6', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'value7', 'readonly': True, 'property_type': Ev3IntType}
    ]

    def __init__(self, port=-1, type_id=-1):
        Ev3Dev.__init__(self)
        type_id = int(type_id)
        sensor_existing = False
        if (port > 0):
            self.port = port
            for p in glob.glob('/sys/class/msensor/sensor*/port_name'):
                f = file(p)
                value = f.read().strip()
                f.close()
                if (value == 'in' + str(port)):
                    self.sys_path = os.path.dirname(p)
                    sensor_existing = True
                    break
        if (type_id > 0 and port == -1):
            for p in glob.glob('/sys/class/msensor/sensor*/type_id'):
                f = file(p)
                value = int(f.read().strip())
                f.close()
                if (value == type_id):
                    self.sys_path = os.path.dirname(p)
                    self.port = int(self.port_name[2:])
                    sensor_existing = True
                    break
        if (not sensor_existing):
            raise NoSuchSensorError(port, type_id)
        self._mode = ''

    # @property
    # def mode(self):
    #     return self._mode

    # @mode.setter
    # def mode(self, value):
    #     if (self._mode != value):
    #         self._mode = value
    #         self.write_value('mode', value)

    def mode_force_flush(self, value):
        self._mode = value
        self.write_value('mode', value)

for p in Msensor.property_list:
    setattr(Msensor, p['name'],  create_ev3_property(**p))


class Motor(Ev3Dev):
    property_list = [
        {'name': 'duty_cycle', 'readonly': True, 'property_type': Ev3IntType},
        {'name': 'duty_cycle_sp', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'estop', 'readonly': False, 'property_type': Ev3IntType},
        {'name': 'polarity_mode', 'readonly': False},
        {'name': 'port_name', 'readonly': True},
        {'name': 'position', 'readonly': False, 'property_type': Ev3IntType},
        {'name': 'position_mode', 'readonly': False},
        {'name': 'position_sp', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'pulses_per_second', 'readonly':
            True, 'property_type': Ev3IntType},
        {'name': 'pulses_per_second_sp', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'ramp_down_sp', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'ramp_up_sp', 'readonly': False, 'property_type': Ev3IntType},
        {'name': 'regulation_mode', 'readonly':
            False, 'property_type': Ev3OnOffType},
        {'name': 'reset', 'readonly': False},
        {'name': 'run', 'readonly': False, 'property_type': Ev3BoolType},
        {'name': 'run_mode', 'readonly': False},
        {'name': 'speed_regulation_D', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'speed_regulation_I', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'speed_regulation_K', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'speed_regulation_P', 'readonly':
            False, 'property_type': Ev3IntType},
        {'name': 'state', 'readonly': True},
        {'name': 'stop_mode', 'readonly': False},
        {'name': 'stop_modes', 'readonly': False},
        {'name': 'time_sp', 'readonly': False, 'property_type': Ev3IntType},
        {'name': 'type', 'readonly': False},
        {'name': 'uevent', 'readonly': True}
    ]

    def __init__(self, port='', _type=''):
        Ev3Dev.__init__(self)
        motor_existing = False
        if (port != ''):
            self.port = port
            for p in glob.glob('/sys/class/tacho-motor/tacho-motor*/port_name'):
                f = file(p)
                value = f.read().strip()
                f.close()
                if (value.lower() == ('out' + port).lower()):
                    self.sys_path = os.path.dirname(p)
                    motor_existing = True
                    break
        if (_type != '' and port == ''):
            for p in glob.glob('/sys/class/tacho-motor/tacho-motor*/type'):
                f = file(p)
                value = f.read().strip()
                f.close()
                if (value.lower() == _type.lower()):
                    self.sys_path = os.path.dirname(p)
                    self.port = self.port_name[3:]
                    motor_existing = True
                    break
        if (not motor_existing):
            raise NoSuchMotorError(port, _type)


    def stop(self):
        self.run = False

    def start(self):
        self.run = True

for p in Motor.property_list:
    setattr(Motor, p['name'],  create_ev3_property(**p))

import os
import glob


class NoSuchSensorError(Exception):

    def __init__(self, port, type_id=None):
        self.port = port
        self.type_id = type_id

    def __str__(self):
        return "No such sensor port=%d type_id=%s" % (self.port, repr(self.type_id))


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


def ev3_meta(property_list=None, const_list=None):
    class Ev3Meta(type):

        def __new__(cls, name, bases, attr):
            if (const_list != None):
                for c in const_list:
                    attr[c] = c

            if (property_list != None):
                for p in property_list:
                    def create_ev3_property(name, read_only=False, property_type=Ev3StringType):
                        def fget(self):
                            return property_type.post_read(self.read_value(name))

                        def fset(self, value):
                            self.write_value(
                                name, property_type.pre_write(value))
                        return property(fget, fset if not read_only else None)
                    attr[p['name']] = create_ev3_property(**p)
            return type.__new__(cls, name, bases, attr)
    return Ev3Meta


class Ev3Dev(object):

    def __init__(self):
        self.sys_path = ""

    def read_value(self, name):
        attr_file = os.path.join(self.sys_path, name)
        if os.path.isfile(attr_file):
            f = open(attr_file)
            value = f.read().strip()
            f.close()
            return value
        else:
            return None

    def write_value(self, name, value):
        attr_file = os.path.join(self.sys_path, name)
        if os.path.isfile(attr_file):
            f = open(attr_file, 'w')
            f.write(str(value))
            print name, value
            f.close()
        else:
            return


class Msensor(Ev3Dev):
    __metaclass__ = ev3_meta(property_list=[
        {'name': 'bin_data', 'read_only': True},
        {'name': 'bin_data_format', 'read_only': True},
        {'name': 'dp', 'read_only': True},
        #{'name': 'mode', 'read_only': False},
        {'name': 'modes', 'read_only': True},
        {'name': 'port_name', 'read_only': True},
        {'name': 'type_id', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'uevent', 'read_only': True},
        {'name': 'units', 'read_only': True},
        {'name': 'value0', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value1', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value2', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value3', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value4', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value5', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value6', 'read_only': True, 'property_type': Ev3IntType},
        {'name': 'value7', 'read_only': True, 'property_type': Ev3IntType}
    ])

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

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if (self._mode != value):
            self._mode = value
            self.write_value('mode', value)

    def mode_force_flush(self, value):
        self._mode = value
        self.write_value('mode', value)


class Motor(Ev3Dev):
    __metaclass__ = ev3_meta(
        const_list=['coast', 'brake', 'hold', 'relative',
                    'absolute', 'A', 'B', 'C', 'D'],
        property_list=[
            {'name': 'duty_cycle', 'read_only':
             True, 'property_type': Ev3IntType},
            {'name': 'duty_cycle_sp', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'estop', 'read_only': False,
             'property_type': Ev3IntType},
            {'name': 'polarity_mode', 'read_only': False},
            {'name': 'port_name', 'read_only': True},
            {'name': 'position', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'position_mode', 'read_only': False},
            {'name': 'position_sp', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'pulses_per_second', 'read_only':
             True, 'property_type': Ev3IntType},
            {'name': 'pulses_per_second_sp', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'ramp_down_sp', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'ramp_up_sp', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'regulation_mode', 'read_only':
             False, 'property_type': Ev3OnOffType},
            #{'name': 'reset', 'read_only': False},
            {'name': 'run', 'read_only': False,
                            'property_type': Ev3BoolType},
            {'name': 'run_mode', 'read_only': False},
            {'name': 'speed_regulation_D', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'speed_regulation_I', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'speed_regulation_K', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'speed_regulation_P', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'state', 'read_only': True},
            {'name': 'stop_mode', 'read_only': False},
            {'name': 'stop_modes', 'read_only': False},
            {'name': 'time_sp', 'read_only':
             False, 'property_type': Ev3IntType},
            {'name': 'type', 'read_only': False},
            {'name': 'uevent', 'read_only': True}
        ]
    )

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

    def reset(self):
        self.write_value('reset', 1)

    def run_forever(self, speed_sp, **kwargs):
        self.run_mode = 'forever'
        for k in kwargs:
            v = kwargs[k]
            if (v != None):
                setattr(self, k, v)
        regulation_mode = self.regulation_mode
        if (regulation_mode):
            self.pulses_per_second_sp = speed_sp
        else:
            self.duty_cycle_sp = speed_sp
        self.start()

    def run_time_limited(self, time_sp, speed_sp,  **kwargs):
        self.run_mode = 'time'
        for k in kwargs:
            v = kwargs[k]
            if (v != None):
                setattr(self, k, v)
        regulation_mode = self.regulation_mode
        if (regulation_mode):
            self.pulses_per_second_sp = speed_sp
        else:
            self.duty_cycle_sp = speed_sp
        self.time_sp = time_sp
        self.start()

    def run_position_limited(self, position_sp, speed_sp,  **kwargs):
        self.run_mode = 'position'
        kwargs['regulation_mode'] = True
        for k in kwargs:
            v = kwargs[k]
            if (v != None):
                setattr(self, k, v)
        self.pulses_per_second_sp = speed_sp
        self.position_sp = position_sp
        self.start()

from smbus import SMBus


class I2CMeta(type):

    def __new__(cls, name, bases, attr):
        smbus_proxied_methods = [
            m for m in dir(SMBus) if (m.startswith('read') or m.startswith('write'))]
        for m in smbus_proxied_methods:
            def create_proxied_smb_method(method):
                def proxied_smb_method(self, *args, **kwargs):
                    return getattr(self.b, method)(self.addr, *args, **kwargs)
                return proxied_smb_method
            attr[m] = create_proxied_smb_method(m)
        return type.__new__(cls, name, bases, attr)


class I2CS(object):
    __metaclass__ = I2CMeta

    def __init__(self, port, addr):
        self.port = port
        self.i2c_port = port + 2
        self.sys_path = '/dev/i2c-%s' % self.i2c_port
        if (not os.path.exists(self.sys_path)):
            raise NoSuchSensorError(port)
        self.b = SMBus(self.i2c_port)
        self.addr = addr

    def read_byte_array(self, reg, _len):
        return [self.read_byte_data(reg + r) for r in range(_len)]

    def read_byte_array_as_string(self, reg, _len):
        return ''.join(chr(r) for r in self.read_byte_array(reg, _len))

    @staticmethod
    def i2c_prop_meta(i2c_property_list):
        class I2CPropMeta(I2CMeta):

            def __new__(cls, name, bases, attr):
                for prop, reg_add in i2c_property_list.iteritems():
                    def create_i2c_property(reg, read_only=True):
                        def fget(self):
                            return self.read_byte_data(reg)

                        def fset(self, value):
                            return self.write_byte_data(reg, value)
                        return property(fget, None if read_only else fset)
                    if (type(reg_add) == int):
                        attr[prop] = create_i2c_property(reg_add)
                    else:
                        attr[prop] = create_i2c_property(
                            reg_add[0], **reg_add[1])
                return super(I2CPropMeta, cls).__new__(cls, name, bases, attr)
        return I2CPropMeta

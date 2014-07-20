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


def create_ev3_prop(**kwargs):
    class Ev3Meta(type):

        def __new__(cls, name, bases, attr):
            for name, args in kwargs.iteritems():
                def create_ev3_property(name, read_only=False, property_type=Ev3StringType):
                    def fget(self):
                        return property_type.post_read(self.read_value(name))

                    def fset(self, value):
                        self.write_value(
                            name, property_type.pre_write(value))
                    return property(fget, None if read_only else fset)
                attr[name] = create_ev3_property(name, **args)
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
            f.close()
        else:
            return


class Msensor(Ev3Dev):
    __metaclass__ = create_ev3_prop(
        bin_data={'read_only': True},
        bin_data_format={'read_only': True},
        dp={'read_only': True},
        #mode={ 'read_only': False},
        modes={'read_only': True},
        port_name={'read_only': True},
        type_id={'read_only': True, 'property_type': Ev3IntType},
        uevent={'read_only': True},
        units={'read_only': True},
        value0={'read_only': True, 'property_type': Ev3IntType},
        value1={'read_only': True, 'property_type': Ev3IntType},
        value2={'read_only': True, 'property_type': Ev3IntType},
        value3={'read_only': True, 'property_type': Ev3IntType},
        value4={'read_only': True, 'property_type': Ev3IntType},
        value5={'read_only': True, 'property_type': Ev3IntType},
        value6={'read_only': True, 'property_type': Ev3IntType},
        value7={'read_only': True, 'property_type': Ev3IntType}
    )

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
        self._mode = self.read_value('mode')

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


class Enum(object):

    def __init__(self, *args, **kwargs):
            for arg in args:
                kwargs[arg] = arg
            self.enum_dict = kwargs

    def __getattr__(self, name):
        if (self.enum_dict.has_key(name)):
            return self.enum_dict[name]
        else:
            raise NameError("no such item %s" % name)


class Motor(Ev3Dev):
    STOP_MODE = Enum(COAST='coast', BRAKE='brake', HOLD='hold')
    POSITION_MODE = Enum(RELATIVE='relative', ABSOLUTE='absolute')
    PORT = Enum('A', 'B', 'C', 'D')
    __metaclass__ = create_ev3_prop(
        duty_cycle={'read_only': True, 'property_type': Ev3IntType},
        duty_cycle_sp={'read_only': False, 'property_type': Ev3IntType},
        estop={'read_only': False, 'property_type': Ev3IntType},
        polarity_mode={'read_only': False},
        port_name={'read_only': True},
        position={'read_only': False, 'property_type': Ev3IntType},
        position_mode={'read_only': False},
        position_sp={'read_only': False, 'property_type': Ev3IntType},
        pulses_per_second={'read_only': True, 'property_type': Ev3IntType},
        pulses_per_second_sp={'read_only': False, 'property_type': Ev3IntType},
        ramp_down_sp={'read_only': False, 'property_type': Ev3IntType},
        ramp_up_sp={'read_only': False, 'property_type': Ev3IntType},
        regulation_mode={'read_only': False, 'property_type': Ev3OnOffType},
        #reset={ 'read_only': False},
        run={'read_only': False, 'property_type': Ev3BoolType},
        run_mode={'read_only': False},
        speed_regulation_D={'read_only': False, 'property_type': Ev3IntType},
        speed_regulation_I={'read_only': False, 'property_type': Ev3IntType},
        speed_regulation_K={'read_only': False, 'property_type': Ev3IntType},
        speed_regulation_P={'read_only': False, 'property_type': Ev3IntType},
        state={'read_only': True},
        stop_mode={'read_only': False},
        stop_modes={'read_only': False},
        time_sp={'read_only': False, 'property_type': Ev3IntType},
        type={'read_only': False},
        uevent={'read_only': True}

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


class I2CSMBusProxy(type):

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
    __metaclass__ = I2CSMBusProxy

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
    def create_i2c_prop(**kwargs):
        class I2CPropMeta(I2CSMBusProxy):

            def __new__(cls, name, bases, attr):
                for prop, reg_add in kwargs.iteritems():
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

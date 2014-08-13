import os
import glob
import sys
import warnings


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


class NoSuchLibraryError(Exception):

    def __init__(self, lib=""):
        self.lib = lib

    def __str__(self):
        return "No such library %s" % self.lib


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


class create_ev3_property(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, cls):
        for name, args in self.kwargs.items():
            def ev3_property(name, read_only=False, property_type=Ev3StringType):
                def fget(self):
                    return property_type.post_read(self.read_value(name))

                def fset(self, value):
                    self.write_value(
                        name, property_type.pre_write(value))
                return property(fget, None if read_only else fset)

            setattr(cls, name, ev3_property(name, **args))

        return cls


class Ev3Dev(object):

    def __init__(self):
        self.sys_path = ""

    def read_value(self, name):
        attr_file = os.path.join(self.sys_path, name)
        if os.path.isfile(attr_file):
            with open(attr_file) as f:
                value = f.read().strip()
                return value
        else:
            return None

    def write_value(self, name, value):
        attr_file = os.path.join(self.sys_path, name)
        if os.path.isfile(attr_file):
            with open(attr_file, 'w') as f:
                f.write(str(value))
        else:
            return


@create_ev3_property(
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
class Msensor(Ev3Dev):

    def __init__(self, port=-1, type_id=-1):
        Ev3Dev.__init__(self)
        type_id = int(type_id)
        sensor_existing = False
        if (port > 0):
            self.port = port
            for p in glob.glob('/sys/class/msensor/sensor*/port_name'):
                with open(p) as f:
                    value = f.read().strip()
                    if (value == 'in' + str(port)):
                        self.sys_path = os.path.dirname(p)
                        sensor_existing = True
                        break
        if (type_id > 0 and port == -1):
            for p in glob.glob('/sys/class/msensor/sensor*/type_id'):
                with open(p) as f:
                    value = int(f.read().strip())
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
        if (name in self.enum_dict.keys()):
            return self.enum_dict[name]
        else:
            raise NameError("no such item %s" % name)


@create_ev3_property(
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
class Motor(Ev3Dev):
    STOP_MODE = Enum(COAST='coast', BRAKE='brake', HOLD='hold')
    POSITION_MODE = Enum(RELATIVE='relative', ABSOLUTE='absolute')
    PORT = Enum('A', 'B', 'C', 'D')

    def __init__(self, port='', _type=''):
        Ev3Dev.__init__(self)
        motor_existing = False
        if (port != ''):
            self.port = port
            for p in glob.glob('/sys/class/tacho-motor/tacho-motor*/port_name'):
                with open(p) as f:
                    value = f.read().strip()
                    if (value.lower() == ('out' + port).lower()):
                        self.sys_path = os.path.dirname(p)
                        motor_existing = True
                        break
        if (_type != '' and port == ''):
            for p in glob.glob('/sys/class/tacho-motor/tacho-motor*/type'):
                with open(p) as f:
                    value = f.read().strip()
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


def I2CSMBusProxy(cls):
    try:
        from smbus import SMBus
        smbus_proxied_methods = [
            m for m in dir(SMBus) if (m.startswith('read') or m.startswith('write'))]
        for m in smbus_proxied_methods:
            def create_proxied_smb_method(method):
                def proxied_smb_method(self, *args, **kwargs):
                    return getattr(self.b, method)(self.addr, *args, **kwargs)
                return proxied_smb_method
            setattr(cls, m,  create_proxied_smb_method(m))
        return cls
    except ImportError:
        warnings.warn('python-smbus binding not found!')
        return cls


@I2CSMBusProxy
class I2CS(object):

    def __init__(self, port, addr):
        self.port = port
        self.i2c_port = port + 2
        self.sys_path = '/dev/i2c-%s' % self.i2c_port
        if (not os.path.exists(self.sys_path)):
            raise NoSuchSensorError(port)
        try:
            from smbus import SMBus
            self.b = SMBus(self.i2c_port)
            self.addr = addr
        except ImportError:
            raise NoSuchLibraryError('smbus')

    def read_byte_array(self, reg, _len):
        return [self.read_byte_data(reg + r) for r in range(_len)]

    def read_byte_array_as_string(self, reg, _len):
        return ''.join(chr(r) for r in self.read_byte_array(reg, _len))

    class create_i2c_property(object):

        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def __call__(self, cls):
            for name, reg_address_and_read_only in self.kwargs.items():
                def i2c_property(reg, read_only=True):
                    def fget(self):
                        return self.read_byte_data(reg)

                    def fset(self, value):
                        return self.write_byte_data(reg, value)
                    return property(fget, None if read_only else fset)
                if (type(reg_address_and_read_only) == int):
                    prop = i2c_property(reg_address_and_read_only)
                else:
                    prop = i2c_property(
                        reg_address_and_read_only[0], **reg_address_and_read_only[1])
                setattr(cls, name, prop)
            return cls


@create_ev3_property(
    brightness={'read_only': False, 'property_type': Ev3IntType},
    trigger={'read_only': False},
    delay_on={'read_only': False, 'property_type': Ev3IntType},
    delay_off={'read_only': False, 'property_type': Ev3IntType}
)
class LEDLight(Ev3Dev):

    def __init__(self, light_path):
        super(Ev3Dev, self).__init__()
        self.sys_path = '/sys/class/leds/' + light_path


class LEDSide (object):

    def __init__(self, left_or_right):
        self.green = LEDLight('ev3:green:%s' % left_or_right)
        self.red = LEDLight('ev3:red:%s' % left_or_right)
        self._color = 0

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self.red.brightness = value & 0x01
        self.green.brightness = (value >> 1) & 0x01
        self._color = value

    def get_operation_lights(self):
        lights = []
        if (self._color & 0x01):
            lights.append(self.red)
        if ((self._color >> 1) & 0x01):
            lights.append(self.green)
        return lights

    def blink(self, color=0, **kwargs):
        if (color != 0):
            self.color = color
        lights = self.get_operation_lights()
        for light in lights:
            light.trigger = 'timer'
            for p, v in kwargs.items():
                setattr(light, p, v)

    def on(self):
        lights = self.get_operation_lights()
        for light in lights:
            light.trigger = 'none'
            light.brightness = 1

    def off(self):
        lights = self.get_operation_lights()
        for light in lights:
            light.trigger = 'none'
            light.brightness = 0


class LED(object):

    class COLOR:
        RED = 1
        GREEN = 2
        AMBER = 3

    left = LEDSide('left')
    right = LEDSide('right')


@create_ev3_property(
    tone={'read_only': False},
    mode={'read_only': True},
    volume={'read_only': False, 'property_type': Ev3IntType}
)
class Tone(Ev3Dev):

    def __init__(self):
        super(Ev3Dev, self).__init__()
        self.sys_path = '/sys/devices/platform/snd-legoev3'

    def play(self, frequency, milliseconds=1000):
        self.tone = '%d %d' % (frequency, milliseconds)

    def stop(self):
        self.tone = '0'

import os


class Lcd(object):

    def __init__(self):
        try:
            from PIL import Image, ImageDraw

            SCREEN_WIDTH = 178
            SCREEN_HEIGHT = 128
            HW_MEM_WIDTH = int((SCREEN_WIDTH + 31) / 32) * 4
            SCREEN_MEM_WIDTH = int((SCREEN_WIDTH + 7) / 8)
            LCD_BUFFER_LENGTH = SCREEN_MEM_WIDTH * SCREEN_HEIGHT
            LCD_HW_BUFFER_LENGTH = HW_MEM_WIDTH * SCREEN_HEIGHT
            self._buffer = Image.new(
                "1", (HW_MEM_WIDTH * 8, SCREEN_HEIGHT), "white")
            self._draw = ImageDraw.Draw(self._buffer)
        except ImportError:
            raise NoSuchLibraryError('PIL')

    def update(self):
        f = os.open('/dev/fb0', os.O_RDWR)
        os.write(f, self._buffer.tobytes("raw", "1;IR"))
        os.close(f)

    @property
    def buffer(self):
        return self._buffer

    @property
    def draw(self):
        return self._draw

    def reset(self):
        self._draw.rectangle(
            (0, 0) + self._buffer.size, outline='white', fill='white')


class attach_ev3_keys(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, cls):
        key_const = {}
        for key_name, key_code in self.kwargs.items():
            def attach_key(key_name, key_code):
                def fget(self):
                    buf = self.polling()
                    return self.test_bit(key_code, buf)
                return property(fget)

            setattr(cls, key_name, attach_key(key_name, key_code))
            key_const[key_name.upper()] = key_code
        setattr(cls, 'CODE', Enum(**key_const))
        return cls


import array
import fcntl


@attach_ev3_keys(
    up=103,
    down=108,
    left=105,
    right=106,
    enter=28,
    backspace=14
)
class Key(object):

    def __init__(self):
        pass

    def EVIOCGKEY(self, length):
        return 2 << (14 + 8 + 8) | length << (8 + 8) | ord('E') << 8 | 0x18

    def test_bit(self, bit, bytes):
        # bit in bytes is 1 when released and 0 when pressed
        return not bool(bytes[int(bit / 8)] & 1 << bit % 8)

    def polling(self):
        KEY_MAX = 0x2ff
        BUF_LEN = int((KEY_MAX + 7) / 8)
        buf = array.array('B', [0] * BUF_LEN)
        with open('/dev/input/by-path/platform-gpio-keys.0-event', 'r') as fd:
            ret = fcntl.ioctl(fd, self.EVIOCGKEY(len(buf)), buf)
        if (ret < 0):
            return None
        else:
            return buf

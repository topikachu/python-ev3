from ctypes import *
import ctypes
import os
import sys


__u16 = c_ushort # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 21
__u32 = c_uint # /home/pikachu/arm-2009q1/bin/../arm-none-linux-gnueabi/libc/usr/include/asm-generic/int-ll64.h: 24

FBIOGET_FSCREENINFO = 0x4602
FBIOGET_VSCREENINFO = 0x4600

class struct_fb_fix_screeninfo(Structure):
    pass

struct_fb_fix_screeninfo.__slots__ = [
    'id',
    'smem_start',
    'smem_len',
    'type',
    'type_aux',
    'visual',
    'xpanstep',
    'ypanstep',
    'ywrapstep',
    'line_length',
    'mmio_start',
    'mmio_len',
    'accel',
    'reserved',
]
struct_fb_fix_screeninfo._fields_ = [
    ('id', c_char * 16),
    ('smem_start', c_ulong),
    ('smem_len', __u32),
    ('type', __u32),
    ('type_aux', __u32),
    ('visual', __u32),
    ('xpanstep', __u16),
    ('ypanstep', __u16),
    ('ywrapstep', __u16),
    ('line_length', __u32),
    ('mmio_start', c_ulong),
    ('mmio_len', __u32),
    ('accel', __u32),
    ('reserved', __u16 * 3),
]

fb_fix_screeninfo = struct_fb_fix_screeninfo # /home/pikachu/ev3/ev3sources/extra/linux-03.20.00.13/include/linux/fb.h: 154


# /home/pikachu/ev3/ev3sources/extra/linux-03.20.00.13/include/linux/fb.h: 237
class struct_fb_var_screeninfo(Structure):
    pass

struct_fb_var_screeninfo.__slots__ = [
    'xres',
    'yres',
    'xres_virtual',
    'yres_virtual',
    'xoffset',
    'yoffset',
    'bits_per_pixel',
    'grayscale',
    'red',
    'green',
    'blue',
    'transp',
    'nonstd',
    'activate',
    'height',
    'width',
    'accel_flags',
    'pixclock',
    'left_margin',
    'right_margin',
    'upper_margin',
    'lower_margin',
    'hsync_len',
    'vsync_len',
    'sync',
    'vmode',
    'rotate',
    'reserved',
]


# /home/pikachu/ev3/ev3sources/extra/linux-03.20.00.13/include/linux/fb.h: 184
class struct_fb_bitfield(Structure):
    pass

struct_fb_bitfield.__slots__ = [
    'offset',
    'length',
    'msb_right',
]
struct_fb_bitfield._fields_ = [
    ('offset', __u32),
    ('length', __u32),
    ('msb_right', __u32),
]

struct_fb_var_screeninfo._fields_ = [
    ('xres', __u32),
    ('yres', __u32),
    ('xres_virtual', __u32),
    ('yres_virtual', __u32),
    ('xoffset', __u32),
    ('yoffset', __u32),
    ('bits_per_pixel', __u32),
    ('grayscale', __u32),
    ('red', struct_fb_bitfield),
    ('green', struct_fb_bitfield),
    ('blue', struct_fb_bitfield),
    ('transp', struct_fb_bitfield),
    ('nonstd', __u32),
    ('activate', __u32),
    ('height', __u32),
    ('width', __u32),
    ('accel_flags', __u32),
    ('pixclock', __u32),
    ('left_margin', __u32),
    ('right_margin', __u32),
    ('upper_margin', __u32),
    ('lower_margin', __u32),
    ('hsync_len', __u32),
    ('vsync_len', __u32),
    ('sync', __u32),
    ('vmode', __u32),
    ('rotate', __u32),
    ('reserved', __u32 * 5),
]

fb_var_screeninfo = struct_fb_var_screeninfo # /home/pikachu/ev3/ev3sources/extra/linux-03.20.00.13/include/linux/fb.h: 237
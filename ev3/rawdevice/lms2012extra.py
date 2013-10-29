from ctypes import sizeof

from . import lms2012


#modify from https://raw.github.com/SpliFF/python-ioctl/master/ioctl.py
NRBITS = 8
TYPEBITS = 8

# may be arch dependent

SIZEBITS = 14
DIRBITS = 2

NRMASK = (1 << NRBITS) - 1
TYPEMASK = (1 << TYPEBITS) - 1
SIZEMASK = (1 << SIZEBITS) - 1
DIRMASK = (1 << DIRBITS) - 1

NRSHIFT = 0
TYPESHIFT = NRSHIFT + NRBITS
SIZESHIFT = TYPESHIFT + TYPEBITS
DIRSHIFT = SIZESHIFT + SIZEBITS

# may be arch dependent

NONE = 0x0
WRITE = 0x1
READ = 0x2

# for the drivers/sound files...

IN = WRITE << DIRSHIFT
OUT = READ << DIRSHIFT
INOUT = (WRITE | READ) << DIRSHIFT
IOCSIZE_MASK = SIZEMASK << SIZESHIFT
IOCSIZE_SHIFT = SIZESHIFT

# used to create numbers ...

def _IO( _type, nr):
    return _IOC(NONE, _type, nr, 0)

def _IOC(direction, _type, nr, tt):
    
    return (direction << DIRSHIFT) | (ord(_type) << TYPESHIFT) | (nr << NRSHIFT) | (  sizeof(tt) << SIZESHIFT)

def _IOR( _type, nr, tt):
    return _IOC(READ, _type, nr, tt)

def IOW(_type, nr, tt):
    return _IOC(WRITE, _type, nr, tt)

def _IOWR(_type, nr, tt):
    return _IOC(READ|WRITE, _type, nr, tt)

def _IOR_BAD(_type, nr, tt):
    return _IOC(READ, _type, nr, tt)

def _IOW_BAD(_type, nr, tt):
    return _IOC(WRITE, _type, nr, tt)

def _IOWR_BAD(_type, nr, tt):
    return _IOC(READ|WRITE, _type, nr, tt)

# used to decode ioctl numbers..

def DIR(nr):
    return (nr >> DIRSHIFT) & DIRMASK

def TYPE(nr):
    return (nr >> TYPESHIFT) & TYPEMASK

def NR(nr):
    return (nr >> NRSHIFT) & NRMASK

def SIZE(nr):
    return (nr >> SIZESHIFT) & SIZEMASK

UART_SET_CONN       =   _IOWR('u',0,lms2012.DEVCON)
UART_READ_MODE_INFO =   _IOWR('u',1,lms2012.UARTCTL)
UART_NACK_MODE_INFO =   _IOWR('u',2,lms2012.UARTCTL)
UART_CLEAR_CHANGED  =   _IOWR('u',3,lms2012.UARTCTL)


IIC_SET_CONN        =   _IOWR('i',2,lms2012.DEVCON)
IIC_READ_TYPE_INFO  =   _IOWR('i',3,lms2012.IICCTL)
IIC_SETUP           =   _IOWR('i',5,lms2012.IICDAT)
IIC_SET             =   _IOWR('i',6,lms2012.IICSTR)


TST_PIN_ON          =   _IOWR('t',1,lms2012.TSTPIN)
TST_PIN_OFF         =   _IOWR('t',2,lms2012.TSTPIN)
TST_PIN_READ        =   _IOWR('t',3,lms2012.TSTPIN)
TST_PIN_WRITE       =   _IOWR('t',4,lms2012.TSTPIN)


TST_UART_ON         =   _IOWR('t',5,lms2012.TSTUART)
TST_UART_OFF        =   _IOWR('t',6,lms2012.TSTUART)
TST_UART_EN         =   _IOWR('t',7,lms2012.TSTUART)
TST_UART_DIS        =   _IOWR('t',8,lms2012.TSTUART)
TST_UART_READ       =   _IOWR('t',9,lms2012.TSTUART)
TST_UART_WRITE      =   _IOWR('t',10,lms2012.TSTUART)

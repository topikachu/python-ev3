from . import lms2012
from ctypes import sizeof

def _IOWR(ch, i, typ):
    return (3 << 30) | (ord(ch) << 8) | i | (sizeof(typ) << 16)

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

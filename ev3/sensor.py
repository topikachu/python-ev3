from rawdevice import uartdevice
from rawdevice import analogdevice
import time
class UartSensor(object):
    
    def __init__ (self,port):
        self.port=port
        uartdevice.reset(port)
    def set_mode(self,mode,delay=0):
        time.sleep(delay)
        self.mode=mode
        uartdevice.set_mode(self.port,mode)
    
    def get_value(self):
        return uartdevice.get_value_byte(self.port)
    def get_value_bytes(self):
        return uartdevice.get_value_bytes(self.port)
    def reset(self):
        uartdevice.reset(self.port)
        
        
class AnalogSensor(object):
    def __init__(self,port):
        self.port=port
        analogdevice.clear_change(port)
    def get_pin1_value(self):
        return analogdevice.get_pin1(self.port)
        
    def get_pin6_value(self):
        return analogdevice.get_pin6(self.port)
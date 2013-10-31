from rawdevice import uartdevice
class UartSensor(object):
    
    def __init__ (self,port):
        self.port=port
        uartdevice.reset(port)
        self.set_mode(0)
    def set_mode(self,mode):
        self.mode=mode
        uartdevice.set_mode(self.port,mode)
    def getValue(self):
        return uartdevice.get_value_byte(self.port)
    def get_value_bytes(self):
        return uartdevice.get_value_bytes(self.port)
    def reset(self):
        uartdevice.reset(self.port)
from rawdevice import uartdevice


import sensor
class EV3ColorSensor(sensor.UartSensor):

    NONE=0
    BLACK=1
    BLUE=2
    GREEN=3 
    YELLOW=4 
    RED=5
    WHITE=6 
    BROWN=7

    def __init__ (self,port):
        self.port=port
        super(EV3ColorSensor, self).__init__(port)
    def set_reflect_mode(self):
        self.set_mode(0)
    def set_ambient_mode(self):
        self.set_mode(1)
    def set_color_mode(self):
        self.set_mode(2)
    def set_ref_raw_mode(self):
        self.set_mode(3)
    def set_rgb_raw_mode(self):
        self.set_mode(4)
    def set_col_cal_mode(self)    :
        self.set_mode(5)
    
    def color_to_string(self):
        print self.getValue()
        return ["NONE","BALCK","BLUE","GREEN","YELLOW","RED","WHITE","BROWN"][self.getValue()]


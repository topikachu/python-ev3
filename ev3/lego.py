import sensor
from rawdevice import lms2012


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
        return ["NONE","BLACK","BLUE","GREEN","YELLOW","RED","WHITE","BROWN"][self.get_value()]

class EV3IRSensor(sensor.UartSensor):
    BUTTON_TOP_LEFT = 1
    BUTTON_BOTTOM_LEFT =2
    BUTTON_TOP_RIGHT =3
    BOTTOM_RIGHT =4
    BUTTON_TOP_LEFT_TOP_RIGHT = 5
    BUTTON_TOP_LEFT_BOTTOM_RIGHT=6
    BOTTOM_LEFT_TOP_RIGHT = 7
    BOTTOM_LEFT_BOTTOM_RIGHT = 8
    BUTTON_CENTRE_BEACON=9
    BOTTOM_LEFT_TOP_LEFT=10
    BUTTON_TOP_RIGHT_BOTTOM_RIGHT=11
    
    CHANNEL_1 = 0
    CHANNEL_2 = 1
    CHANNEL_3 = 2
    CHANNEL_4 = 3
    
    
    def __init__ (self,port):
        self.port=port
        super(EV3IRSensor,self).__init__(port)
    def set_prox_mode(self):
        self.set_mode(0)
    def set_seek_mode(self):
        self.set_mode(1)
    def set_remote_mode(self):
        self.set_mode(2)     
    
    
    def get_distance(self):
        """
        use in prox mode
        """                    
        return self.get_value()
    
    def get_remote_command(self,chan=0):
        """
        use in remote mode
        """
        return self.get_value_bytes()[chan]
        
    def get_direction_and_distance(self,chan=0):
        """
        use in seek mode
        """
        return self.get_all_direction_and_distance()[chan]
        
    def get_all_direction_and_distance(self):
        """
        use in seek mode
        """
        allchannels=self.get_value_bytes()[0:8]
        i = 0
        values=[]
        while (i<4):
            values.append((allchannels[i*2],allchannels[i*2+1]) )
            i+=1
        return values
    
class EV3TouchSensor(sensor.AnalogSensor):
    def __init__ (self,port):
        self.port=port
        super(EV3TouchSensor,self).__init__(port)
    def is_pressed(self):
        return self.get_pin6_value()> lms2012.ADC_REF/2
    
class EV3Motor():
    pass
    
        


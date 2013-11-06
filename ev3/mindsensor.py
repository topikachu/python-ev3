import sensor
import functools

class PSP(sensor.IICSensor):

    __command_map={"button_set_1":0x42,
                   "button_set_2":0x43,
                   "x_left":0x44,
                   "y_left":0x45,
                   "x_right":0x46,
                   "y_right":0x47,
                   "up":0x4A,
                   "right":0x4B,
                   "down":0x4C,
                   "left":0x4D,
                   "l2":0x4E,
                   "r2":0x4F,
                   "l1":0x50,
                   "r1":0x51,
                   "triangle" :0x52,
                   "circle":0x52,
                   "cross":0x53,
                   "square":0x54,

                   }


    def __init__ (self,port,address=0x02):
        self.port=port
        super(PSP, self).__init__(port,address)
        self.command(0x41, 0x49) #Initialize the Playstation 2 Wireless Receiver dongle (attached to PSP-Nx)
    def read_value(self,button):
        register=PSP.__command_map[button]
        return self.read_single_byte(register)&0xff
    def __getattr__(self, attrName):        
        return functools.partial(self.read_value, attrName[len("get_"):])

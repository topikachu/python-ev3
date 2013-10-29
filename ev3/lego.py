from rawdevice import uartdevice


class EV3ColorSensor():

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
    def set_mode(self,mode):
        self.mode=mode
        uartdevice.set_mode(self.port,mode)
    def setReflectMode(self):
        self.set_mode(0)
    def setAmbientMode(self):
        self.set_mode(1)
    def setColorMode(self):
        self.set_mode(2)
    def setRefRAWMode(self):
        self.set_mode(3)
    def setRGBRAWMode(self):
        self.set_mode(4)
    def setColCalMode(self)    :
        self.set_mode(5)
    def getValue(self):
        return uartdevice.get_value_byte(self.port)
    def colorToString(self):
        return ["NONE","BALCK","GREEN","YELLOW","RED","WHITE","BROWN"][self.getValue()]


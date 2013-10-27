from rawdevice import UARTDevice
from rawdevice import AnalogDevice
from rawdevice import MotorDevice

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
    def setMode(self,mode):
        self.mode=mode
        UARTDevice.setMode(self.port,mode)
    def setReflectMode(self):
        self.setMode(0)
    def setAmbientMode(self):
        self.setMode(1)
    def setColorMode(self):
        self.setMode(2)
    def setRefRAWMode(self):
        self.setMode(3)
    def setRGBRAWMode(self):
        self.setMode(4)
    def setColCalMode(self)    :
        self.setMode(5)
    def getValue(self):
        return UARTDevice.getValueByte(self.port)
    def colorToString(self):
        return ["NONE","BALCK","GREEN","YELLOW","RED","WHITE","BROWN"][self.getValue()]


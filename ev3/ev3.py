import threading
import time

from rawdevice import analogdevice, dcm, iicdevice, lcd, motordevice, sound, uartdevice, ui, lms2012

_AMP_CIN= 22.0 
_AMP_VIN  =  0.5
_VCE  =   0.05
_SHUNT_IN     =   0.11  
_AMP_COUT  =       19.0  
_SHUNT_OUT   =    0.055

pollingThread=None
events={}

SENSOR_1 = 0
SENSOR_2 = 1
SENSOR_3 = 2
SENSOR_4 = 3

MOTOR_A=0
MOTOR_B=1
MOTOR_C=2
MOTOR_D=3

MOTOR_A_BIT=1
MOTOR_B_BIT=2
MOTOR_C_BIT=4
MOTOR_D_BIT=8


def open_all_device():
    analogdevice.open_device()
    dcm.open_device()
    iicdevice.open_device()
    lcd.open_device()
    motordevice.open_device()
    sound.open_device()
    uartdevice.open_device()
    ui.open_device()
    
    for port in range(0,4):
        analogdevice.clear_change(port)
        uartdevice.reset(port)
        iicdevice.reset(port)
    
def close_all_device():
    ui.close_device()
    uartdevice.close_device()
    sound.close_device()
    motordevice.close_device()
    lcd.close_device()    
    iicdevice.close_device()
    dcm.close_device()
    analogdevice.close_device()

def start():
    global pollingThread
    pollingThread=Polling()
    pollingThread.daemon = True
    pollingThread.start()

def convert(val):
    return float(val)*lms2012.ADC_REF/lms2012.ADC_RES;

def get_battery():
    CinV = lms2012.CtoV(float(analogdevice.get_analog().BatteryCurrent))/_AMP_CIN
    battery_v = lms2012.CtoV(float(analogdevice.get_analog().Cell123456))/_AMP_VIN + CinV + _VCE
    battery_i = CinV / _SHUNT_IN;
    motor_i = lms2012.CtoV(float(analogdevice.get_analog().MotorCurrent)/_AMP_COUT)/_SHUNT_OUT
    return battery_v,battery_i,motor_i



       

def registerEvent(predicate,handle):
    events[predicate]=handle



class Polling(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
 
    def run(self):
        while True:
            for predicate,handle in events.iteritems():
                if predicate():
                    handle()
            time.sleep(0)




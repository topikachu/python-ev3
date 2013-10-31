import threading
import time

from rawdevice import analogdevice, dcm, iicdevice, lcd, motordevice, sound, uartdevice, ui


pollingThread=None
events={}

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
    ui.open_device()
    uartdevice.open_device()
    sound.open_device()
    motordevice.open_device()
    lcd.open_device()    
    iicdevice.open_device()
    dcm.open_device()
    analogdevice.open_device()

def start():
    global pollingThread
    pollingThread=Polling()
    pollingThread.daemon = True
    pollingThread.start()



def registerEvent(predicate,handle):
    events[predicate]=handle

def close_device():
    motordevice.close_device()
    uartdevice.close_device()
    analogdevice.close_device()

class Polling(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
 
    def run(self):
        while True:
            for predicate,handle in events.iteritems():
                if predicate():
                    handle()
            time.sleep(0)


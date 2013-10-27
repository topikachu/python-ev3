from rawdevice import *
import threading
import time
pollingThread=None
events={}

def init():
    AnalogDevice.init()
    UARTDevice.init()
    MotorDevice.init()
    for port in range(0,4):
        AnalogDevice.clearChange(port)
        UARTDevice.clearChange(port)
    

def start():
    global pollingThread
    pollingThread=Polling()
    pollingThread.daemon = True
    pollingThread.start()



def registerEvent(predicate,handle):
    events[predicate]=handle

def close():
    MotorDevice.close()
    UARTDevice.close()
    AnalogDevice.close()

class Polling(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
 
    def run(self):
        while True:
            for predicate,handle in events.iteritems():
                if predicate():
                    handle()
            time.sleep(0)


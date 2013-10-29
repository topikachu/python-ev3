import threading
import time

from rawdevice import analogdevice, uartdevice, motordevice


pollingThread=None
events={}

def open_device():
    analogdevice.open_device()
    uartdevice.open_device()
    motordevice.open_device()
    for port in range(0,4):
        analogdevice.clear_change(port)
        uartdevice.clear_change(port)
    

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


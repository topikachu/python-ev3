import threading
import time

from rawdevice import *


pollingThread=None
events={}

def open():
    analogdevice.open()
    uartdevice.open()
    motordevice.open()
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

def close():
    motordevice.close()
    uartdevice.close()
    analogdevice.close()

class Polling(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
 
    def run(self):
        while True:
            for predicate,handle in events.iteritems():
                if predicate():
                    handle()
            time.sleep(0)


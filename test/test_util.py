import datetime
import time
def _dumy():
    pass
def count_down(sec,f=_dumy):
    while (sec>0):
        print sec
        f()
        time.sleep(1)
        sec-=1

def wait(sec,f=_dumy):
    timeout=datetime.datetime.now()+datetime.timedelta(seconds=sec)
    while True:
        f()
        if datetime.datetime.now()>timeout:
            break
        #time.sleep(1)
                
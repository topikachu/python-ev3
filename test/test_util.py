import time
def _dumy():
    pass
def count_down(sec,f=_dumy):
    while (sec>0):
        print sec
        f()
        time.sleep(1)
        sec-=1
        
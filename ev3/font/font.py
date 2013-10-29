import array
import mmap
import os
import re

import ev3.font


fontfile = os.path.join(ev3.__path__[0],'font', 'wenquanyi_12pt.bdf')
size = os.stat(fontfile).st_size
f = open(fontfile)
data = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)
def get_font(c):
    point=ord(c)
    p=re.compile(r"ENCODING %d.*?BITMAP(.*?)ENDCHAR" % point,re.S|re.M)
    m = p.search(data)
    if m:
        result=array.array('B')
        s= m.group(1)
        width=0
        height=0
        for l in s.splitlines():
            if (len(l.strip())==0):
                continue
            line = array.array('B', l.decode("hex"))
            width=8*len(line)
            result += array.array('B', l.decode("hex"))
            height+=1
        return result,width,height



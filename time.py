#!/usr/bin/python



import time;
vartick=time.time()
print(vartick)

import time;
localtime=time.localtime(time.time())
print(localtime)


import time;
localtime=time.asctime(time.localtime(time.time()))
print(localtime)


import calendar
cal2=calendar.month(2018,9)
print(cal2)

import time
print("staring time %s"%time.ctime())
time.sleep(2)
print("ending time %s"%time.ctime())

import time
import os
os.environ['Tolk;Z'] = 'CST+6CDT,M3.2.0,M11.1.0'
time.tzset()
print(time.strftime('%X %x %Z'))

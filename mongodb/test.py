# -*- coding: UTF-8 -*-
import pytz
import time
import datetime
from pytz import all_timezones



print(all_timezones)

#print datetime.datetime.now(sh)

print pytz.country_timezones('us')

#print datetime.datetime(2009,2,21,8,10,0,tzinfo=sh)
#print new
utc = pytz.utc
boston = pytz.timezone("Etc/GMT")
newyork = pytz.timezone("Etc/GMT+0")


origin1 = datetime.datetime(2009, 3, 23, 0, 0, 0, tzinfo=boston)
origin2 = datetime.datetime(2009, 3, 23, 0, 0, 0, tzinfo=newyork)
print origin1
print origin2
new1 = origin1.astimezone(utc)
new2 = origin2.astimezone(utc)
print new1
print new2


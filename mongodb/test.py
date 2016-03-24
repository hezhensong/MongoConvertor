# -*- coding: UTF-8 -*-
import pytz
import time
import datetime
from pytz import all_timezones
from TimeZoneUtil import TimeZoneUtil

test = [''] * 10
print(test)
print(len(test))

print len(TimeZoneUtil.timezoneMap)
print TimeZoneUtil.gettimezone('516a35427dbbf72336000003',2016, 3, 24, 10, 42, 0)

test = {'1':'a','2':'b'}
print test['1']
#print datetime.datetime.now(sh)

print pytz.country_timezones('us')

#print datetime.datetime(2009,2,21,8,10,0,tzinfo=sh)
#print new
utc = pytz.utc
boston = pytz.timezone("Etc/GMT+5")
newyork = pytz.timezone("America/New_York")


origin1 = datetime.datetime(2016, 3, 24, 10, 42, 0, tzinfo=boston)
origin2 = datetime.datetime(2009, 3, 24, 10, 42, 0, tzinfo=newyork)
print origin1
print origin2
new1 = origin1.astimezone(utc)
new2 = origin2.astimezone(utc)
print new1
print new2


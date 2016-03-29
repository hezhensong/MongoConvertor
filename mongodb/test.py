# -*- coding: UTF-8 -*-
import pytz
import time
import datetime
from pytz import all_timezones
from TimeZoneUtil import TimeZoneUtil
from bson.objectid import ObjectId

test = [''] * 10
print(test)
print(len(test))

print len(TimeZoneUtil.timezoneMap)
#print TimeZoneUtil.gettimezone('516a35427dbbf72336000003',2016, 3, 24, 10, 42, 0)

test = {'1':'a','2':'b'}
print test['1']
#print datetime.datetime.now(sh)

print pytz.country_timezones('us')

#print datetime.datetime(2009,2,21,8,10,0,tzinfo=sh)
#print new
utc = pytz.utc
boston = pytz.timezone("Etc/GMT-8")
newyork = pytz.timezone("America/New_York")


origin1 = datetime.datetime(2016, 3, 24, 19, 0, 0, tzinfo=pytz.utc)
print origin1
origin2 = datetime.datetime(2009, 3, 24, 14, 0, 0, tzinfo=newyork)
#print origin2
print origin1
#print origin2
#new1 = origin1.astimezone(utc)
new2 = origin2.astimezone(utc)
#print new1
print new2

temp1 = {'type': 0, 'name': u'\u5468\u8fb9'}
temp2 = {'type': 0, 'name': u'\u5468\u8fb9'}
temp3 = {'type': 0, 'name': u'\u5468\u8fb9'}


temp4 = {'name':'米其林' ,'type':0}
temp5 = {'name':'米其林' ,'type':0}
temp6 = {'name':'米其林' ,'type':0}

temp_array = []
if temp_array.count(temp1) == 0:
    temp_array.append(temp1)
    
if temp_array.count(temp2) == 0:
    temp_array.append(temp2)
    
if temp_array.count(temp3) == 0:
    temp_array.append(temp3)
print temp_array

test = 'abc*'
print test.find('*')


test = [{'a':1},{'b':2}]
print type(test)



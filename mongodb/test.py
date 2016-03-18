# -*- coding: UTF-8 -*-

import time
import datetime

a = '20150430'
b = '17'
year = int(a[0:4])
month = int(a[4:6])
day = int(a[6:8])
print year
print month
print day
print datetime.datetime(year,month,day,4)

test = 'this'
print(type(test))


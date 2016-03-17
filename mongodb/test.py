# -*- coding: UTF-8 -*-

import time
import datetime

a = '1458038390723'
b = float(a) / 1000
x = time.localtime(b)  
y,m,d,h,mm,s = x[0:6]

print(datetime.datetime(y,m,d,h,mm,s))


test = 'Tue, 15 Mar 2016 11:00 am CET'
test2 = 'Tue, 15 Mar 2016 11:00 am CEMT'
print(len(test))
print(len(test2))
m = test2[0:21]
print(m)
print(len(m))
test = time.strptime(m, "%a, %d %b %Y %H:%M")
print(test[0:6])


str = '2015年0月1日'

a1 = str.find('光')
if a1 != 0:
    print("OK")
print(a1)
a2 = str.index('月')
a3 = str.index('日')
year = str[0:a1]
month = str[a1+3:a2]
day = str[a2+3:a3]
print(year)
print(month)
print(day)

    

#print(type(str))
#l = time.strptime(str,"%Y年%m月%d日")[0:3]
#print(l)
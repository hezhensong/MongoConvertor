import time
import datetime

a = '1458038390723'
b = float(a) / 1000
x = time.localtime(b)  
y,m,d,h,mm,s = x[0:6]
print(datetime.datetime(y,m,d,h,mm,s))


test = 'Tue, 15 Mar 2016 11:00 am CET'
test2 = 'Tue, 15 Mar 2016 11:00 am CEMT'
m = test[0:len(test)-7]
print(m)
print(len(m))
test = time.strptime(m, "%a, %d %b %Y %H:%M")
print(test[0:6])
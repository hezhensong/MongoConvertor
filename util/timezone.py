#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime

import pytz as pytz

tz = pytz.timezone('Asia/Shanghai')
time = datetime.datetime(2009, 2, 21, 7, 16, 41, 843000, tzinfo=tz)

print time.ctime()

tzus = pytz.timezone('Asia/Shanghai')
utc = pytz.utc
print utc.normalize('utc', time.astimezone())

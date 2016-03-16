import json
import datetime
import time

ts = time.time()

print(ts)
isodate = datetime.datetime.fromtimestamp(ts,None)
print(isodate)
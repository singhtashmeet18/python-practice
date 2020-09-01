import time
ticks = time.time()        #time in seconds since 1 jan,1970
print (ticks)
print ("number of ticks since 12:00am,january 1, 1970:", ticks)
import time;
localtime = time.localtime(time.time())
print = ("local current time:", localtime)

import calendar
cal = calendar.month(2020,6)
print (cal)
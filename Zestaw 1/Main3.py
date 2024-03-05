# code that shows current time

import time
import datetime

while(1):
    now = datetime.datetime.now()
    string = "<"
    if (now.second < 10):
        print(">"+str(now.hour) + ":" + str(now.minute) + ":0" + str(int(now.second)) +str("<"))
    else:
        print(">"+str(now.hour) + ":" + str(now.minute) + ":" + str(int(now.second)) +str("<"))
    time.sleep(1)
#!/usr/bin/env python

<other imports>
import time 

def shutdown():
    subprocess.call( <shutdown command> )

GPIO.add_event_detect(3, GPIO.FALLING, shutdown)
GPIO.add_event_detect(4, GPIO.FALLING, shutdown)

while True:
    time.sleep(0.010)

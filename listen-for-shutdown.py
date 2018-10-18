#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.wait_for_edge(3, GPIO.FALLING)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.wait_for_edge(4, GPIO.FALLING)

def shutdown():
subprocess.call(['shutdown', '-h', 'now'], shell=False)

GPIO.add_event_detect(3, GPIO.FALLING, shutdown)
GPIO.add_event_detect(4, GPIO.FALLING, shutdown)

while True:
    time.sleep(0.010)

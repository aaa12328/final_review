#!/usr/bin/env python3
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
	if (GPIO.input(4)==1):
		print('Turn on the switch')
		time.sleep(1)
	if(GPIO.input(4)==0):
		print('Turn off the switch')
		time.sleep(1)
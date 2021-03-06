#!/usr/bin/python
import time
import sys
import httplib, urllib
import json
deviceId = "DtvT7uGl"
deviceKey = "jmdwKi5yMbc3ckFb"
def post_to_mcs(payload):
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = httplib.HTTPConnection("api.mediatek.com:80")
			conn.connect() 
			not_connected = 0 
		except (httplib.HTTPException, socket.error) as ex: 
			print ("Error: %s" % ex)
			time.sleep(10)
			 # sleep 10 seconds 
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close()  

import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    DataSwitch=GPIO.input(4)
    if(DataSwitch ==1):
        print('Button pressed')
    else:
        print('botton released')
    payload = {"datapoints":[{"dataChnId":"DataSwitch","values":{"value":DataSwitch}}]} 
    post_to_mcs(payload)

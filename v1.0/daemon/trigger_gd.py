#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#led24 = 24
gpio_door = 11

#GPIO.setup(led24, GPIO.OUT)
GPIO.setup(gpio_door, GPIO.OUT)
#GPIO.setup(led24, GPIO.IN) 

wait_time = 0.5

start = 1
end = 2
while(start < end):
	#GPIO.output(led24, 1)
	GPIO.output(gpio_door, 1)
	time.sleep(wait_time)

	#GPIO.output(led24, 0)
	GPIO.output(gpio_door, 0)
	#time.sleep(wait_time)
        start = start + 1
GPIO.cleanup()

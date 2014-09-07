#!/usr/bin/python

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
gpio11 = 11 #Garage Door Down
gpio13 = 13 #Garage Door up
gpio16 = 16 #Door
gpio18 = 18 #Door

#GPIO.setup(gpio12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gpio11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gpio13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gpio16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gpio18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def printMag(channel):
        print("Mag intact.")
	print(channel)


#GPIO.add_event_detect(gpio12, GPIO.RISING, callback=printMag, bouncetime=100)
#GPIO.add_event_detect(gpio11, GPIO.RISING, callback=printMag, bouncetime=1000)
#GPIO.add_event_detect(gpio13, GPIO.RISING, callback=printMag, bouncetime=1000)

def write_logs(my_str):
	file = open("/var/www/door.log", "w+")
	file.write(my_str)
	file.close()

gd_open_state = 1 
gd_closed_state = 1

g_to_porch_state = 1
g_to_kitchen_state = 1

gd_open_string = "Garage Door is <b>Open</b>. </br>"
gd_closed_string = "Garage Door is <b>Closed</b>. </br>"
gd_moving_string = "Garage Door <b>moving</b>. </br>"

door_to_porch_closed_string = "Door from garage to porch is <b>Closed</b>. </br>"
door_to_porch_open_string = "Door  from garage to porch is <b>open</b>. </br>"
door_from_garage_to_kitcken_open_str = "Door from kitchen to garage is <b>open</b>. </br>"
door_from_garage_to_kitchen_closed_str = "Door from kitchen to garage is <b>Closed</b>. </br>"

while(1):
        time.sleep(0.6)
#	print chr(27) + "[2J"
	str_to_write = ""
	write_out_logs = 0

	if (GPIO.input(gpio11) == 0 and GPIO.input(gpio13) == 0):
#		print("GarageDoor moving.")
		str_to_write = str_to_write + gd_moving_string
	elif (GPIO.input(gpio11) == 1):
#		print("GarageDoor is Closed.")
		str_to_write = str_to_write + gd_closed_string
	elif (GPIO.input(gpio13) == 1):
#		print("GarageDoor is Open.")
		str_to_write = str_to_write + gd_open_string

	if (GPIO.input(gpio16) == 1):
#		print("Door from kitchen to garage is Closed.")
		str_to_write = str_to_write + door_from_garage_to_kitchen_closed_str
	else:
#		print("Door from kitchen to garage is open.")
		str_to_write = str_to_write + door_from_garage_to_kitcken_open_str
        if (GPIO.input(gpio18) == 1):
 #               print("Door from garage to porch is Closed.")
		str_to_write = str_to_write + door_to_porch_closed_string
	else:
#		print("Door  from garage to porch is open.")
		str_to_write = str_to_write + door_to_porch_open_string 

	#States and logs
	if (GPIO.input(gpio11) != gd_closed_state ):
		write_out_logs = 1
		gd_closed_state = GPIO.input(gpio11)
	elif ( GPIO.input(gpio13) != gd_open_state ):
		write_out_logs = 1 
		gd_open_state = GPIO.input(gpio13)
	elif ( GPIO.input(gpio16) != g_to_kitchen_state ):
		write_out_logs = 1
		g_to_kitchen_state = GPIO.input(gpio16)
	elif ( GPIO.input(gpio18) != g_to_porch_state ):
		write_out_logs = 1
		g_to_porch_state = GPIO.input(gpio18)
		

	if (write_out_logs == 1):
#		print("Writing to logs.")
		write_logs(str_to_write)

GPIO.cleanup()


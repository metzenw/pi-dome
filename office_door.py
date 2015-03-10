#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from subprocess import call
import os
GPIO.setmode(GPIO.BOARD) #Pin number
#GPIO.setmode(GPIO.BCM)
MAG1 = 7 #Office door

GPIO.setup(MAG1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#time.sleep(1)
#GPIO.output(MAG1, False)

office_door = 1
played = 1

while(1):
    time.sleep(0.6)
    if (GPIO.input(MAG1) == 1):
        print("Office Door Closed.")
        if played == 0:
            #call("ssh", "odroid@192.168.1.9 mplayer /home/odroid/door1.ogg")
            os.system("ssh odroid@192.168.1.9 mplayer /home/odroid/byedude.wav")
            #os.system("ssh odroid@192.168.1.9 mplayer /home/odroid/door1.ogg")
            played = 1
    if (GPIO.input(MAG1) == 0):
         print("Office Door Open.")
         if played == 1:
            #os.system("ssh odroid@192.168.1.9 mplayer /home/odroid/door1.ogg")
            os.system("ssh odroid@192.168.1.9 mplayer /home/odroid/welcome1.wav")
            #os.system("ssh odroid@192.168.1.9 mplayer /home/odroid/welcome1.wav")
            played = 0

#ssh odroid@192.168.1.9 mplayer /home/odroid/storm.wav
#ssh odroid@192.168.1.9 mplayer /home/odroid/door1.ogg

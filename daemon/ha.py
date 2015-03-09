#!/usr/bin/env python

import sys, time, signal 
import RPi.GPIO as GPIO
from daemon import Daemon

#s_log = open("/tmp/home_automation.log", "a")
#s_log.write("Opening Log file")

class MyDaemon(Daemon):
   def run(self):
      GPIO.setmode(GPIO.BOARD)
      gpio11 = 12 #Garage Door Down
      gpio13 = 16 #Garage Door up
      gpio16 = 18 #Door Kitchen
      gpio18 = 15 #Door Porch

      #GPIO.setup(gpio12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      def printMag(channel):
         self.logger.write("INFO:   Mag intact:   " + channel)

      def write_logs(my_str):
         file = open("/var/www/door.log", "w+", 0)
         file.write(my_str)
         sys.stdout.flush()
         sys.stderr.flush()
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

      #While loop
      while True:
         time.sleep(0.5)
         #self.logger.write("INFO:   Daemon running....\n")
         str_to_write = ""
         write_out_logs = 0

         if (GPIO.input(gpio11) == 0 and GPIO.input(gpio13) == 0):
            #print("GarageDoor moving.")
            str_to_write = str_to_write + gd_moving_string
         elif (GPIO.input(gpio11) == 1):
            #print("GarageDoor is Closed.")
            str_to_write = str_to_write + gd_closed_string
         elif (GPIO.input(gpio13) == 1):
            #print("GarageDoor is Open.")
            str_to_write = str_to_write + gd_open_string
         if (GPIO.input(gpio16) == 1):
            #print("Door from kitchen to garage is Closed.")
            str_to_write = str_to_write + door_from_garage_to_kitchen_closed_str
         else:
            #print("Door from kitchen to garage is open.")
            str_to_write = str_to_write + door_from_garage_to_kitcken_open_str
         if (GPIO.input(gpio18) == 1):
            #print("Door from garage to porch is Closed.")
            str_to_write = str_to_write + door_to_porch_closed_string
         else:
            #print("Door  from garage to porch is open.")
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
            #print("Writing to logs.")
            write_logs(str_to_write)

if __name__ == "__main__":
   daemon = MyDaemon('/var/run/home_automation.pid')
   if len(sys.argv) == 2:
      if 'start' == sys.argv[1]:
         daemon.start()
      elif 'stop' == sys.argv[1]:
         daemon.stop()
      elif 'restart' == sys.argv[1]:
         daemon.restart()
      else:
         print "Unknown command"
         print sys.argv[1]
         sys.exit(2)
         sys.exit(0)
   else:
      daemon.start()

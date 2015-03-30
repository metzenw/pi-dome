#!/usr/bin/env python

import sys, time, signal 
import RPi.GPIO as GPIO
from daemon import Daemon
import datetime

#s_log = open("/tmp/home_automation.log", "a")
#s_log.write("Opening Log file")

class MyDaemon(Daemon):
   def run(self):
      GPIO.setmode(GPIO.BOARD)
      gpio18 = 12 #Garage Door Down
      gpio13 = 16 #Garage Door up
      gpio16 = 18 #Door Kitchen
      gpio22 = 15 #Door Porch
      gpio04 = 7  #Sensor      
      gpio11 = 23 #Front Door motion sensor
      gpio09 = 21 #Fron door door sensor
      gpio08 = 24 #Living room motion sensor

      #GPIO.setup(gpio12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio04, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio09, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.setup(gpio08, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

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

      g_sensor_state = 1
      fd_motion_sensor_state = 1

      #Front door door sensor
      fd_door_sensor = 1
   
      #Livingroom motion sensor 
      lr_motion_sensor_state = 1

      #Livingroom motion text
      lr_audio_active = "<audio controls autoplay><source src=\"foot_steps.ogg\" type=\"audio/ogg\"></audio>"
      lr_active_string = "Living room sensor <b>Active</b>. </br>" + lr_audio_active
      lr_inactive_string = "Living room sensor <b>In-active</b>. </br>" 
      
      gd_open_sound = "<audio controls autoplay><source src=\"gd_open.ogg\" type=\"audio/ogg\"></audio>"
      gd_open_string = "Garage Door is <b>Open</b>. </br>"
      gd_closed_string = "Garage Door is <b>Closed</b>. </br>"
      gd_moving_string = "Garage Door <b>moving</b>. </br>" + gd_open_sound

      #Motion Sensor garage
      sensor_active = "Garage sensor <b>Active</b>. </br>"
      sensor_inactive = "Garage sensor <b>In-active</b>. </br>"

      #Motion Sensor front door
      audio_play = "<audio controls autoplay><source src=\"door_bell.wav\" type=\"audio/wav\"></audio>"
      front_door_motion_sensor_active = "Front door motion <b>Active</b>. </br>" + audio_play
      front_door_motion_sensor_inactive = "Front door motion <b>In-active</b>. </br>"

      front_door_closed = "Front door <b>Closed</b> </br>"
      audio_play2 = "<audio controls autoplay><source src=\"front_door.ogg\" type=\"audio/ogg\"></audio>"
      front_door_open = "Front door <b>Open</b> </br>" +  audio_play2     

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
         log_buff = ""
         if (GPIO.input(gpio18) == 0 and GPIO.input(gpio13) == 0):
            #print("GarageDoor moving.")
            #self.logger.write("GarageDoor moving.")
            log_buff = log_buff + "INFO:   GarageDoor moving. \n"
            str_to_write = str_to_write + gd_moving_string
         elif (GPIO.input(gpio18) == 1):
            #print("GarageDoor is Closed.")
            #self.logger.write("GarageDoor is Closed.")
            log_buff = log_buff + "INFO:   GarageDoor is Closed. \n"
            str_to_write = str_to_write + gd_closed_string
         elif (GPIO.input(gpio13) == 1):
            #print("GarageDoor is Open.")
            #self.logger.write("GarageDoor is Open.")
            log_buff = log_buff + "INFO:   GarageDoor is Open. \n"
            str_to_write = str_to_write + gd_open_string
         if (GPIO.input(gpio16) == 1):
            #print("Door from kitchen to garage is Closed.")
            #self.logger.write("Door from kitchen to garage is Closed.")
            log_buff = log_buff + "INFO:   Door from kitchen to garage is Closed. \n"
            str_to_write = str_to_write + door_from_garage_to_kitchen_closed_str
         else:
            #print("Door from kitchen to garage is open.")
            #self.logger.write("Door from kitchen to garage is open.")
            log_buff = log_buff + "INFO:   Door from kitchen to garage is open. \n"
            str_to_write = str_to_write + door_from_garage_to_kitcken_open_str
         if (GPIO.input(gpio22) == 1):
            #print("Door from garage to porch is Closed.")
            #self.logger.write("Door from garage to porch is Closed.")
            log_buff = log_buff + "INFO:   Door from garage to porch is Closed. \n"
            str_to_write = str_to_write + door_to_porch_closed_string
         else:
            #print("Door  from garage to porch is open.")
            #self.logger.write("Door  from garage to porch is open.")
            log_buff = log_buff + "INFO:   Door from garage to porch is open.\n "
            str_to_write = str_to_write + door_to_porch_open_string 

         #Sensor activity
         if(GPIO.input(gpio04) == 1):
            log_buff = log_buff + "INFO:   Garage sensor active. \n"
            str_to_write = str_to_write + sensor_active
         else:
            log_buff = log_buff + "INFO:   Garage sensor in-active.\n "
            str_to_write = str_to_write + sensor_inactive

         #Front door motion sensor 
         if(GPIO.input(gpio11) == 1):
            log_buff = log_buff + "INFO:   Front door motion active. \n"
            str_to_write = str_to_write + front_door_motion_sensor_active
         else:
            log_buff = log_buff + "INFO:   Front door motion in-active.\n "
            str_to_write = str_to_write + front_door_motion_sensor_inactive

         #Front door door sensor
         if(GPIO.input(gpio09) == 1):
            log_buff = log_buff + "INFO:   Front door closed. \n"
            str_to_write = str_to_write + front_door_closed
         else:
            log_buff = log_buff + "INFO:   Front door open.\n "
            str_to_write = str_to_write + front_door_open

         #Living room motion sensor
         if(GPIO.input(gpio08) == 1):
            log_buff = log_buff + "INFO:   Living room sensor active. \n"
            str_to_write = str_to_write + lr_active_string
         else:
            log_buff = log_buff + "INFO:   Living room sensor in-active.\n "
            str_to_write = str_to_write + lr_inactive_string


         #States and logs
         if (GPIO.input(gpio18) != gd_closed_state ):
            write_out_logs = 1
            gd_closed_state = GPIO.input(gpio18)
         elif ( GPIO.input(gpio13) != gd_open_state ):
            write_out_logs = 1 
            gd_open_state = GPIO.input(gpio13)
         elif ( GPIO.input(gpio16) != g_to_kitchen_state ):
            write_out_logs = 1
            g_to_kitchen_state = GPIO.input(gpio16)
         elif ( GPIO.input(gpio22) != g_to_porch_state ):
            write_out_logs = 1
            g_to_porch_state = GPIO.input(gpio22)
         elif ( GPIO.input(gpio04) != g_sensor_state ):
            write_out_logs = 1
            g_sensor_state = GPIO.input(gpio04)
         elif ( GPIO.input(gpio11) != fd_motion_sensor_state ):
            write_out_logs = 1
            fd_motion_sensor_state = GPIO.input(gpio09)
         elif ( GPIO.input(gpio09) != fd_door_sensor ):
            write_out_logs = 1
            fd_door_sensor = GPIO.input(gpio09)
         elif ( GPIO.input(gpio08) != lr_motion_sensor_state ):
            write_out_logs = 1
            lr_motion_sensor_state = GPIO.input(gpio08)	

         if (write_out_logs == 1):
            #print("Writing to logs.")
            write_logs(str_to_write)
            time_now = datetime.datetime.now()
            diag_date = "{0}-{1}-{2}_{3}-{4}-{5}".format(str(time_now.year), str(time_now.month),
                        str(time_now.day), str(time_now.hour), str(time_now.minute),
                        str(time_now.second))
            diag_date = diag_date + ":   "+ log_buff
            log_buff = diag_date
            self.logger.write(log_buff)
            

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

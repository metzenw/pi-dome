#!/usr/bin/env python

RPI_FOUND = False

#Libraries
import socket
import uuid
import re
import PIgeneral as PIgeneral

try:
   import RPi.GPIO as GPIO
   RPI_FOUND = True
except ImportError:
   RPI_FOUND = False
   

class PInode:
  #'Common base class for PInodes'#
   def __init__(self):
      self.mode = ""
      self.mac = ""
      self.model = ""
      self.hostname = ""
      self.uuid = ""
      #All GPIO numbers are board pin numbers.
      self.gpio = {
                  '1':
                     {
                     'gpio_setting': u'3v',
                     'active': False,
                     'action': u'<script>',
                     'type': u'3v',
                     'description': u'The GPIO outputs continuous 3 volts.'
                     },
                  '2':
                     {
                     'gpio_setting': u'5v',
                     'active': False,
                     'action': u'<script>',
                     'type': u'5v',
                     'description': u'The GPIO outputs continuous 5 volts.'
                     },
                  '3':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '4':
                     {
                     'gpio_setting': u'5v',
                     'active': False,
                     'action': u'<script>',
                     'type': u'5v',
                     'description': u'The GPIO outputs continuous 5 volts.'
                     },
                  '5':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '6':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '7':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '8':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '9':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '10':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '11':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '12':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '13':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '14':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '15':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '16':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '17':
                     {
                     'gpio_setting': u'3v',
                     'active': False,
                     'action': u'<script>',
                     'type': u'3v',
                     'description': u'The GPIO delivers 3v continuously.'
                     },
                  '18':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '19':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '20':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '21':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '22':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '23':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '24':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '25':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '26':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '27':
                     {
                     'gpio_setting': u'DNC',
                     'active': False,
                     'action': u'<script>',
                     'type': u'DNC',
                     'description': u'DO NOT CONNECT!'
                     },
                  '28':
                     {
                     'gpio_setting': u'DNC',
                     'active': False,
                     'action': u'<script>',
                     'type': u'DNC',
                     'description': u'DO NOT CONNECT!'
                     },
                  '29':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '30':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '31':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '32':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '33':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '34':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '35':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '36':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '37':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '38':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '39':
                     {
                     'gpio_setting': u'Ground',
                     'active': False,
                     'action': u'<script>',
                     'type': u'Ground',
                     'description': u'The GPIO is for ground.'
                     },
                  '40':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     }
                      
                  }

   # ====================================================================
   #  Initialize - Initial call to setup the object
   # ====================================================================
   def init(self, mode, model):
      self.mode = mode
      self.model = model
      self.generate_uuid()
      self.get_hostname()
      if self.mode == "node":
          self.setup_gpio()

   # ====================================================================
   #  Generate a unique name to be tracked by the server.
   # ====================================================================
   def generate_uuid(self):
      print("Making uuid.")
      self.uuid = uuid.uuid1()

   # ====================================================================
   #  Set the hostname of the system
   # ====================================================================
   def get_hostname(self):
      print("Retrieving hostname.")
      self.hostname = socket.gethostname()

   # ====================================================================
   #  Setup GPIOs
   # ====================================================================
   def setup_gpio(self):
      print("Setting up GPIOs.")
      if RPI_FOUND:
         GPIO.setmode(GPIO.BOARD) #Pin number
         print("Found a PI model: " + self.model)
         for key in self.gpio:
            if self.model == "b" and int(key) > 26:
               continue
            match = re.search(r'PUD_DOWN', self.gpio[key]["gpio_setting"])
            if match:
               try:
                  GPIO.setup(int(key), GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
                  print("Setting down on " + key)
               except ExceptionI:
                  print ("Unable to set gpio down: " + str(ExceptionI))
            match = re.search(r'PUD_UP', self.gpio[key]["gpio_setting"])
            if match:
               try:
                  GPIO.setup(int(key), GPIO.OUT)
               except ExceptionI:
                  print ("Unnable to set gpio out: " + str(ExceptionI))

   # ====================================================================
   #  Monitor GPIOs
   # ====================================================================
   def monitor_gpio(self):
      #print("Monitor GPIOs.")
      for key in self.gpio:
         match = re.search(r'PUD_DOWN', self.gpio[key]["gpio_setting"])
         if match:
            if self.model == "b" and int(key) > 26:
               continue
            if GPIO.input(int(key)) == 1:
               self.gpio[key]['active'] = True
               #print (str(key) + " is active")
         else:
            self.gpio[key]['active'] = False



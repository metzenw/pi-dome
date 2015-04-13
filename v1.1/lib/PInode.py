#!/usr/bin/env python

#Libraries
import socket
import uuid
import re
import PIgeneral as PIgeneral
if PIgeneral.module_exists("RPi.GPIO"):
   import RPi.GPIO as GPIO

class PInode:
  #'Common base class for PInodes'#
   def __init__(self):
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '8':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '11':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '12':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '13':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '16':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '19':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '22':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '23':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '24':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '32':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '33':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '36':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '37':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '38':
                     {
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
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
                     'gpio_setting': u'up|down', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     }
                      
                  }

   # ====================================================================
   #  Initialize - Initial call to setup the object
   # ====================================================================
   def init(self):
      print("Init.")
      self.generate_uuid()
      self.get_hostname()

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
      for key in self.gpio:
         match = re.search(r'PUD_DOWN', self.gpio[key]["gpio_setting"])
         if match:
            GPIO.setup(key, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
         match = re.search(r'PUD_UP', self.gpio[key]["gpio_setting"])
         if match:
            GPIO.setup(key, GPIO.OUT)





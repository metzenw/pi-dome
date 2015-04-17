#!/usr/bin/env python

RPI_FOUND = False

#Libraries
import json
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
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '8':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '11':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '12':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '13':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '16':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '19':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '22':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '23':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '24':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '32':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '33':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     },
                  '36':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '37':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
                     },
                  '38':
                     {
                     'gpio_setting': u'PUD_DOWN', #PUD_DOWN|PUD_UP
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'This is a GPIO.'
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
                     'description': u'This is a GPIO.'
                     }
                      
                  }

   # ====================================================================
   #  Initialize - Initial call to setup the object
   # ====================================================================
   def init(self, mode, model, config):
      self.mode = mode
      self.model = model
      self.generate_uuid()
      self.get_hostname()
      if self.mode == "node":
          self.setup_gpio()
      #GPIO 3
      self.gpio['3']['action'] = config.get('scripts', 'pin3_script')
      self.gpio['3']['gpio_setting'] = config.get('node', 'pin3')
      self.gpio['3']['description'] = config.get('node', 'pin3_description')
      #GPIO 5
      self.gpio['5']['action'] = config.get('scripts', 'pin5_script')
      self.gpio['5']['gpio_setting'] = config.get('node', 'pin5')
      self.gpio['5']['description'] = config.get('node', 'pin5_description')
      #GPIO 7
      self.gpio['7']['action'] = config.get('scripts', 'pin7_script')
      self.gpio['7']['gpio_setting'] = config.get('node', 'pin7')
      self.gpio['7']['description'] = config.get('node', 'pin7_description')
      #GPIO 8
      self.gpio['8']['action'] = config.get('scripts', 'pin8_script')
      self.gpio['8']['gpio_setting'] = config.get('node', 'pin8')
      self.gpio['8']['description'] = config.get('node', 'pin8_description')
      #GPIO 10
      self.gpio['10']['action'] = config.get('scripts', 'pin10_script')
      self.gpio['10']['gpio_setting'] = config.get('node', 'pin10')
      self.gpio['10']['description'] = config.get('node', 'pin10_description')
      #GPIO 11
      self.gpio['11']['action'] = config.get('scripts', 'pin11_script')
      self.gpio['11']['gpio_setting'] = config.get('node', 'pin11')
      self.gpio['11']['description'] = config.get('node', 'pin11_description')
      #GPIO 12
      self.gpio['12']['action'] = config.get('scripts', 'pin12_script')
      self.gpio['12']['gpio_setting'] = config.get('node', 'pin12')
      self.gpio['12']['description'] = config.get('node', 'pin12_description')
      #GPIO 13
      self.gpio['13']['action'] = config.get('scripts', 'pin13_script')
      self.gpio['13']['gpio_setting'] = config.get('node', 'pin13')
      self.gpio['13']['description'] = config.get('node', 'pin13_description')
      #GPIO 15
      self.gpio['15']['action'] = config.get('scripts', 'pin15_script')
      self.gpio['15']['gpio_setting'] = config.get('node', 'pin15')
      self.gpio['15']['description'] = config.get('node', 'pin15_description')
      #GPIO 16
      self.gpio['16']['action'] = config.get('scripts', 'pin16_script')
      self.gpio['16']['gpio_setting'] = config.get('node', 'pin16')
      self.gpio['16']['description'] = config.get('node', 'pin16_description')
      #GPIO 18
      self.gpio['18']['action'] = config.get('scripts', 'pin18_script')
      self.gpio['18']['gpio_setting'] = config.get('node', 'pin18')
      self.gpio['18']['description'] = config.get('node', 'pin18_description')
      #GPIO 19
      self.gpio['19']['action'] = config.get('scripts', 'pin19_script')
      self.gpio['19']['gpio_setting'] = config.get('node', 'pin19')
      self.gpio['19']['description'] = config.get('node', 'pin19_description')
      #GPIO 21
      self.gpio['21']['action'] = config.get('scripts', 'pin21_script')
      self.gpio['21']['gpio_setting'] = config.get('node', 'pin21')
      self.gpio['21']['description'] = config.get('node', 'pin21_description')
      #GPIO 22
      self.gpio['22']['action'] = config.get('scripts', 'pin22_script')
      self.gpio['22']['gpio_setting'] = config.get('node', 'pin22')
      self.gpio['22']['description'] = config.get('node', 'pin22_description')
      #GPIO 23
      self.gpio['23']['action'] = config.get('scripts', 'pin23_script')
      self.gpio['23']['gpio_setting'] = config.get('node', 'pin23')
      self.gpio['23']['description'] = config.get('node', 'pin23_description')
      #GPIO 24
      self.gpio['24']['action'] = config.get('scripts', 'pin24_script')
      self.gpio['24']['gpio_setting'] = config.get('node', 'pin24')
      self.gpio['24']['description'] = config.get('node', 'pin24_description')
      #GPIO 26
      self.gpio['26']['action'] = config.get('scripts', 'pin26_script')
      self.gpio['26']['gpio_setting'] = config.get('node', 'pin26')
      self.gpio['26']['description'] = config.get('node', 'pin26_description')
      #GPIO 29
      self.gpio['29']['action'] = config.get('scripts', 'pin29_script')
      self.gpio['29']['gpio_setting'] = config.get('node', 'pin29')
      self.gpio['29']['description'] = config.get('node', 'pin29_description')
      #GPIO 31
      self.gpio['31']['action'] = config.get('scripts', 'pin31_script')
      self.gpio['31']['gpio_setting'] = config.get('node', 'pin31')
      self.gpio['31']['description'] = config.get('node', 'pin31_description')
      #GPIO 32
      self.gpio['32']['action'] = config.get('scripts', 'pin32_script')
      self.gpio['32']['gpio_setting'] = config.get('node', 'pin32')
      self.gpio['32']['description'] = config.get('node', 'pin32_description')
      #GPIO 33
      self.gpio['33']['action'] = config.get('scripts', 'pin33_script')
      self.gpio['33']['gpio_setting'] = config.get('node', 'pin33')
      self.gpio['33']['description'] = config.get('node', 'pin33_description')
      #GPIO 35
      self.gpio['35']['action'] = config.get('scripts', 'pin35_script')
      self.gpio['35']['gpio_setting'] = config.get('node', 'pin35')
      self.gpio['35']['description'] = config.get('node', 'pin35_description')
      #GPIO 36
      self.gpio['36']['action'] = config.get('scripts', 'pin36_script')
      self.gpio['36']['gpio_setting'] = config.get('node', 'pin36')
      self.gpio['36']['description'] = config.get('node', 'pin36_description')
      #GPIO 37
      self.gpio['37']['action'] = config.get('scripts', 'pin37_script')
      self.gpio['37']['gpio_setting'] = config.get('node', 'pin37')
      self.gpio['37']['description'] = config.get('node', 'pin37_description')
      #GPIO 38
      self.gpio['38']['action'] = config.get('scripts', 'pin38_script')
      self.gpio['38']['gpio_setting'] = config.get('node', 'pin38')
      self.gpio['38']['description'] = config.get('node', 'pin38_description')
      #GPIO 40
      self.gpio['40']['action'] = config.get('scripts', 'pin40_script')
      self.gpio['40']['gpio_setting'] = config.get('node', 'pin40')
      self.gpio['40']['description'] = config.get('node', 'pin40_description')


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
                  if int(key) == 5:
                     print("Doing nothing with pin 5.")
                  elif int(key) == 3:
                     print("Doing nothing with pin 3.")
                     nothing = 0
                  else:
                     print("Setting res down on " + key)
                     GPIO.setup(int(key), GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
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
      #print("Monitor GPIOs: "+ str(RPI_FOUND))
      if not RPI_FOUND:
         return 1
      for key in self.gpio:
         #print (key + ": " + self.gpio[key]["gpio_setting"])
         match = re.search(r'PUD_DOWN', self.gpio[key]["gpio_setting"])
         if match:
            if self.model == "b" and int(key) > 26:
               continue
            if GPIO.input(int(key)) == 1 and int(key) != 3 and int(key) != 5:
               self.gpio[key]['active'] = True
               #print (str(key) + " is active")
         else:
            self.gpio[key]['active'] = False


   # ====================================================================
   #  Convert GPIOs to jason
   # ====================================================================
   def convert_gpio_to_jason(self):
      data = json.dumps(self.gpio)
      data_out = json.loads(data)
      return data_out






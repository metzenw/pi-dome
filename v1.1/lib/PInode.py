#!/usr/bin/env python

#Libraries
import socket
import uuid

class PInode:
  #'Common base class for PInodes'#
   def __init__(self):
      self.mac = ""
      self.hostname = ""
      self.uuid = ""
      self.gpio = {
                  '1':
                     {
                     'gpio_setting': u'<PUD_DOWN|PUD_UP>',
                     'active': False,
                     'action': u'<script>',
                     'type': u'<door|window|action|motion_sensor>',
                     'description': u'The GPIO handels action request for a door.'
                     },
                  '2':
                     {
                     'gpio_setting': u'<PUD_DOWN|PUD_UP>',
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








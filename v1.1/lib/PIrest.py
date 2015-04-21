#!/usr/bin/python
import httplib
import base64
import string
import json


class PIrest:
  #'Common base class for PIrest'#
   def __init__(self):
      self.base_address = "vengersonline.com"
      self.port = 5000
      self.user_name = "pi-dome"
      self.password = "pi-dome"
   ####################################################
   # Rest post
   ####################################################
   def post(self, url, payload):
      conn = httplib.HTTPConnection(self.base, self.port, timeout=60)
      conn.request('POST', self.url, payload, { 'Authorization' : 'Basic '+string.strip(base64.encodestring(self.user_name+":"+self.password)), 'Content-Type' : 'application/json' })
      r = conn.getresponse()
      return r.read()

   ####################################################
   # Rest put
   ####################################################
   def put(self, url, payload):
      conn = httplib.HTTPConnection(self.base, self.port, timeout=60)
      conn.request('PUT', url, payload, { 'Authorization' : 'Basic '+string.strip(base64.encodestring(self.user_name+":"+self.password)), 'Content-Type' : 'application/json' })
      r = conn.getresponse()
      return r.read()

   ####################################################
   # Rest get
   ####################################################
   def get(self, url):
      conn = httplib.HTTPConnection(self.base_address, self.port, timeout=60)
      conn.request('GET', url, None, { 'Authorization' : 'Basic '+string.strip(base64.encodestring(self.user_name+":"+self.password))})
      return conn.getresponse().read()



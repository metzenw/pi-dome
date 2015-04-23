#!/usr/bin/python
import httplib
import base64
import string
import json
import urllib2

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
   def post(self, url, payload, lockrest):
      lockrest.acquire()
      print(self.base_address+":"+str(self.port)+url)
      conn = httplib.HTTPConnection(self.base_address, self.port, timeout=60)
      conn.request('POST', url, payload, { 'Authorization' : 'Basic '+string.strip(base64.encodestring(self.user_name+":"+self.password)), 'Content-Type' : 'application/json' })
      r = conn.getresponse()
      lockrest.release()
      #return r.read()

   ####################################################
   # Rest put
   ####################################################
   def put(self, url, payload):
      conn = httplib.HTTPConnection(self.base_address, self.port, timeout=60)
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

   ####################################################
   # Rest del
   ####################################################
   def delete_node(self, sub_url,  id):
      query_url = "http://vengersonline.com:5000"+ sub_url + id
      opener = urllib2.build_opener(urllib2.HTTPHandler)
      req = urllib2.Request(query_url, None)
      req.get_method = lambda: 'DELETE'
      url = ""
      try:
         url = urllib2.urlopen(req)
         return 0 
      except:
         print("Unable to remove: " + id + ". " + url)
         return 1



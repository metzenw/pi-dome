#!/usr/bin/python
import Adafruit_DHT as dht
import time

try:
   import Adafruit_DHT as dht
   DHT_FOUND = True
except ImportError:
   DHT_FOUND = False


class PItemp:
   #'Common base class for PInodes'#
   def __init__(self):
      self.name = "Temp and humidity."

   def get_temp_and_humidity(self):
      if DHT_FOUND:
         h,t = dht.read_retry(dht.DHT11, 4)
         #print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h)
         fahrenheit = t*1.8000 + 32.00
         #print "Fahrenheit: " + str(fahrenheit)
         return fahrenheit, h



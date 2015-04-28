#!/usr/bin/python
import Adafruit_DHT as dht
import time
import calendar

try:
   import Adafruit_DHT as dht
   DHT_FOUND = True
except ImportError:
   DHT_FOUND = False


class PItemp:
   #'Common base class for PInodes'#
   def __init__(self):
      self.name = "Temp and humidity."
      self.delta = 10
      self.track_delta = calendar.timegm(time.gmtime())
      self.reset_delta_count = calendar.timegm(time.gmtime())      
      self.fahrenheit = 0.0
      self.humidity = 0.0
   # ====================================================================
   #  Updated every 10 seconds for temp and humidity
   # ====================================================================
   def get_temp_and_humidity(self):
      if DHT_FOUND:
        self.track_delta = calendar.timegm(time.gmtime())
        if (self.track_delta - self.reset_delta_count > self.delta):
           #Reset times
           self.track_delta = calendar.timegm(time.gmtime())
           self.reset_delta_count = calendar.timegm(time.gmtime())
           #Call DHT and get temp, humidity.
           self.humidity,t = dht.read_retry(dht.DHT11, 4)
           self.fahrenheit = t*1.8000 + 32.00
        return self.fahrenheit, self.humidity



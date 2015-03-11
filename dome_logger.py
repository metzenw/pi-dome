#!/usr/bin/python
import urllib
import urllib2
import json

url = 'http://vengersonline.com:5000/get_my_ip/'
response = urllib2.urlopen(url).read()

print response


data = json.loads(response)
print data

"""
params = urllib.urlencode({
   'firstName': 'John',
   'lastNme': 'Doe'
})

print params
"""

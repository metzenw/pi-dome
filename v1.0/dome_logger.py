#!/usr/bin/python
import urllib
import urllib2
import json
import base64

username = 'pi-dome'
password = 'pi-dome'


request = urllib2.Request("http://vengersonline.com:5000/api/doors/?key=1234")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)
page = result.read()
#print page
json_d = json.loads(page)[0]
datapoints = json_d['doors']
print datapoints

doors = json.loads(page)
#print doors
"""
base64string = base64.encodestring(
                '%s:%s' % (username, password))[:-1]
authheader =  "Basic %s" % base64string
request.add_header("Authorization", authheader)
try:
   result = urllib2.urlopen(request)
except IOError, e:
   print "Failed to authenticate."
#print result
thepage=result.read()
print thepage
"""


""" Working request
url = 'http://vengersonline.com:5000/api/doors/?key=1234'
response = urllib2.urlopen(url).read()

print response


doors = json.loads(response)
print doors

end working request """ 

"""
params = urllib.urlencode({
   'firstName': 'John',
   'lastNme': 'Doe'
})

print params
"""

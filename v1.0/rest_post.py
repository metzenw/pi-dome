#!/usr/bin/python
import httplib
import base64
import string
import json
def post(base, port, url, payload):
	conn = httplib.HTTPConnection(base, port, timeout=60)
	conn.request('POST', url, payload, { 'Authorization' : 'Basic '+string.strip(base64.encodestring('pi-dome:pi-dome')), 'Content-Type' : 'application/json' })
	r = conn.getresponse()
	return r.read()

# Note that json.dumps may also be used to create the json string from a python object
data = post("vengersonline.com", 5000, "/api/doors/", '{"gpio":11}')
print json.loads(data)

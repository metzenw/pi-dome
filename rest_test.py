#!/usr/bin/python
import httplib
import base64
import string
import json
def get(base, port, url):
	conn = httplib.HTTPConnection(base, port, timeout=60)
	conn.request('GET', url, None, { 'Authorization' : 'Basic '+string.strip(base64.encodestring('pi-dome:pi-dome'))})
	return conn.getresponse().read()

data = get("vengersonline.com", 5000, "/api/doors/")
print json.loads(data)

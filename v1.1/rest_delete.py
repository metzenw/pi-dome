#!/usr/bin/python
import requests
import httplib
import base64
import string
import json


#requests.delete(url)

#requests.delete("vengersonline.com:5000/api/nodes/192.168.1.100")
#delete_url = "vengersonline.com:5000/api/nodes/192.168.1.100"

#req = urllib2.Request(delete_url, None, headers)<br>req.get_method = lambda: 'DELETE'
#data = urllib2.urlopen(req).read()
#result = json.loads(data)


#def _make_request(url, data, method):
#    request.urllib2.Request(url, data=data)
#    request.get_method = lambda: method
#url = "http://vengersonline.com:5000/api/nodes/192.168.1.100"
#url = "http://vengersonline.com:5000/api/nodes/192.168.1.100"
#requests.delete(url)



import urllib2
#opener = urllib2.build_opener(urllib2.HTTPHandler)
#request = urllib2.Request('http://vengersonline.com:5000/api/nodes/192.168.1.100')
#request.add_header('Content-Type', 'your/contenttype')
#request.get_method = lambda: 'DELETE'
#url = opener.open(request)

def delete_node(id):
   query_url = "http://vengersonline.com:5000/api/nodes/" + id
   #query_url = oauth['http://vengersonline.com:5000']+'/api/nodes/%s' % id 
   #headers = {
   #  'Authorization': 'OAuth '+oauth['access_token']
   #}
   opener = urllib2.build_opener(urllib2.HTTPHandler)
   req = urllib2.Request(query_url, None)
   #req = urllib2.Request(query_url, None, headers)
   req.get_method = lambda: 'DELETE' 
   url = urllib2.urlopen(req) 

delete_node("192.168.1.100")


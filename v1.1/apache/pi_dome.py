#!/usr/bin/python
# ====================================================================
# The pi-dome script was a idea I had after seeing a garage door 
# youtube video where a raspberry pi was used with a 5v relay to open
# the garage over wifi.
#
# Copyright (C) 2014 by TekZap Co. 
# All Rights Reserved.
# https://github.com/metzenw/pi-dome

# ====================================================================
# The MIT License (MIT)
#
# Copyright (c) 2014 TekZap Co.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE
# ====================================================================

# ====================================================================
# Import from libraries 
# ====================================================================
import ConfigParser

from flask import Flask, jsonify, abort, make_response, request
#from flask.ext.httpauth import HTTPBasicAuth, HTTPDigestAuth
from flask import render_template

#Used to convers string to python dict
import ast

# Read in conf file
config = ConfigParser.ConfigParser()
config.read('dome.cfg')


PI_DOME_VERSION = config.get('MASTER', 'VERSION', 0)   # Pi-dome version.
AUTHOR = "Jason Booth"                                 # The author (me).
AUTHOR_EMAIL = "metzenw at gmail (dot) com"            # My email. Report bugs here or via github.com.
GIT_REPO = "https://github.com/metzenw/pi-dome"        # Repo address.

# Setting up username and password for http auth user.
if config.get('MASTER', 'HTTP_AUTH_USER', 0):
    HTTP_AUTH_USER = config.get('MASTER', 'HTTP_AUTH_USER', 0)
else:
    HTTP_AUTH_USER = "pi-dome"
if config.get('MASTER', 'HTTP_AUTH_PASSWORD', 0):
    HTTP_AUTH_PASSWORD = config.get('MASTER', 'HTTP_AUTH_PASSWORD', 0)
else:
    HTTP_AUTH_PASSWORD = "pi-dome"

# Setup flask
app = Flask(__name__)

# Setup HTTPAuth
#auth = HTTPBasicAuth()
#@auth.get_password
def get_password(username):
    if username == HTTP_AUTH_USER:
        return HTTP_AUTH_PASSWORD
    return None

# HTTPAuth failed to access responce
#@auth.error_handler
#def unauthorized():
#    return make_response( jsonify( { 'error': 'Unauthorized access' } ), 401 )


# Supported resources that pi-dome manages.
pi_servers = [
    {
        'id': 1,
        'version': u'vB',   #vA, vB, vB+
        'notes': u'Some notes.',
        'cputemp': 0,
        'description': u'Central pi-server.',
        'lastupdate': '0',
        'ip': '',
        'active': False
    }
]

pi_nodes = {}
"""
pi_nodes = {
        'id': 1,
        'version': u'vB',   #vA, vB, vB+
        'notes': u'Some notes.',
        'cputemp': 0,
        'description': u'Central pi-server.',
        'lastupdate': '0',
        'ip': '',
        'active': False
}
"""

# ====================================================================
# Root
# ====================================================================
@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)


# ====================================================================
# IP logging
# ====================================================================
@app.route("/get_my_ip/", methods=["GET"])
def get_my_ip():
    print(request.remote_addr)
    return jsonify({'ip': request.remote_addr}), 200



# ====================================================================
# v1.1 pi-node 
# ====================================================================
@app.route('/api/nodes/', methods = ['GET'])
#@auth.login_required
def get_nodes():
    return jsonify( { 'nodes': pi_nodes } )

@app.route('/api/nodes/<node_id>', methods = ['GET'])
#@auth.login_required
def get_node_id(node_id):
    if node_id in pi_nodes:
        return jsonify( { node_id : pi_nodes[node_id] } )
    else:
        return jsonify( { "result" : False } ), 404




######################################################
# Create
######################################################
@app.route('/api/nodes/', methods = ['POST'])
#@auth.login_required
def create_node():
    if not request.json :
        abort(400)
    duplicate_found = 0
    try:
        for n_id in request.json:
            if n_id in pi_nodes:
                #return jsonify( { 'result': False } ), 404
                duplicate_found = 1
            # Add to pi-nodes
            pi_nodes[n_id] = request.json[n_id]
       # return jsonify( { 'result': True } ), 201
    except:
        return jsonify( { 'result': False } ), 406
    #if duplicate_found == 0:
    return jsonify( { 'result': True } ), 201
    #else:
    #    return jsonify( { 'result': False } ), 404

######################################################
# Updates after a post
######################################################
@app.route('/api/nodes/<node_id>', methods = ['PUT'])
#@auth.login_required
def update_door(node_id):
    if not request.json :
        abort(400)

    if node_id in pi_nodes:
        #update node
        #print ("Found key!")
        pi_nodes[node_id] = request.json[node_id]
        return jsonify( { 'result': True } ), 201
    else:
        return jsonify( { 'result': False } ), 404

######################################################
# Delete
######################################################
@app.route('/api/nodes/<node_id>', methods = ['DELETE'])
#@auth.login_required
def delete_node(node_id):
    print("Del request")
    if node_id in pi_nodes:
        try: 
            print "Trying to pop"
            pi_nodes.pop(node_id, None)
            return jsonify( { 'result': True } ), 201
        except:
            return jsonify( { 'result': False } ), 404
    else:
        return jsonify( { 'result': False } ), 404


# ====================================================================
# pi_servers
# ====================================================================
@app.route('/api/servers/', methods = ['GET'])
#@auth.login_required
def get_servers():
    return jsonify( { 'servers': pi_servers } )

@app.route('/api/servers/<int:server_id>', methods = ['GET'])
#@auth.login_required
def get_server_id(server_id):
    n_id = filter(lambda t: t['id'] == server_id, pi_servers)
    if len(n_id ) == 0:
        abort(404)
    return jsonify( { 'server': n_id[0] } )

@app.route('/api/servers/', methods = ['POST'])
#@auth.login_required
def create_server():
    """
    server = {
        'id': pi_servers[-1]['id'] + 1,
        'version': request.json.get('version', ""),
        'notes': request.json.get('notes', ""),
        'cputemp': request.json.get('cputemp', ""), 
        'description': request.json.get('description', ""),
        'lastupdate': request.json.get('lastupdate', ""),
        'ip': request.remote_addr,
        'active': False
    }
    """
    #pi_servers.append(server)
    #return jsonify( { 'server': server } ), 201
    print request.json.get('id', "")
    return jsonify( { 'test': "test" } ), 201

@app.route('/api/servers/<int:server_id>', methods = ['PUT'])
#@auth.login_required
def update_server(server_id):
    server = filter(lambda t: t['id'] == server_id, pi_servers)
    if len(server) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'open' in request.json and type(request.json['open']) is not bool:
        abort(400)
    server[0]['version'] = request.json.get('version', server[0]['version'])
    server[0]['notes'] = request.json.get('notes', server[0]['notes'])
    server[0]['cputemp'] = request.json.get('cputemp', server[0]['cputemp'])
    server[0]['description'] = request.json.get('description', server[0]['description'])
    server[0]['active'] = request.json.get('active', server[0]['active'])
    #server[0]['ip'] = request.remote_addr
    return jsonify( { 'server': server[0] } )

@app.route('/api/servers/<int:server_id>', methods = ['DELETE'])
#@auth.login_required
def delete_server(server_id):
    server = filter(lambda t: t['id'] == server_id, pi_servers)
    if len(server) == 0:
        abort(404)
    pi_servers.remove(server[0])
    return jsonify( { 'result': True } )



# ====================================================================
# Error Handling
# ====================================================================
@app.errorhandler(404)
def not_found(error):
    return make_response( jsonify( { 'error': 'Not found' } ), 404 )

# ====================================================================
# Main function
# ====================================================================
if __name__ == '__main__':
    print ("Starting Flask \n")
    app.run(host='0.0.0.0', threaded=True)

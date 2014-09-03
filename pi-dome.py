#!flask/bin/python
# ====================================================================
# The pi-dome script was a idea I had after seeing a garage door 
# youtube video where a raspberry pi was used with a 5v relay.
#
# Copyright (C) 2014 by TekZap Co. 
# All Rights Reserved.
#
# THIS SOFTWARE SCRIPT IS PROVIDED BY TekZap Co.
# "AS IS" AND IS FOR REFERENCE USE ONLY.  ANY EXPRESS OR IMPLIED 
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL TekZap Co. 
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
# OR CONSEQUENTIAL DAMAGES ARISING FROM THE USE THEREOF.
# ====================================================================

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

from flask import Flask, jsonify, abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
def get_password(username):
    if username == "pi-dome":
        return 'pi-dome'
    return None

@auth.error_handler
def unauthorized():
    return make_response( jsonify( { 'error': 'Unauthorized access' } ), 401 )


app = Flask(__name__)

doors = [
    {
        'id': 1,
        'type': u'door',
        'gpio': 11,
        'voltage': 3.3,
        'notes': u'Some notes.',
        'description': u'Garage door up.', 
        'open': False
    },
    {
        'id': 2,
        'type': u'door',
        'gpio': 13,
        'voltage': 3.3,
        'notes': u'Some notes.',
        'description': u'Garage door down.', 
        'open': False
    }
]

windows = [
    {
        'id': 1,
        'type': u'window',
        'gpio': 0,
        'voltage': 3.3,
        'notes': u'Some notes.',
        'description': u'Place Holder.',
        'open': False
    }
]

garage = [
    {
        'id': 1,
        'type': u'garage',
        'gpio': 0,
        'voltage': 5,
        'notes': u'Some notes.',
        'description': u'The garage door.',
        'active': False,
        'open': False
    }
]

# ====================================================================
# Doors 
# ====================================================================
@app.route('/api/doors/', methods = ['GET'])
@auth.login_required
def get_doors():
    return jsonify( { 'doors': doors } )

@app.route('/api/doors/<int:door_id>', methods = ['GET'])
@auth.login_required
def get_door_id(door_id):
    d_id = filter(lambda t: t['id'] == door_id, doors)
    if len(d_id ) == 0:
        abort(404)
    return jsonify( { 'door': d_id[0] } )

@app.route('/api/doors/', methods = ['POST'])
@auth.login_required
def create_door():
    if not request.json or not 'gpio' in request.json:
        abort(400)
    door = {
        'id': doors[-1]['id'] + 1,
        'type': request.json.get('type', ""),
        'gpio': request.json['gpio'],
        'voltage': request.json.get('voltage', ""),
        'notes': request.json.get('notes', ""),
        'description': request.json.get('description', ""),
        'active': False,
        'open': False
    }
    doors.append(door)
    return jsonify( { 'door': door } ), 201

@app.route('/api/doors/<int:door_id>', methods = ['PUT'])
@auth.login_required
def update_door(door_id):
    door = filter(lambda t: t['id'] == door_id, doors)
    if len(door) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'open' in request.json and type(request.json['open']) is not bool:
        abort(400)
    door[0]['id'] = request.json.get('id', door[0]['id'])
    door[0]['type'] = request.json.get('type', door[0]['type'])
    door[0]['gpio'] = request.json.get('gpio', door[0]['gpio'])
    door[0]['voltage'] = request.json.get('voltage', door[0]['voltage'])
    door[0]['notes'] = request.json.get('notes', door[0]['notes'])
    door[0]['description'] = request.json.get('description', door[0]['description'])
    door[0]['open'] = request.json.get('open', door[0]['open'])
    return jsonify( { 'door': door[0] } )

@app.route('/api/doors/<int:door_id>', methods = ['DELETE'])
@auth.login_required
def delete_door(door_id):
    door = filter(lambda t: t['id'] == door_id, doors)
    if len(door) == 0:
        abort(404)
    doors.remove(door[0])
    return jsonify( { 'result': True } )

# ====================================================================
# Windows                     
# ====================================================================
@app.route('/api/windows/', methods = ['GET'])
@auth.login_required
def get_windows():
    return jsonify( { 'windows': windows } )

@app.route('/api/windows/<int:window_id>', methods = ['GET'])
@auth.login_required
def get_window_id(window_id):
    w_id = filter(lambda t: t['id'] == window_id, windows)
    if len(w_id) == 0:
        abort(404)
    return jsonify( { 'window': w_id[0] } )

@app.route('/api/windows/', methods = ['POST'])
@auth.login_required
def create_window():
    if not request.json or not 'gpio' in request.json:
        abort(400)
    window =  {
        'id': windows[-1]['id'] + 1,
        'type': request.json.get('type', ""),
        'gpio': request.json['gpio'],
        'voltage': request.json.get('voltage', ""),
        'notes': request.json.get('notes', ""),
        'description': request.json.get('description', ""),
        'open': False
    }
    windows.append(window)
    return jsonify( {'window': window} ), 201

@app.route('/api/windows/<int:window_id>', methods = ['PUT'])
@auth.login_required
def update_window(window_id):
    window = filter(lambda t: t['id'] == window_id, windows)
    if len(window) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'open' in request.json and type(request.json['open']) is not bool:
        abort(400)
    window[0]['id'] = request.json.get('id', window[0]['id'])
    window[0]['type'] = request.json.get('type', window[0]['type'])
    window[0]['gpio'] = request.json.get('gpio', window[0]['gpio'])
    window[0]['voltage'] = request.json.get('voltage', window[0]['voltage'])
    window[0]['notes'] = request.json.get('notes', window[0]['notes'])
    window[0]['description'] = request.json.get('description', window[0]['description'])
    window[0]['open'] = request.json.get('open', window[0]['open'])
    return jsonify( { 'window': window[0] } )

@app.route('/api/windows/<int:window_id>', methods = ['DELETE'])
@auth.login_required
def delete_window(window_id):
    window = filter(lambda t: t['id'] == window_id, windows)
    if len(window) == 0:
        abort(404)
    windows.remove(window[0])
    return jsonify( { 'result': True } )


# ====================================================================
# Garage Door                     
# ====================================================================
@app.route('/api/garage/', methods = ['GET'])
@auth.login_required
def get_garage():
    return jsonify( { 'garage': garage } )

@app.route('/api/garage/<int:garage_id>', methods = ['GET'])
@auth.login_required
def get_garage_id(garage_id):
    g_id = filter(lambda t: t['id'] == garage_id, garage)
    if len(g_id) == 0:
        abort(404)
    return jsonify( { 'garage': g_id[0] } )

@app.route('/api/garage/', methods = ['POST'])
@auth.login_required
def create_garage():
    if not request.json or not 'gpio' in request.json:
        abort(400)
    g_garage = {
        'id': garage[-1]['id'] + 1,
        'type': request.json.get('type', ""),
        'gpio': request.json['gpio'],
        'voltage': request.json.get('voltage', ""),
        'notes': request.json.get('notes', ""),
        'description': request.json.get('description', ""),
        'active': False,
        'open': False
    }
    garage.append(g_garage)
    return jsonify( { 'garage': g_garage } ), 201

@app.route('/api/garage/<int:garage_id>', methods = ['PUT'])
@auth.login_required
def update_garage(garage_id):
    g_garage = filter(lambda t: t['id'] == garage_id, garage)
    if len(g_garage) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'open' in request.json and type(request.json['open']) is not bool:
        abort(400)
    g_garage[0]['id'] = request.json.get('id', g_garage[0]['id'])
    g_garage[0]['type'] = request.json.get('type', g_garage[0]['type'])
    g_garage[0]['gpio'] = request.json.get('gpio', g_garage[0]['gpio'])
    g_garage[0]['voltage'] = request.json.get('voltage', g_garage[0]['voltage'])
    g_garage[0]['notes'] = request.json.get('notes', g_garage[0]['notes'])
    g_garage[0]['description'] = request.json.get('description', g_garage[0]['description'])
    g_garage[0]['open'] = request.json.get('open', g_garage[0]['open'])
    return jsonify( { 'garage': g_garage[0] } )

@app.route('/api/garage/<int:garage_id>', methods = ['DELETE'])
@auth.login_required
def delete_garage(garage_id):
    g_garage = filter(lambda t: t['id'] == garage_id, garage)
    if len(g_garage) == 0:
        abort(404)
    garage.remove(g_garage[0])
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
    app.run(debug = True)

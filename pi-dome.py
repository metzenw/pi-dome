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
def get_doors():
    return jsonify( { 'doors': doors } )

@app.route('/api/doors/<int:door_id>', methods = ['GET'])
def get_door_id(door_id):
    d_id = filter(lambda t: t['id'] == door_id, doors)
    if len(d_id ) == 0:
        abort(404)
    return jsonify( { 'door': d_id[0] } )

# ====================================================================
# Windows                     
# ====================================================================
@app.route('/api/windows/', methods = ['GET'])
def get_windows():
    return jsonify( { 'windows': windows } )

@app.route('/api/windows/<int:window_id>', methods = ['GET'])
def get_window_id(window_id):
    w_id = filter(lambda t: t['id'] == window_id, windows)
    if len(w_id) == 0:
        abort(404)
    return jsonify( { 'window': w_id[0] } )

# ====================================================================
# Garage Door                     
# ====================================================================
@app.route('/api/garage/', methods = ['GET'])
def get_garage():
    return jsonify( { 'garage': garage } )

@app.route('/api/garage/<int:garage_id>', methods = ['GET'])
def get_garage_id(garage_id):
    g_id = filter(lambda t: t['id'] == garage_id, garage)
    if len(g_id) == 0:
        abort(404)
    return jsonify( { 'garage': g_id[0] } )

# ====================================================================
# Place holder
# ====================================================================
@app.route('/api/doors/update/', methods = ['GET'])
def update_doors():
    #doors[0]['description'] = 'Garge door up - updated'
    return "Updating"

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

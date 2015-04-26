#!/usr/bin/env python
import ConfigParser
import time
import json
from flask import jsonify
import thread
import calendar
import signal
import sys

#My own libs
from lib.PInode import *
import lib.PIgeneral as PIgeneral
from lib.PIconnection import *
from lib.PIrest import *


reset_delta_count = calendar.timegm(time.gmtime())
track_delta = calendar.timegm(time.gmtime())
delta = 3

lockrest = thread.allocate_lock()
lockcon = thread.allocate_lock()

config = ConfigParser.RawConfigParser()
config.read('server.cfg')
model = config.get('node', 'model')
server_ipaddr = config.get('server', 'ipaddr')
server_port = int(config.get('server', 'port'))
clean_up_and_exit = 0

# ====================================================================
# Register signal
# ====================================================================
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global clean_up_and_exit 
    clean_up_and_exit = 1
    #sys.exit(0)
    #sys.exit(0)

# ====================================================================
# Main entry into the pi-server
# ====================================================================
def main():
    # Register signal ctrl + c
    signal.signal(signal.SIGINT, signal_handler)

    reset_delta_count = calendar.timegm(time.gmtime())
    track_delta = calendar.timegm(time.gmtime())
    delta = 2
 
    pi_rest = PIrest()

    pi_nodes = {}
    # Create a server connection.
    pi_server_con = PIconnection("server", server_ipaddr, server_port)
    pi_server_con.init()
    while 1:
        if clean_up_and_exit == 1:
            #pi_server_con.server_disconnect()
            sys.exit(0)
        time.sleep(0.1)
        #return_value_update, client_addr = pi_server_con.update("server")
        try:
            if not lockcon.locked():
                thread.start_new_thread(pi_server_con.server_update, ("server", pi_nodes, lockcon))
        except:
            print("Unable to start thread.")
        # Track the time between when we send REST updates.
        track_delta = calendar.timegm(time.gmtime())
        if (track_delta - reset_delta_count > delta):
            track_delta = calendar.timegm(time.gmtime())
            reset_delta_count = calendar.timegm(time.gmtime())
            try:
                print lockrest.locked()
                if not lockrest.locked():
                    thread.start_new_thread(pi_rest.post2,("/api/nodes/", json.dumps(pi_nodes), lockrest))
            except:
                print("Unable to start thread.")
            #print pi_nodes

# ====================================================================
# main
# ====================================================================
if __name__ == '__main__':
    main()


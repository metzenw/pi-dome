#!/usr/bin/env python
import ConfigParser
import time
import json
from flask import jsonify
import thread
import calendar


#My own libs
from lib.PInode import *
import lib.PIgeneral as PIgeneral
from lib.PIconnection import *
from lib.PIrest import *


reset_delta_count = calendar.timegm(time.gmtime())
track_delta = calendar.timegm(time.gmtime())
delta = 2

lockrest = thread.allocate_lock()
lockcon = thread.allocate_lock()

config = ConfigParser.RawConfigParser()
config.read('server.cfg')
model = config.get('node', 'model')
server_ipaddr = config.get('server', 'ipaddr')
server_port = int(config.get('server', 'port'))

# ====================================================================
# Main entry into the pi-server
# ====================================================================
def main():
    #pi_node = PInode()
    #pi_node.init("server", model, config) #Supported b, b+, b+2, and c1
    #pi_node.convert_gpio_to_jason()
    reset_delta_count = calendar.timegm(time.gmtime())
    track_delta = calendar.timegm(time.gmtime())
    delta = 2
 
    pi_rest = PIrest()

    pi_nodes = {}

    pi_server_con = PIconnection("server", server_ipaddr, server_port)
    pi_server_con.init()
    #try:
    #    if not lockcon.locked():
    #       pi_server_con.server_update("server")
    #except:
    #    print("Unable to connect to: " + pi_server_con.server_name)
    while 1:
        #pi_node.monitor_gpio()
        print("Loop")
        time.sleep(0.1)
        #return_value_update, client_addr = pi_server_con.update("server")
        try:
            if not lockcon.locked():
                thread.start_new_thread(pi_server_con.server_update, ("server", pi_nodes, lockcon))
        except:
            print("Unable to start thread.")
#        if return_value_update == 0:
#            nothing_here = 0
#        else:
            #Work with jason
            #print("Process jason")
            #pi_nodes[client_addr] = {}
            #pi_nodes[client_addr]["gpio"] = json.loads(return_value_update)
            #for key in pi_nodes[client_addr]["gpio"]:
            #    print pi_nodes[client_addr]["gpio"][key]["gpio_setting"]
            #    print pi_nodes[client_addr]["gpio"][key]["type"]
            #for key in pi_nodes:
                #print("PInodes:" + str(key))
                #print jsonify({ key : pi_nodes[key]["gpio"] })
                #print json.dumps(pi_nodes)
        track_delta = calendar.timegm(time.gmtime())
        if (track_delta - reset_delta_count > delta):
            track_delta = calendar.timegm(time.gmtime())
            reset_delta_count = calendar.timegm(time.gmtime())
            try:
                if not lockrest.locked():
                    thread.start_new_thread(pi_rest.post,("/api/nodes/", json.dumps(pi_nodes), lockrest))
            except:
                print("Unable to start thread.")
                #print(pi_rest.post("/api/nodes/", json.dumps(pi_nodes)))
                #print json.dumps(pi_nodes)
if __name__ == '__main__':
    main()


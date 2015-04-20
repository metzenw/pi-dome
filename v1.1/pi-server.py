#!/usr/bin/env python
import ConfigParser
import time
from lib.PInode import *
import lib.PIgeneral as PIgeneral
from lib.PIconnection import *

config = ConfigParser.RawConfigParser()
config.read('server.cfg')
model = config.get('node', 'model')
server_ipaddr = config.get('server', 'ipaddr')
server_port = int(config.get('server', 'port'))

# ====================================================================
# Main entry into the pi-server
# ====================================================================
def main():
    pi_node = PInode()
    pi_node.init("server", model, config) #Supported b, b+, b+2, and c1
    pi_node.convert_gpio_to_jason()

    pi_server_con = PIconnection("server", server_ipaddr, server_port)
    pi_server_con.init()
    try:
        pi_server_con.update("test")
    except:
        print("Unable to connect to: " + pi_server_con.server_name)
    while 1:
        #pi_node.monitor_gpio()
        time.sleep(0.1)
        pi_server_con.update("test")
        print("Loop")
if __name__ == '__main__':
    main()


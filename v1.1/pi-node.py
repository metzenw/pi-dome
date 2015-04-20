#!/usr/bin/env python
import ConfigParser
import time
from lib.PInode import *
import lib.PIgeneral as PIgeneral
from lib.PIconnection import *

config = ConfigParser.RawConfigParser()
config.read('node.cfg')
model = config.get('node', 'model')
server_ipaddr = str(config.get('server', 'ipaddr'))
server_port = int(config.get('server', 'port'))

# ====================================================================
# Main entry into the pi-node
# ====================================================================
def main():
    pi_node = PInode()
    pi_node.init("node", model, config) #Supported b, b+, b+2, and c1
    pi_node.convert_gpio_to_jason()
 
    pi_client_con = PIconnection("client", server_ipaddr, 9090)
    pi_client_con.init()

    while 1:
        pi_node.monitor_gpio()
        pi_node_jason_gpio = pi_node.convert_gpio_to_jason()
        #print pi_node_jason_gpio
        time.sleep(3.0)

        try:
            pi_client_con = PIconnection("client", server_ipaddr, 9090)
            pi_client_con.update(pi_node_jason_gpio)
            print "Sent msg test to server."
        except:
            print("Unable to connect to: " + pi_client_con.server_name)


# ====================================================================
# Application start
# ====================================================================
if __name__ == '__main__':
    main()


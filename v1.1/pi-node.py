#!/usr/bin/env python
import ConfigParser
import time
from lib.PInode import *
import lib.PIgeneral as PIgeneral


config = ConfigParser.RawConfigParser()
config.read('node.cfg')
model = config.get('node', 'model')
server_ipaddr = config.get('server', 'ipaddr')

# ====================================================================
# Main entry into the pi-node
# ====================================================================
def main():
    pi_node = PInode()
    pi_node.init("node", model, config) #Supported b, b+, b+2, and c1
    while 1:
        pi_node.monitor_gpio()
        time.sleep(0.5)

# ====================================================================
# Application start
# ====================================================================
if __name__ == '__main__':
    main()


#!/usr/bin/env python
import time
from lib.PInode import *
import lib.PIgeneral as PIgeneral


# ====================================================================
# Main entry into the pi-server
# ====================================================================
def main():
    pi_node = PInode()
    pi_node.init("node", "b")
    while 1:
        pi_node.monitor_gpio()
        time.sleep(0.5)
if __name__ == '__main__':
    main()


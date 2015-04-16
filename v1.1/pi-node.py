#!/usr/bin/env python
from lib.PInode import *
import lib.PIgeneral as PIgeneral


# ====================================================================
# Main entry into the pi-server
# ====================================================================
def main():
    pi_node = PInode()
    pi_node.init("node")
    pi_node.monitor_gpio()
if __name__ == '__main__':
    main()


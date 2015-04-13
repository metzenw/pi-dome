#!/usr/bin/env python
from lib.PInode import *
import lib.PIgeneral as PIgeneral


# ====================================================================
# Main entry into the pi-server
# ====================================================================
def main():
    pi_server = PInode()
    pi_server.init()

if __name__ == '__main__':
    main()


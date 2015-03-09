#!/usr/bin/env python

import sys, time, signal
from daemon import Daemon

#s_log = open("/tmp/home_automation.log", "a")
#s_log.write("Opening Log file")

class MyDaemon(Daemon):
   def run(self):
      while True:
         time.sleep(1)
         self.logger.write("INFO:   Daemon running....\n")

#Function to handel signals
#def signalHandler(s_signal,b):
   #print "Signal received ",s_signal,"==",b;
#   tmp_signal_log = "Signal received " + str(s_signal)
#   s_log.write(tmp_signal_log)
#   if s_signal == 15:
#      daemon.stop()
#   if s_signal == 2:
#      daemon.stop()

#Define how to handel signals
#signal.signal(signal.SIGINT,signalHandler);
#signal.signal(signal.SIGUSR1,signalHandler);
#signal.signal(signal.SIGTERM,signalHandler);

if __name__ == "__main__":
   daemon = MyDaemon('/var/run/home_automation.pid')
   if len(sys.argv) == 2:
      if 'start' == sys.argv[1]:
         daemon.start()
      elif 'stop' == sys.argv[1]:
         daemon.stop()
      elif 'restart' == sys.argv[1]:
         daemon.restart()
      else:
         print "Unknown command"
         print sys.argv[1]
         sys.exit(2)
         sys.exit(0)
   else:
      daemon.start()

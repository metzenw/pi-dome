#!/usr/bin/python
#client side
# echo client
from socket import *
from ssl import *

#user is not finnished
finnished =False

#create socket
client_socket=socket(AF_INET, SOCK_STREAM)
tls_client = wrap_socket(client_socket, ssl_version=PROTOCOL_TLSv1, cert_reqs=CERT_NONE)

class PIconnection:
  #'Common base class for PIconnection'#
   def __init__(self, client_or_server):
      self.client_socket = socket(AF_INET, SOCK_STREAM)
      self.tls_client_socket = wrap_socket(self.client_socket, ssl_version=PROTOCOL_TLSv1, cert_reqs=CERT_NONE)
      self.server_name = "localhost"
      self.server_port = 6668
      self.finished = False
      self.service_type = client_or_server
   # ====================================================================
   #  Client Connect - connect to the server
   # ====================================================================
   def client_connect(self):
      #connect to the pi-server
      self.tls_client_socket.connect((self.server_name, self.server_port))

   # ====================================================================
   #  Send to server - send update to server and recieve server 
   #  instructions.
   # ====================================================================
   def send_to_server(self, message):

      data_out= message.encode()
      #send data out
      self.tls_client_socket.send(data_out)    

      #receive data
      data_in=self.tls_client_socket.recv(1024)


      #decode message
      response= data_in.decode()
      print('Received from client:', response)

   # ====================================================================
   #  Client disconnect - disconnect from server
   # ====================================================================
   def client_disconnect(self):
      #close the socket
      self.client_socket.shutdown(SHUT_RDWR)
      self.client_socket.close()

   # ====================================================================
   #  Client client_update - disconnect from server
   # ====================================================================
   def update(self, message):
      if self.service_type == "client":
         self.client_connect()
         self.send_to_server(message)
         self.client_disconnect
      if self.service_type == "server":
         print "server."



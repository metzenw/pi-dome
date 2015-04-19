#!/usr/bin/python
#client side
# echo client
from socket import *
from ssl import *


class PIconnection:
  #'Common base class for PIconnection'#
   def __init__(self, client_or_server, server_name, server_port):
      self.client_socket = socket(AF_INET, SOCK_STREAM)
      self.server_socket = socket(AF_INET, SOCK_STREAM)
      self.tls_client_socket = wrap_socket(self.client_socket, ssl_version=PROTOCOL_TLSv1, cert_reqs=CERT_NONE)
      self.server_name = server_name
      self.server_port = server_port
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
   #  Serve bind - server bind
   # ====================================================================
   def server_bind(self):
      self.server_socket.bind((self.server_name, self.server_port))

      #listen for connection
      self.server_socket.listen (1)
      self.tls_server = wrap_socket(server_socket, ssl_version=PROTOCOL_TLSv1, cert_reqs=CERT_NONE, server_side=True, keyfile='my.key', certfile='my.crt')

      print('server started')

   def server_listen(self):
      #accept connection
      self.connection, client_address= tls_server.accept()
      print ('connection from', client_address)


      #send and receive data from the client socket
      data_in=connection.recv(1024)
      message=data_in.decode()
      print('client send',message)
      message = "Got it!"
      data_out=message.encode()
      connection.send(data_out)

   # ====================================================================
   #  Server cleanup - clean up server connections.
   # ====================================================================
   def server_disconnect(self):
      #close the connection
      self.connection.shutdown(SHUT_RDWR)
      self.connection.close()

      #close the server socket
      self.server_socket.shutdown(SHUT_RDWR)
      self.server_socket.close()





   # ====================================================================
   #  Client client_update - disconnect from server
   # ====================================================================
   def update(self, message):
      if self.service_type == "client":
         print "Client connect."
         self.client_connect()
         self.send_to_server(message)
         self.client_disconnect
      if self.service_type == "server":
         print "Server connect."
         self.server_bind()
         self.server_disconnect()


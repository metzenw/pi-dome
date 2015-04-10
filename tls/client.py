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


#connect to the echo server
tls_client.connect(('localhost',6668))

#while not finnished
while not finnished:

    #message
    message=raw_input('enter message:   ')

    data_out= message.encode()
    #data_out= message

    #send data out
    tls_client.send(data_out)    

    #receive data
    data_in=tls_client.recv(1024)


    #decode message
    response= data_in.decode()
    print('Received from client:', response)
    if response =='quit':
        finnished= True
    else:
        reapet=raw_input('(y)es or (n)o?  ')
        if reapet == 'n':
            #finnished= True
            print("No selected!")
            message = 'quit'
            data_out= message.encode()
            tls_client.send(data_out)
            data_in=tls_client.recv(1024)
            response= data_in.decode()
            if response== 'quit':
                finnished= True

#close the socket
client_socket.shutdown(SHUT_RDWR)
client_socket.close()

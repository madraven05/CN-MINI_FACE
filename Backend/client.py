'''
Python code to define Multi-threaded Client 
'''

import socket

class Client():
    def __init__(self, host, PORT):
        self.host = host
        self.PORT = PORT

    '''
    Create Client Socket
    '''
    def create_client_socket(self):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Client Socket Created!")
        return self.client_socket

    '''
    Client Socket Connect
    '''
    def client_socket_connect(self):
        self.client_socket.connect((self.host, self.PORT))

    '''
    Client Send and Receive
    '''
    def client_snd_and_rcv(self):
        while(1):
            # Perform the necessary functions of send and receive 
            # on the client side

        self.client_socket.close()
'''
Python code to define Multi-Threaded Server
'''

import socket
from _thread import *
import threading

print_lock = threading.Lock()

class Server():
    def __init__(self, PORT, host):
        self.PORT = PORT
        self.host = host

    '''
    Create a server socket
    '''
    def create_server_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return server_socket


    '''
    Bind Socket
    '''
    def bind_server_socket(self, host):   
        self.server_socket.bind((self.host, self.PORT))
        print("Socket Binded to port {}!".format(self.host))

    '''
    Socket Listening
    '''
    def server_socket_listen(self):
        self.server_socket.listen(5)
        print("Server Socket is listening")


    '''
    Server Socket Accept
    '''
    def server_socket_accept(self):
        # Establish connection with client
        client, addr = self.server_socket.accept()

        # Client acquires lock
        print_lock.acquire()
        print("Connected to client: " addr[0])
        return client, addr

    '''
    Connect with Clients and perform Send and Receive
    '''
    def connect_to_clients(self):
        while(1):
            
            client, addr = self.server_accept()
            
            # Perform Threaded Send and Receive
            start_new_thread(self.server_snd_and_rcv(), (client,))

        self.server_socket.close()

    '''
    Server side send and receive
    '''
    def server_snd_and_rcv(self, client):
        while(1):
            # Send and Receive
            # Necessary functions for sending and accepting req/response to be added here
        client.close()
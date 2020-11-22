'''
Python code to define Multi-Threaded Server

CLIENT REQUEST MESSAGE:
------------------------
req_msg = {
    command: "LOGIN/LOGOUT/FETCH...",
    header_lines: {
        server_id: server_id,
        accept_encoding: 'utf-8',
        ... 
    },
    body: 'data'
}

SERVER RESPONSE MESSAGE:
------------------------
response_msg = {
    status_line: {
        protocol: 'TCP/UDP',
        status_code: 200/301...
    },
    header_lines: {
        date: date,
        accept_ranges: bytes,
        content_length: content_length,
        keep_alive: {
            timeout: 10,
            max: 100
        },
        connection: 'keep-alive'
    }
    data: data
}
'''

import socket
from _thread import *
import threading
import pickle

from Backend.database import user_login, user_register

print_lock = threading.Lock()

# Client Request Message
client_req_msg = {
    "command": "",
    "header_lines": {
        "server_id": 12345,
        "accept_encoding": 'utf-8',
    },
    "body": ""
}

# Server Response Message
server_response_msg = {
    "status_line": {
        "protocol": 'TCP',
        "status_code": 1
    },
    "header_lines": {
        "date": "",
        "accept_ranges": bytes,
        "content_length": 0,
        "keep_alive": {
            "timeout": 10,
            "max": 100
        },
        "connection": 'keep-alive'
    },
    "data": ""
}


class Server():
    def __init__(self, PORT, host):
        self.PORT = PORT
        self.host = host

    '''
    Create a server socket
    '''
    def create_server_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server Socket Created!")
        return self.server_socket


    '''
    Bind Socket
    '''
    def bind_server_socket(self):   
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
        print("Connected to client: ", addr[0])
        return client, addr

    '''
    Connect with Clients and perform Send and Receive
    '''
    def connect_to_clients(self):
        while(1):
            
            client, addr = self.server_socket_accept()
            
            # Perform Threaded Send and Receive
            start_new_thread(self.server_snd_and_rcv, (client,))

        self.server_socket.close()

    def get_registration_details(self, client_req_body):
        first_name = client_req_body[0]
        last_name = client_req_body[1]
        username = client_req_body[2]
        password = client_req_body[3]

        return first_name, last_name, username, password

    def get_login_details(self, client_req_body):
        username = client_req_body[0]
        password = client_req_body[1]

        return username, password

    '''
    Server side send and receive
    '''
    def server_snd_and_rcv(self, client):
        while(1):
            # Send and Receive
            # Necessary functions for sending and accepting req/response to be added here
            request = client.recv(1024)
            if request:
                # print("object in bytes: ", request)
                client_req = pickle.loads(request, encoding='utf-8')
                client_req_body = client_req['body']
                client_req_body = client_req_body.split('\n')
                
                # If command is LOGIN
                if client_req['command'] == 'LOGIN':
                    username, password = self.get_login_details(client_req_body)
                    if user_login(username, password):
                        # Sagar username and password will be sent to user_login function in database.py
                        print("User Login Successful!")
                        
                        # Send Server Response

                    else:
                        print("User Login Failed! :(")
                
                # If command is REGISTER
                elif client_req['command'] == 'REGISTER':
                    
                    # print(client_req_body)
                    fname, lname, username, password = self.get_registration_details(client_req_body)
                    
                    if user_register(fname, lname, username, password):
                        # Send to client server success Response
                        print("User Registered!")
                    
                    else:
                        print("User Registration Failed! :(")
                    
            else:
                break
        client.close()

        
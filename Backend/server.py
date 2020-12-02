'''
Python code to define Multi-Threaded Server

CLIENT REQUEST MESSAGE:
------------------------
req_msg = {
    command: "LOGIN/LOGOUT/FETCH...",
    header_lines: {
        server_id: server_id,
        accept_encoding: 'utf-8',
        client_id = ''
        ... 
    },
    body: {
        'sent_to': ...
        'text': ...
    }
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
import datetime
from threading import Thread
# from Backend.database import user_login, user_register, publish_post, fetch_all_users, fetch_user,fetch_posts
from Backend.database import * 

BUFF_SIZE = 32000
####### Status Codes ########
SUCCESS = 200
FAILURE = 404
CHAT_FETCHED = 100
############################
clients={}

#print_lock = threading.Lock()

# Client Request Message
client_req_msg = {
    "command": "",
    "header_lines": {
        "content_length":0,
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
    },
    "data": ""
}


class ClientThread(Thread):
    def __init__(self, PORT, host,client):
        Thread.__init__(self)
        self.PORT = PORT
        self.host = host
        self.client= client
        print("New Thread started")
    '''
    Create a server socket
    
    def create_server_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server Socket Created!")
        return self.server_socket
    '''

    '''
    Bind Socket
    
    def bind_server_socket(self):   
        self.server_socket.bind((self.host, self.PORT))
        print("Socket Binded to port {}!".format(self.host))
    '''
    '''
    Socket Listening
    
    def server_socket_listen(self):
        self.server_socket.listen(5)
        print("Server Socket is listening")
    '''

    '''
    Server Socket Accept
    
    def server_socket_accept(self):
        # Establish connection with client
        client, addr = self.server_socket.accept()

        # Client acquires lock
       
        print("Connected to client: ", addr[0])
        return client, addr
    '''
    '''
    Connect with Clients and perform Send and Receive
    '''
    def run(self):
       
            
        # Perform Threaded Send and Receive
        # print_lock.acquire() # Acquire lock
        #(self.server_snd_and_rcv, (self.client,))
        self.server_snd_and_rcv(self.client)
        

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

    def get_post_details(self, client_req_body):
        author = client_req_body[0]
        title = client_req_body[1]
        content = client_req_body[2]
        published_at = client_req_body[3]
        ownership = client_req_body[4]
        ownership = int(ownership)
        # print(type(ownership))
        return author, title, content, published_at, ownership
    
    def get_message_details(self, client_req_body):
        print(client_req_body)
        username=client_req_body[0]
        message=client_req_body[1]
        send_to=client_req_body[2]
        published_at=client_req_body[3]
        return username,message,send_to,published_at

    '''
    Server side send and receive
    '''
    def server_snd_and_rcv(self, client):
        print("Client Window opened..")
        self.user_n = ""
        while(1):
            # Send and Receive
            # Necessary functions for sending and accepting req/response to be added here
            request = client.recv(1024)
            # print(request)
            # print(request)
            if request:
                # print("object in bytes: ", request)
                client_req = pickle.loads(request, encoding='utf-8')
                client_req_body = client_req['body']
                client_req_body = client_req_body.split('\n')
                
                
                
                ###########################################
                # If command is LOGIN
                ###########################################
                if client_req['command'] == 'LOGIN':
                    username, password = self.get_login_details(client_req_body)
                    clients.update({username:client})
                    if user_login(username, password):
                        # Sagar username and password will be sent to user_login function in database.py
                        print("User Login Successful!")
                        self.user_n = username
                        
                        # online user
                        online(username)
                        
                        # Send Server Response
                        server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                        server_response_msg["status_line"]["status_code"] = SUCCESS # Success status code set!
                        server_response_msg['data'] = ""

                        server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                        # print(server_reponse)
                        client.send(server_reponse) # Send to client! 


                    else:
                        server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                        server_response_msg["status_line"]["status_code"] = FAILURE # Success status code set!
                        server_response_msg['data'] = ""
                        
                        server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                        # print(server_reponse)
                        client.send(server_reponse) # Send to client!

                        print("User Login Failed! :(")
                        
                
                ##############################################
                # If command is LOGOUT
                ##############################################
                
                
                        
                
                elif client_req['command'] == 'LOG_OUT':
                        
                    # print(client_req_body)
                   
                    
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    server_response_msg['data'] = ""

                    if  logout(self.user_n) :
                        server_response_msg["status_line"]["status_code"] = SUCCESS # Success status code set!
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE # Failure status code set!

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 

                
                
                ##############################################
                # If command is REGISTER
                ##############################################
                elif client_req['command'] == 'REGISTER':
                    
                    # print(client_req_body)
                    fname, lname, username, password = self.get_registration_details(client_req_body)
                    
                    if user_register(fname, lname, username, password):
                        # Send to client server success Response
                        print("User Registered!")
                    
                    else:
                        print("User Registration Failed! :(")


                ##############################################
                # If command is PUBLISH
                ##############################################
                elif client_req['command'] == 'PUBLISH':

                    author, title, content, published_at, ownership = self.get_post_details(client_req_body)
                    print("Server received post details!")
                    # Send Server Response
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    server_response_msg['data'] = ""

                    if publish_post(author, title, content, published_at, ownership):
                        server_response_msg["status_line"]["status_code"] = SUCCESS # Success status code set!
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE # Failure status code set!

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 

                
                
                ##############################################
                # If command is FETCH_USERS
                ##############################################
                elif client_req['command'] == 'FETCH_USERS':

                    users = fetch_all_users()
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if users:
                        server_response_msg['data'] = users
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 


                ##############################################
                # If command is FETCH_USER
                ##############################################
                elif client_req['command'] == 'FETCH_USER':
                    
                    search_username = client_req_body[0]
                    user = fetch_user(search_username)

                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if user:
                        server_response_msg['data'] = user
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 

                
                ##############################################
                # If command is FETCH_POSTS
                ##############################################
                elif client_req['command'] == 'FETCH_POSTS':
                    
                    username = client_req['body']
                    posts = fetch_posts(username)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time

                    if posts:
                        server_response_msg['data'] = posts
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 


                ##############################################
                # If command is FETCH_USER_POSTS
                ##############################################
                elif client_req['command'] == 'FETCH_USER_POSTS':
                    
                    user2 = client_req['body']
                    posts = fetch_user_posts(user2)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time

                    if posts:
                        server_response_msg['data'] = posts
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 

                    
                ##############################################
                # If command is FETCH_POSTS
                ###########################################
                elif client_req['command'] == 'FETCH_F_1':
                    
                
                    
                    id1 = user_to_id(self.user_n )
                    # print(self.user_n )
                    # print("check")
                    
                    # print(id1)
                    users = friend_list(id1)
                    # print(users)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if users:
                        server_response_msg['data'] = users
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client! 
                   
                   
                   # not connected users 
                elif client_req['command'] == 'FETCH_F_2':
        
                    id1 = user_to_id(self.user_n )
                    # print(self.user_n )
                    # print("check")
                    
                    # print(id1)
                    users = not_connected(id1)
                    # print(users)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if users:
                        server_response_msg['data'] = users
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client!
                    
                    
                    # pending friend requests 
                        # not connected users 
                elif client_req['command'] == 'FETCH_F_3':
        
                    id1 = user_to_id(self.user_n )
                    # print(self.user_n )
                    # print("check")
                    
                    # print(id1)
                    users = pending_requested_list(id1)
                    # print(users)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if users:
                        server_response_msg['data'] = users
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client!
                    
                    

                elif client_req['command'] == 'FETCH_F_4':
            
                    id1 = user_to_id(self.user_n )
                    # print(self.user_n )
                    # print("check")
                    
                    # print(id1)
                    users = fr_sent_na(id1)
                    # print(users)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if users:
                        server_response_msg['data'] = users
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client!
                    
                    
                ##############################################
                # If command is SEND_CHAT
                ##############################################
                elif client_req['command']=='SEND_CHAT':
                    
                    username, message, send_to, published_at = self.get_message_details(client_req_body)

                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    # Read_bool set to 0 if the client is not active/online
                    if send_to in clients.keys():
                        read_bool = 1
                    else:
                        read_bool = 0

                    # store message in the database
                    if store_message(username, send_to, message, read_bool, published_at):
                        server_response_msg["status_line"]["status_code"] = SUCCESS # Success status code set!
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE # Failure status code set!

                    # If client is active/online, send them the message!
                    if send_to in clients.keys():
                        client1=clients[send_to] ##client1 is client socket of the user to whom we wants to message.
                        finalmessage=username+': '+message
    
                        server_response_msg['data'] = finalmessage

                        server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                            # print(server_reponse)
                        client1.send(server_reponse)


                ##############################################
                # If command is FETCH_CHAT
                ##############################################
                elif client_req['command'] == 'FETCH_CHAT':
                    data = client_req['data'].split(',')

                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    
                    # Username and send_to fetch
                    username = data[0]
                    send_to = data[1]
                    message_list = fetch_chat(username, send_to)
                    if message_list:
                        server_response_msg["status_line"]["status_code"] = CHAT_FETCHED # Success status code set!
                        server_response_msg['data'] = message_list
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE # Failure status code set!
                        
                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    self.client.send(server_reponse)



                ##############################################
                # If command is SEND_REQ
                ##############################################    
                elif client_req['command'] == 'SEND_REQ':
                
                    id1 = user_to_id(self.user_n )
                    # print(self.user_n )
                    # print("check")
                    user2 =  client_req['body'] 
                    print(user2)
                    id2 = user_to_id(user2 )
                    print(id2)
                    
                    
                    # print(id1)
                    
                    # print(users)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if send_req(id1, id2):
                    
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client!
                    
                elif client_req['command'] == 'ACCEPT_REQ':
                    
                    id1 = user_to_id(self.user_n )
                    # print(self.user_n )
                    # print("check")
                    user2 =  client_req['body'] 
                    print(user2)
                    id2 = user_to_id(user2 )
                    print(id2)
                    
                    
                    # print(id1)
                    
                    # print(users)
                    server_response_msg["header_lines"]['date'] = datetime.datetime.now() # Setting the date and time
                    
                    if accept_req(id1, id2):
                    
                        server_response_msg["status_line"]["status_code"] = SUCCESS
                    else:
                        server_response_msg["status_line"]["status_code"] = FAILURE

                    server_reponse = pickle.dumps(server_response_msg) # Convert objects to bytes
                    # print(server_reponse)
                    client.send(server_reponse) # Send to client!
                    
                    


                
                
            else:
                # print_lock.release() # Release Lock here!
                break
        client.close()

        
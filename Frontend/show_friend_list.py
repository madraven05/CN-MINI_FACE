'''
The Write Post Page GUI code
Write Modular (using Functions whenever necessary) and a well commented code! 
'''

from tkinter import *
from tkinter import font
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from Backend.server import client_req_msg, SUCCESS, FAILURE
#from Frontend.homepage import HomePage
import pickle
import datetime
from functools import partial
from Frontend.chat import Chat

class Show_friend_list:
    def __init__(self, root, client_socket, username):
    
        self.root = root 
        self.username = username
        self.root.title("Friend list Window")
        self.root.geometry("910x607+0+0")
        self.client_socket = client_socket

        #Register
        self.Frame_friend=Frame(self.root,bg="white")
        self.Frame_friend.place(x=105,y=150,height=340,width=700)

        # button 1
        My_friends=Button(self.Frame_friend, command = self.myfriend ,cursor="hand2",text="My Friends",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=10,y=10)

         # button 2
        My_friends=Button(self.Frame_friend, command = self.not_connected, cursor="hand2",text="Other Users",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=150,y=10)

         # button 3
        My_friends=Button(self.Frame_friend, command = self.pending_request, cursor="hand2",text="Pending Requests",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=10,y=200)

         # button 4
        My_friends=Button(self.Frame_friend, command = self.pending_by_them, cursor="hand2",text="Sent Requests",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=150,y=200)

       
        



        Exit=Button(self.Frame_friend,cursor="hand2",text="Exit?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        
    def myfriend(self):
        client_req_msg['command'] = "FETCH_F_1"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        if server_response['status_line']['status_code'] == SUCCESS:
            print("Friendlist Fetched!")
 
            friends = server_response['data']
            print(friends)
            
            y = 60
            for f in friends:
                username = Label(self.Frame_friend,text='@' + f,font=("Impact",8),fg="#d77337",bg="white").place(x=10,y=y)
                message=Button(self.Frame_friend,cursor="hand2",text="Message",bg="gray",fg="white",bd=0,font=("Times New Roman",10), command =partial(self.chat_friend,f)).place(x=60,y=y)
                y += 100
            
        
            
        else:
            print("Fetching friends has failed!")
        
        ###############################################################################################################################################
        

        
        
        ################################################### display data ############################################################################

       
        
    def not_connected(self):
        client_req_msg['command'] = "FETCH_F_2"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        
        if  server_response['status_line']['status_code'] == SUCCESS:
            print("Friendlist Fetched!")
 
            friends = server_response['data']
            print(friends)
            
            y = 50
            for f in friends:
                username = Label(self.Frame_friend,text='@' + f,font=("Impact",8),fg="#d77337",bg="white").place(x=150,y=y)
                add_friend=Button(self.Frame_friend,cursor="hand2",text="Add Friend",bg="gray",fg="white",bd=0,font=("Times New Roman",10), command = partial(self.add_friend,f)).place(x=200,y=y)
            
                y += 100
        
    def pending_request(self):
        client_req_msg['command'] = "FETCH_F_3"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        
        if  server_response['status_line']['status_code'] == SUCCESS:
            print("Friendlist Fetched!")
 
            friends = server_response['data']
            print(friends)
            
            y = 250
            for f in friends:
                username = Label(self.Frame_friend,text='@' + f,font=("Impact",8),fg="#d77337",bg="white").place(x=10,y=y)
                accept_friend=Button(self.Frame_friend,cursor="hand2",text="Accept Req",bg="gray",fg="white",bd=0,font=("Times New Roman",10), command = partial(self.accept_req,f)).place(x=60,y=y)
                y += 30
        
    def pending_by_them(self):
        client_req_msg['command'] = "FETCH_F_4"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        
        if  server_response['status_line']['status_code'] == SUCCESS:
            print("Friendlist Fetched!")
 
            friends = server_response['data']
            print(friends)
            
            y = 250
            for f in friends:
                username = Label(self.Frame_friend,text='@' + f,font=("Impact",8),fg="#d77337",bg="white").place(x=150,y=y)
                # add_friend=Button(self.Frame_friend,cursor="hand2",text="Add Friend",bg="gray",fg="white",bd=0,font=("Times New Roman",10), command = self.add_friend).place(x=60,y=y)
                y += 100
    
    def add_friend(self , id2):
        print('add f')
        client_req_msg['command'] = "SEND_REQ"
        client_req_msg['body']  = id2  
        print(id2)
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        
        if  server_response['status_line']['status_code'] == SUCCESS:
            print("Request Sent")
            messagebox.showerror("Success","Request sent",parent=self.root) 
 
            
        else:
            print("Request Not Sent")
            
    def accept_req(self, id2):
        # print('add f')
        client_req_msg['command'] = "ACCEPT_REQ"
        client_req_msg['body']  = id2  
        print(id2)
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        
        if  server_response['status_line']['status_code'] == SUCCESS:
            print("Request Accepted")
            messagebox.showerror("Success","Request accepted",parent=self.root) 
 
            
        else:
            print("Request Not Accepted")
        
            
            
        
        
    
    def chat_friend(self,user):
        master5 = Tk()
        print("Username: ", user)

        app3 = Chat(master5, self.client_socket, self.username,user)
        
        master5.mainloop()
    
    
        
       
        
    
        
            
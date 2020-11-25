'''
The Home Page GUI code
Write Modular (using Functions whenever necessary) and a well commented code! 
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from Backend.server import client_req_msg, SUCCESS, FAILURE
import pickle
import datetime
from Frontend.writepostpage import WritePostPage 
class HomePage:
    '''
    Here Posts will be shown
    '''
    def __init__(self, root, client_socket, username):
        
        self.root = root 
        self.username = username
        self.root.title("Home Window")
        self.root.geometry("910x607+0+0")
        self.client_socket = client_socket

        #Register
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=105,y=150,height=340,width=700)

        #Post=Button(Frame_login,cursor="hand2",text="Write Post",bg="white",fg="#d77337",font=("Times New Roman",15), command = self.write_post_page(username)).place(x=300+150,y=50)
        # Server request - Fetch all users!
        client_req_msg['command'] = "FETCH_USERS"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [username, username, ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary
        Post=Button(Frame_login,command=self.call1,cursor="hand2",text="Write Post",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=400,y=200)
        
        if server_response['status_line']['status_code'] == SUCCESS:
            print("Users Fetched!")

            users = server_response['data']

            y = 10
            for user in users:
                if user != self.username:
                    username=Label(Frame_login,text=user,font=("Impact",15,"bold"),fg="#d77337",bg="white").place(x=70,y=y)
                    add_friend=Button(Frame_login,cursor="hand2",text="Add Friend",bg="white",fg="#d77337",bd=0,font=("Times New Roman",15), command = self.add_friend).place(x=300,y=y)
                    y += 50
        
            # i = 1
            # Lb1 = Listbox(self.root)
            # for user in users:
            #     Lb1.insert(i, user)
            #     i+=1
            
        else:
            print("Post publishing failed! :(")
        # show all users -> button = "Add Friend"
    def call1(self):
        self.write_post_page(self.username)
    def write_post_page(self, username):    
        
        master3 = Tk()

        app3 = WritePostPage(master3, self.client_socket, username)
        
        master3.mainloop()    

    def add_friend(self):
        pass
        
        # # First Name
        # lbl=Label(Frame_login,text="Title",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        # self.txt_title=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        # self.txt_title.place(x=70,y=170,width=200,height=35)  

        # # Last Name
        # lbl=Label(Frame_login,text="Content ",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=140)
        # self.txt_content=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        # self.txt_content.place(x=350,y=170,width=200,height=35)     
    
           

        # Exit=Button(Frame_login,cursor="hand2",text="Exit?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        # Post=Button(self.root,command=self.publish_post,cursor="hand2",text="Post",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=320,y=470,width=180,height=40)
        
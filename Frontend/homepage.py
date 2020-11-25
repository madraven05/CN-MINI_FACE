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
        self.root.geometry("900x600+0+0")
        self.client_socket = client_socket

        ###################################### show all users ##########################################################################
        Frame_users=Frame(self.root,bg="gray")
        Frame_users.place(x=650,y=20,height=700,width=300)

        #Post=Button(Frame_users,cursor="hand2",text="Write Post",bg="white",fg="#d77337",font=("Times New Roman",15), command = self.write_post_page(username)).place(x=300+150,y=50)
        # Server request - Fetch all users!
        client_req_msg['command'] = "FETCH_USERS"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [username, username, ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary
        
        if server_response['status_line']['status_code'] == SUCCESS:
            print("Users Fetched!")

            users = server_response['data']
            
        else:
            print("Fetching users failed!");
            # add message box here!

        ################################################### fetch all post ##########################################################################
        Frame_posts=Frame(self.root,bg="white")
        Frame_posts.place(x=150,y=50,height=700,width=450)

        client_req_msg['command'] = "FETCH_POSTS"
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> [[post], [post], ....]
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

        if server_response['status_line']['status_code'] == SUCCESS:
            print("Posts Fetched!")

            posts = server_response['data']
            
        else:
            print("Fetching users failed!");

        


        ################################################### display data ############################################################################
        y = 10
        for user in users:
            if user != self.username:
                username=Label(Frame_users,text=user,font=("Impact",10),fg="#d77337",bg="white").place(x=10,y=y)
                add_friend=Button(Frame_users,cursor="hand2",text="Add Friend",bg="white",fg="#d77337",bd=0,font=("Times New Roman",10), command = self.add_friend).place(x=60,y=y)
                y += 30

        y = 50
        for post in posts:
            username = Label(Frame_posts,text='@' + post[0],font=("Impact",8),fg="#d77337",bg="white").place(x=10,y=y)
            published_at = Label(Frame_posts,text=post[3],font=("Impact",5),fg="gray",bg="white").place(x=50,y=y)
            title = Label(Frame_posts,text=post[1],font=("Impact",15, "bold"),fg="#d77337",bg="white").place(x=10,y=y+15)
            content = Label(Frame_posts,text=post[2],font=("Impact",10),fg="#d77337",bg="white").place(x=10,y=y+40)
            y += 100

        Post=Button(Frame_posts,command=self.write_post_page,cursor="hand2",text="Write Post",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=10,y=10)
        
            # break


    
    def write_post_page(self):    
        
        master3 = Tk()
        # print("Username: ", self.user)

        app3 = WritePostPage(master3, self.client_socket, self.username)
        
        master3.mainloop()    

    def add_friend(self):
        pass
        
        # # First Name
        # lbl=Label(Frame_users,text="Title",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        # self.txt_title=Entry(Frame_users,font=("Times New Roman",15),bg="lightgray")  
        # self.txt_title.place(x=70,y=170,width=200,height=35)  

        # # Last Name
        # lbl=Label(Frame_users,text="Content ",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=140)
        # self.txt_content=Entry(Frame_users,font=("Times New Roman",15),bg="lightgray")  
        # self.txt_content.place(x=350,y=170,width=200,height=35)     
    
           

        # Exit=Button(Frame_users,cursor="hand2",text="Exit?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        # Post=Button(self.root,command=self.publish_post,cursor="hand2",text="Post",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=320,y=470,width=180,height=40)
        
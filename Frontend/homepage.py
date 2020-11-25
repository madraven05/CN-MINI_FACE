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

        self.users = 0

        ###################################### search from registered users ##########################################################################
        
        self.Frame_users=Frame(self.root,bg="gray")
        self.Frame_users.place(x=650,y=20,height=700,width=300)

        self.txt_search=Entry(self.Frame_users,font=("Times New Roman",15),bg="lightgray")  
        self.txt_search.place(x=5,y=10,width=200,height=35)
        search_btn = Button(self.Frame_users,command=self.search_users,cursor="hand2",text="Search",bg="gray",fg="white",font=("Times New Roman",15)).place(x=5,y=60) 
        search_all_btn = Button(self.Frame_users,command=self.search_all_users,cursor="hand2",text="Search All",bg="gray",fg="white",font=("Times New Roman",15)).place(x=100,y=60) 

        ###############################################################################################################################################




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
        
        ###############################################################################################################################################
        

        
        
        ################################################### display data ############################################################################

        y = 50
        for post in posts:
            username = Label(Frame_posts,text='@' + post[0],font=("Impact",8),fg="#d77337",bg="white").place(x=10,y=y)
            published_at = Label(Frame_posts,text=post[3],font=("Impact",5),fg="gray",bg="white").place(x=50,y=y)
            title = Label(Frame_posts,text=post[1],font=("Impact",15, "bold"),fg="#d77337",bg="white").place(x=10,y=y+15)
            content = Label(Frame_posts,text=post[2],font=("Impact",10),fg="#d77337",bg="white").place(x=10,y=y+40)
            y += 100

        Post=Button(Frame_posts,command=self.write_post_page,cursor="hand2",text="Write Post",bg="white",fg="#d77337",font=("Times New Roman",15)).place(x=10,y=10)
        
        ###############################################################################################################################################


    '''
    Open Write Post Window
    '''
    def write_post_page(self):    
        
        master3 = Tk()
        # print("Username: ", self.user)

        app3 = WritePostPage(master3, self.client_socket, self.username)
        
        master3.mainloop()    


    '''
    when 'Search all users' button is clicked
    '''
    def search_all_users(self):
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

        ################################################### display all users ############################################################################
        
            y = 100
            for user in users:
                if user != self.username:
                    username=Label(self.Frame_users,text=user,font=("Impact",10),fg="white",bg="gray").place(x=10,y=y)
                    add_friend=Button(self.Frame_users,cursor="hand2",text="Add Friend",bg="gray",fg="white",bd=0,font=("Times New Roman",10), command = self.add_friend).place(x=60,y=y)
                    y += 30
            
        else:
            print("Fetching users failed!");
            # add message box here!
        
        ###############################################################################################################################################



    '''
    When username in search field is entered
    '''
    def search_users(self):
        # Server request - Fetch all users!
        client_req_msg['command'] = "FETCH_USER"
        client_req_msg['body'] = self.txt_search.get().lower() # get the searched user entry
        print(self.txt_search.get().lower())
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)

        # Server Response -> user or user not found!
        server_response = self.client_socket.recv(1024) # receive from server
        server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary
        
        if server_response['status_line']['status_code'] == SUCCESS:
            print("Users Fetched!")
            searched_user = server_response['data']

            ################################################### display searched users ############################################################################
        
            y = 100
            username=Label(self.Frame_users,text=searched_user,font=("Impact",10),fg="white",bg="gray").place(x=10,y=y)
            add_friend=Button(self.Frame_users,cursor="hand2",text="Add Friend",bg="gray",fg="white",bd=0,font=("Times New Roman",10), command = self.add_friend).place(x=60,y=y)
        
            ###############################################################################################################################################
            
        else:
            print("Fetching user failed!");
            messagebox.showerror("Error","Incorrect username!",parent=self.root)
    


    '''
    Add friend
    '''
    def add_friend(self):
        pass
        
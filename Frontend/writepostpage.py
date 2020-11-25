'''
The Write Post Page GUI code
Write Modular (using Functions whenever necessary) and a well commented code! 
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from Backend.server import client_req_msg, SUCCESS, FAILURE
#from Frontend.homepage import HomePage
import pickle
import datetime

class WritePostPage:
    def __init__(self, root, client_socket, username):
    
        self.root = root 
        self.username = username
        self.root.title("Write Post Window")
        self.root.geometry("910x607+0+0")
        self.client_socket = client_socket

        #Register
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=105,y=150,height=340,width=700)


        title=Label(Frame_login,text="Write Post",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=70,y=30)
        desc=Label(Frame_login,text="Fill the details",font=("Calibiri",15,"bold"),fg="#d25d17",bg="white").place(x=70,y=100)
    
        # First Name
        lbl=Label(Frame_login,text="Title",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        self.txt_title=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_title.place(x=70,y=170,width=200,height=35)  

        # Last Name
        lbl=Label(Frame_login,text="Content ",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=140)
        self.txt_content=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_content.place(x=350,y=170,width=200,height=35)     
    
           

        Exit=Button(Frame_login,cursor="hand2",text="Exit?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        Post=Button(self.root,command=self.publish_post,cursor="hand2",text="Post",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=320,y=470,width=180,height=40)
        
        
    def publish_post(self):
        if self.txt_title.get()=="" or self.txt_content.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)    

        
            # Send server the register info using the client socket
        # title = self.txt_title.get()
        # content = self.txt_content.get()
        else:
            published_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            author = self.username 
            
            
            client_req_msg['command'] = "PUBLISH"
            client_req_msg['body'] = author + '\n' + self.txt_title.get() + '\n' + self.txt_content.get() + '\n' + published_at 
            
            
            client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
            self.client_socket.send(client_req)
            
            # Receive Server Response and show success message!
            server_response = self.client_socket.recv(1024) # receive from server
            server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary
        
            if server_response['status_line']['status_code'] == SUCCESS:
                print("Post published at: ", published_at)

               # master4 = Tk()

              #  app4 = HomePage(master4, self.client_socket, self.username)

                self.root.destroy()
                
              #  master4.mainloop()   # third window

            
            else:
                print("Post publishing failed! :(")

        
        
            
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

class Chat:
    def __init__(self, root, client_socket, username,send_to):
        self.send_to=send_to
        self.root = root 
        self.username = username
        self.root.title("Write Chat Window")
        self.root.geometry("910x607+0+0")
        self.client_socket = client_socket
        
        #Register
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=105,y=150,height=340,width=700)
        
        
        title=Label(self.root,text="Write Message",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=450,y=30)
     #   desc=Label(Frame_login,text="Fill the details",font=("Calibiri",15,"bold"),fg="#d25d17",bg="white").place(x=70,y=100)
    
        # First Name
        lbl=Label(Frame_login,text="Title",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        self.txt_title=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_title.place(x=70,y=170,width=200,height=35)  
        '''
        # Last Name
        lbl=Label(Frame_login,text="Content ",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=140)
        self.txt_content=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_content.place(x=350,y=170,width=200,height=35)     
        '''
           

        Exit=Button(Frame_login,cursor="hand2",text="Exit?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        
        Post=Button(self.root,command=self.send_message,cursor="hand2",text="Send",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=320,y=470,width=180,height=40)
        
        
    def send_message(self):
        if self.txt_title.get()=="":
            messagebox.showerror("Error","Please Write some message.",parent=self.root)    

        
            # Send server the register info using the client socket
        # title = self.txt_title.get()
        # content = self.txt_content.get()
        else:
            published_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         #   author = self.username 
           # print(self.username,self.txt_title.get(),self.send_to,published_at)
            
            client_req_msg['command'] = "SEND_CHAT"
            client_req_msg['body'] = self.username+ '\n' + self.txt_title.get()+ '\n' + self.send_to +'\n' + published_at 
            
            
            client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
            self.client_socket.send(client_req)
            try:
            # Receive Server Response and show success message!
                while True:
                    server_response = self.client_socket.recv(1024) # receive from server
                    server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary
        
                    if server_response['status_line']['status_code'] == SUCCESS:
                        print(server_response['data'])

               #master4 = Tk()

              #app4 = HomePage(master4, self.client_socket, self.username)

                        
                 
              #  master4.mainloop()   # third window

            
                    else:
                        print("Message not sent! :(")
            except Exception as e:
        # Any other exception - something happened, exit
                print('Reading error: '.format(str(e)))
                self.root.destroy()
            
        

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from Backend.server import client_req_msg, SUCCESS, FAILURE
from Frontend.writepostpage import WritePostPage
from Frontend.homepage import HomePage
import pickle
import datetime

class LoginPage:
    def __init__(self,root, client_socket):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("910x607")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="Frontend/templates/Image3.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.client_socket = client_socket

        #LoginFrame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=205,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=70,y=30)
        desc=Label(Frame_login,text="Login Area",font=("Calibiri",15,"bold"),fg="#d25d17",bg="white").place(x=70,y=100)
       
        lbl=Label(Frame_login,text="Username",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        self.txt_user=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_user.place(x=70,y=170,width=350,height=35)     
        #title=Label(Frame_login,text="Login",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        lbl_pass=Label(Frame_login,text="Password",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=210)
        self.txt_pass=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_pass.place(x=70,y=240,width=350,height=35)   

        Reg_btn=Button(Frame_login,command= self.register, cursor="hand2",text="Create Your Account!",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12)).place(x=70,y=280) 
        Login_btn=Button(self.root,command=self.Login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=390,y=470,width=180,height=40) 
    
    '''
    Login Function for the GUI
    '''
    def Login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        
        else:
            username = self.txt_user.get()
            # Send server the login info as Client Request using client socket
            client_req_msg['command'] = "LOGIN"
            client_req_msg['body'] = self.txt_user.get() + '\n' + self.txt_pass.get()
            client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
            print(client_req)
            self.client_socket.send(client_req) 
            
            # Receive Server Response and show success message!
            server_response = self.client_socket.recv(1024) # receive from server
            server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

            if server_response['status_line']['status_code'] == SUCCESS:
                # Login Successful!
                messagebox.showinfo('Welcome',"Login Successful!",parent=self.root)
                
                # Move to homepage
                print("Login Successful!")
                
                self.root.destroy()
                # no GUI, terminal pe ask user to write post!
                self.home_page(username)
                

            else:
                # Login Failed
                messagebox.showinfo("Login Failed! :(",'Wrong Username or Password',parent=self.root)
                print("Login Failed! :(")


    # second window (registration window)
    def register(self):    
        
        master2 = Tk()

        app = RegisterPage(master2, self.client_socket)
        
        master2.mainloop()   # second window
        
    def write_post_page(self, username):    
        
        master3 = Tk()

        app3 = WritePostPage(master3, self.client_socket, username)
        
        master3.mainloop()   # third window
    def home_page(self, username):    
        
        master4 = Tk()

        app3 = HomePage(master4, self.client_socket, username)
        
        master4.mainloop()    
    
    


class RegisterPage:
    def __init__(self, root, client_socket):

        self.root = root 
        self.root.title("Register Window")
        self.root.geometry("910x607+0+0")
        self.client_socket = client_socket

        #Register
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=105,y=150,height=340,width=700)


        title=Label(Frame_login,text="Register your account",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=70,y=30)
        desc=Label(Frame_login,text="Fill the details",font=("Calibiri",15,"bold"),fg="#d25d17",bg="white").place(x=70,y=100)
    
        # First Name
        lbl=Label(Frame_login,text="First Name",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        self.txt_fname=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_fname.place(x=70,y=170,width=200,height=35)  

        # Last Name
        lbl=Label(Frame_login,text="Last Name",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=140)
        self.txt_lname=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_lname.place(x=350,y=170,width=200,height=35)     
    
        # Username
        lbl_pass=Label(Frame_login,text="Username",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=210)
        self.txt_username=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_username.place(x=70,y=240,width=200,height=35)  

        # Password
        lbl_pass=Label(Frame_login,text="Password",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=210)
        self.txt_password=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_password.place(x=350,y=240,width=200,height=35)   

        Go_to_login=Button(Frame_login,cursor="hand2",text="Already have an account?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        Register_button=Button(self.root,command=self.Register_function,cursor="hand2",text="Register",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=320,y=470,width=180,height=40)
        
        
    def Register_function(self):
        check =0
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)    

        else:
            # Send server the register info using the client socket
            client_req_msg['command'] = 'REGISTER'
            client_req_msg['body'] = self.txt_fname.get() + '\n' + self.txt_lname.get() + '\n' + self.txt_username.get() + '\n' + self.txt_password.get()
            client_req = pickle.dumps(client_req_msg) # Conver client req msg to bytes
            self.client_socket.send(client_req)
            

                    
           
            
            
            
            


    
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from Backend.server import client_req_msg
import pickle

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
    
    def Login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        
        else:

            # Send server the login info as Client Request using client socket
            client_req_msg['command'] = "LOGIN"
            client_req_msg['body'] = self.txt_user.get() + ',' + self.txt_pass.get()
            client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
            self.client_socket.send(client_req) 
            
            # Receive Server Response and show success message!
            

            messagebox.showinfo("Information sent to server",parent=self.root)

            

    # second window (registration window)
    def register(self):    
        
        master2 = Tk()

        app = RegisterPage(master2, self.client_socket)
        
        master2.mainloop()   # second window


class RegisterPage:
    def __init__(self, root, client_socket):

        self.root = root 
        self.root.title("Register Window")
        self.root.geometry("910x607+0+0")
        self.client_socket = client_socket

        #LoginFrame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=105,y=150,height=340,width=700)


        title=Label(Frame_login,text="Register your account",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=70,y=30)
        desc=Label(Frame_login,text="Fill the details",font=("Calibiri",15,"bold"),fg="#d25d17",bg="white").place(x=70,y=100)
    
        #entry 1
        lbl=Label(Frame_login,text="Entry1",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        self.txt_entry1=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_entry1.place(x=70,y=170,width=200,height=35)  

        #entry 2
        lbl=Label(Frame_login,text="Entry2",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=140)
        self.txt_entry2=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_entry2.place(x=350,y=170,width=200,height=35)     
    
        #entry 3
        lbl_pass=Label(Frame_login,text="Entry3",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=210)
        self.txt_entry3=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_entry3.place(x=70,y=240,width=200,height=35)  

        #entry 4
        lbl_pass=Label(Frame_login,text="Entry4",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=350,y=210)
        self.txt_entry4=Entry(Frame_login,font=("Times New Roman",15),bg="lightgray")  
        self.txt_entry4.place(x=350,y=240,width=200,height=35)   

        Go_to_login=Button(Frame_login,cursor="hand2",text="Already have an account?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12), command = self.root.destroy).place(x=70,y=280)
        Register_button=Button(self.root,command=self.Register_function,cursor="hand2",text="Register",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=320,y=470,width=180,height=40)
        
        
    def Register_function(self):
        check =0
        if self.txt_entry1.get()=="" or self.txt_entry2.get()=="" or self.txt_entry3.get()=="" or self.txt_entry4.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)    

        else:
            # Send server the register info using the client socket
            self.client_socket.send(self.txt_entry1.get().encode('utf-8'))
            # pass
'''
The Login Post Page GUI code
Write Modular (using Functions whenever necessary) and a well commented code! 
'''
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class LoginPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("910x607")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="/home/pranshu/Documents/Acads/CN/Project/MINI_FACE/CN-MINI_FACE/Frontend/templates/Image3.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

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

        forget_btn=Button(Frame_login,cursor="hand2",text="Forget Password?",bg="white",fg="#d77337",bd=0,font=("Times New Roman",12)).place(x=70,y=280) 
        Login_btn=Button(self.root,command=self.Login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=390,y=470,width=180,height=40) 
    
    def Login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        elif self.txt_pass.get()!="12345" or self.txt_user.get()!="neel.kirankumar":
            messagebox.showerror("Error","Invalid Username/Password.",parent=self.root)
        else:
            messagebox.showinfo("Welcome",parent=self.root)


root=Tk()
obj=LoginPage(root)
root.mainloop()
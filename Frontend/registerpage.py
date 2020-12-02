'''
The Register Page GUI code 
'''
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class RegisterPage():
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("910x607")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="/home/pranshu/Documents/Acads/CN/Project/MINI_FACE/CN-MINI_FACE/Frontend/templates/Image3.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # Register Frame
        Frame_register=Frame(self.root,bg="white")
        Frame_register.place(x=205,y=150,height=340,width=500)

        title=Label(Frame_register,text="Register",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=70,y=30)
        desc=Label(Frame_register,text="Register Area",font=("Calibiri",15,"bold"),fg="#d25d17",bg="white").place(x=70,y=100)
       
        lbl=Label(Frame_register,text="Username",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=140)
        self.txt_user=Entry(Frame_register,font=("Times New Roman",15),bg="lightgray")  
        self.txt_user.place(x=70,y=170,width=350,height=35)     
        #title=Label(Frame_login,text="Login",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        lbl_pass=Label(Frame_register,text="Password",font=("Calibiri",15,"bold"),fg="gray",bg="white").place(x=70,y=210)
        self.txt_pass=Entry(Frame_register,font=("Times New Roman",15),bg="lightgray")  
        self.txt_pass.place(x=70,y=240,width=350,height=35)   

        register_btn=Button(self.root,command=self.register_function,cursor="hand2",text="Register",fg="white",bg="#d77337",font=("Times New Roman",20)).place(x=390,y=470,width=180,height=40) 

    def register_function(self):
        

root=Tk()
obj=RegisterPage(root)
root.mainloop()
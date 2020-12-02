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
import threading
import datetime

class ReceiveThread(threading.Thread):
    def __init__(self, msg_list, client_socket):
        threading.Thread.__init__(self)
        self.msg_list = msg_list
        self.client_socket = client_socket

    def run(self):
        try:
            # Receive Server Response and show success message!
                while True:
                    server_response = self.client_socket.recv(1024) # receive from server
                    server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

                    if server_response['status_line']['status_code'] == SUCCESS:
                        # print("server response: ",server_response['data'])
                        rcv_msg = server_response['data']
                        self.msg_list.insert(tk.END, rcv_msg)
                        
                    else:
                        print("Message not sent! :(")
        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))



class Chat:
    def __init__(self, root, client_socket, username,send_to):
        self.send_to=send_to
        self.root = root 
        self.username = username
        self.send_to = send_to
        self.root.geometry("400x400")
        self.root.title("Chatting With @" + send_to)
        # self.root.geometry("910x607+0+0")
        self.client_socket = client_socket
        

        messages_frame = tk.Frame(self.root)
        messages_frame.place(x=10,y=10,height=200,width=200)
        # self.my_msg = tk.StringVar()  # For the messages to be sent.
        # my_msg.set("Type your messages here.")
        scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = tk.Listbox(messages_frame, height=25, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        messages_frame.pack()

        self.my_msg=Entry(messages_frame,font=("Times New Roman",15),bg="white")

        # entry_field = tk.Entry(self.root, textvariable=self.my_msg)
        # entry_field.place(x=10,y=170,width=50,height=35) 
        # entry_field.bind("<Return>", self.send_message)
        self.my_msg.pack()
        send_button = tk.Button(self.root, text="Send", command=self.send_message)
        send_button.pack()

        # Receive thread start -- A seperate thread for receiving messages
        # bucket = Queue.Queue()
        receive_thread = ReceiveThread(self.msg_list, self.client_socket)
        receive_thread.setDaemon(True)
        receive_thread.start()

        
    def send_message(self):
        if self.my_msg.get()=="":
            messagebox.showerror("Error","Please Write some message.",parent=self.root)    

    
        else:
            published_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         
            client_req_msg['command'] = "SEND_CHAT"
            client_req_msg['body'] = self.username+ '\n' + self.my_msg.get()+ '\n' + self.send_to +'\n' + published_at 
            
            
            client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
            self.client_socket.send(client_req)
            
            self.msg_list.insert(tk.END, self.username + ": " + self.my_msg.get())
            self.my_msg.set("")
                        
        

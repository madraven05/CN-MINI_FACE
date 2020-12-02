'''
The Write Post Page GUI code
Write Modular (using Functions whenever necessary) and a well commented code! 
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from Backend.server import client_req_msg, SUCCESS, FAILURE, BUFF_SIZE, CHAT_FETCHED
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
                    server_response = self.client_socket.recv(BUFF_SIZE) # receive from server
                    server_response = pickle.loads(server_response, encoding='utf-8') # convert to dictionary

                    if server_response['status_line']['status_code'] == SUCCESS:
                        # print("server response: ",server_response['data'])
                        rcv_msg = server_response['data']
                        self.msg_list.insert(tk.END, rcv_msg)

                    elif server_response['status_line']['status_code'] == CHAT_FETCHED:
                        # Get previous messages and update GUI
                        message_list = server_response['data']
                        for message in message_list:
                            self.msg_list.insert(tk.END, message[0])
                        # pass
        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))



class Chat:
    def __init__(self, root, client_socket, username,send_to):
        self.send_to=send_to
        self.root = root 
        self.username = username
        self.send_to = send_to
        self.root.geometry("800x800")
        self.root.title("Chatting With @" + send_to)
        self.client_socket = client_socket

        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Request Previous Messages
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~
        client_req_msg['command'] = "FETCH_CHAT"
        client_req_msg['data'] = username + ',' + send_to
        client_req = pickle.dumps(client_req_msg) # convers the client req message to bytes
        self.client_socket.send(client_req)
        
        #########################################################################################
        messages_frame = tk.Frame(self.root)
        messages_frame.place(x=10,y=10,height=200,width=200)
        
        scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
        
        self.msg_list = tk.Listbox(messages_frame, height=25, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        messages_frame.pack()

        self.my_msg=Entry(messages_frame,font=("Times New Roman",15),bg="white")
        self.my_msg.pack()
        send_button = tk.Button(self.root, text="Send", command=self.send_message)
        send_button.pack()
        ###########################################################################################
        
        # Start Receive Thread!
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
            self.my_msg.delete(0, 'end')
        

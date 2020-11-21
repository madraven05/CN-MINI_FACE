'''
Python code to define Multi-threaded Client 
'''

import socket
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from Frontend.loginreg import LoginPage

class Client():
    def __init__(self, host, PORT):
        self.host = host
        self.PORT = PORT

    '''
    Create Client Socket
    '''
    def create_client_socket(self):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Client Socket Created!")

    '''
    Client Socket Connect
    '''
    def client_socket_connect(self):
        self.client_socket.connect((self.host, self.PORT))
        print("Client Connected!")
        root = Tk()
        obj = LoginPage(root, self.client_socket)
        root.mainloop()
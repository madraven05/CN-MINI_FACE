from Backend.client import Client

import socket

host = socket.gethostname()
PORT = 12345

client = Client(host, PORT)

client.create_client_socket()
client.client_socket_connect()

client.client_snd_and_rcv()